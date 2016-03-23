from cx_Freeze import setup, Executable
import os
import shutil
import subprocess
import sys
import platform
import PyQt5
sys.path.append('ui')
sys.path.append('images')
from libglparchis import version

def winversion():
    lastpoint="0"
    if version.find("+")!=-1:
        lastpoint="1"
        
    versio=version.replace("+","")
    return versio[:-4]+"."+versio[4:-2]+"."+versio[6:]+"."+lastpoint
    
def build_dir():
    pyversion="{}.{}".format(sys.version_info[0], sys.version_info[1])
    if sys.platform=="win32":
        so="win"
        if platform.architecture()[0]=="64bit":
            pl="amd64"
        else:
            pl="win32"
    else:#linux
        so="linux"
        if platform.architecture()[0]=="64bit":
            pl="x86_64"
        else:
            pl="x86"
    return "build/exe.{}-{}-{}".format(so, pl, pyversion)
    
def filename_output():
    if sys.platform=="win32":
        so="windows"
        if platform.architecture()[0]=="64bit":
            pl="amd64"
        else:
            pl="win32"
    else:#linux
        so="linux"
        if platform.architecture()[0]=="64bit":
            pl="x86_64"
        else:
            pl="x86"
    return "glparchis-{}-{}.{}".format(so,  version, pl)

print ("Building for", sys.platform, version, winversion())
name="glParchis"

#Add files for all platforms
include_files=['sounds/', 'images/ficharoja.ico', 'GPL-3.txt']
include_files.append(('i18n', 'i18n')) #include files puede ser tambien una tupla (origen,destino)

#Build options
if sys.platform=='win32':
        shutil.rmtree("build/", ignore_errors=True)
        base = 'Win32GUI'     
        include_files.append((PyQt5.__path__[0]+'/plugins/audio/qtaudio_windows.dll', 'audio/qtaudio_windows.dll' ))#Si no no sonaba en windows solo
        include_files.append('glparchis.iss')
        build_exe_options = dict(
           create_shared_zip=False,
           includes = ['OpenGL','OpenGL.platform.win32','OpenGL.arrays','OpenGL.arrays.ctypesarrays', 'OpenGL.arrays.lists','OpenGL.converters','PyQt5.QtNetwork'],
           excludes=[], 
           include_files=include_files
           )

        options={
      #'bdist_msi': build_msi_options,
               'build_exe': build_exe_options
               }
               
               
               
else:#linux
        base="Console"
        build_options = dict(
           includes = ['OpenGL','OpenGL.platform.glx','OpenGL.arrays','OpenGL.arrays.ctypesarrays', 'OpenGL.arrays.lists','OpenGL.converters','PyQt5.QtNetwork'], 
           excludes = [], 
           include_files=include_files
           )
        options=dict(build_exe = build_options)

executables = [
      Executable('glparchis.py', base=base, icon='images/ficharoja.ico', shortcutName= name, shortcutDir='ProgramMenuFolder')
]

setup(name=name,
      version = winversion(),
      author = 'Mariano Muñoz',
      description = 'Parcheesi Game',
      options = options,
      executables = executables)


#Post setup
if sys.platform=="win32":
    os.chdir(build_dir())
    subprocess.call(["c:/Program Files (x86)/Inno Setup 5/ISCC.exe",  "/o../",  "/DVERSION_NAME={}".format(winversion()), "/DFILENAME={}".format(filename_output()),"glparchis.iss"], stdout=sys.stdout)
else:   #Linux
    print (build_dir(), filename_output(), os.getcwd())
    pwd=os.getcwd()
    os.chdir(build_dir())
    print (build_dir(), filename_output(), os.getcwd())
    os.system("tar cvz -f '{0}/build/{1}.tar.gz' * -C '{0}/{2}/'".format(pwd, filename_output(),  build_dir()))
