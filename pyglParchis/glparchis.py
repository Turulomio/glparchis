#!/usr/bin/python3
import sys, os, datetime
#
#so="src.linux" #src.linux src.windows bin.linux bin.windows. Se debe cambiar antes de compilar
#os.environ['glparchisso']=so
#if sys.platform=="linux":
#    sys.path.append("/usr/lib/glparchis")
#if so=="bin.windows":
#    sys.path.append("../lib/glparchis")
#elif so=="src.linux" or so=="bin.linux":
#    
    


if sys.platform=='win32':
    sys.path.append("ui")
    sys.path.append("images")
else:
    sys.path.append("../lib/glparchis")
    sys.path.append("/usr/lib/glparchis")

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from frmMain import *

try:
    os.makedirs(os.path.expanduser("~/.glparchis/"))
except:
    pass

sys.setrecursionlimit(100000)

cfgfile=ConfigFile(os.path.expanduser("~/.glparchis/") +"glparchis.cfg")
cfgfile.save()

app = QApplication(sys.argv)
app.setApplicationName("glParchis {0}".format(str(datetime.datetime.now())))
app.setQuitOnLastWindowClosed(True)
if not sys.platform=='win32':
    try:
        from PyQt5.phonon import Phonon
        borrar= Phonon.MediaObject(app)
    except ImportError:
        QMessageBox.critical(None, "glParchis",  "Tu instalación QT no tiene soporte Phonon")
        sys.exit(1)

from libglparchis import cargarQTranslator
cfgfile.qtranslator=QTranslator()
cargarQTranslator(cfgfile)

frmMain = frmMain(cfgfile) 
frmMain.show()
sys.exit(app.exec_())

