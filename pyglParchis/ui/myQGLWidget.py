import datetime
import math

from PyQt5.QtCore import pyqtSignal, QPoint, QSize, Qt
from PyQt5.QtOpenGL import QGLWidget
from PyQt5.QtGui import QPixmap, QColor
from OpenGL.GL import glCallList, glClear, glColorMaterial, glEnable,  glEndList,  glFrontFace, glGenLists, glGetIntegerv, glHint, glLightfv, glLoadIdentity, glMatrixMode, glNewList, glOrtho, glPopMatrix, glPushMatrix, glRenderMode, glRotated, glSelectBuffer, glShadeModel, glTranslated, glViewport,  glScaled,  glVertex3d, glBegin, glEnd
from OpenGL.GL import  GL_AMBIENT, GL_QUADS, GL_AMBIENT_AND_DIFFUSE, GL_CCW, GL_COLOR_BUFFER_BIT, GL_COLOR_MATERIAL, GL_COMPILE, GL_CULL_FACE, GL_DEPTH_BUFFER_BIT, GL_DEPTH_TEST, GL_FRONT, GL_LIGHT0, GL_LIGHTING, GL_MODELVIEW, GL_NICEST, GL_PERSPECTIVE_CORRECTION_HINT, GL_POSITION, GL_PROJECTION, GL_RENDER, GL_SELECT, GL_SMOOTH, GL_STENCIL_BUFFER_BIT, GL_TEXTURE_2D, GL_VIEWPORT,  GL_FLAT
from OpenGL.GLU import gluPerspective, gluPickMatrix

from libglparchis import Color, Casilla, Ficha, Jugador, Tablero, Dado, Coord3D
from libglparchistypes import TNames
from frmShowCasilla import frmShowCasilla
from frmShowFicha import frmShowFicha



class myQGLWidget(QGLWidget):
    def __init__(self, parent):
        QGLWidget.__init__(self, parent)

    def load_textures(self):
        """
            Load textures function to be reused in several QGLWidget
            
            I couldn't do it in a class due to it needed QGLWidget and I got Crashes
        """
        texNumeros=[]
        texDecor=[]
        texNumeros.append(self.bindTexture(QPixmap(':/glparchis/0.png')))
        texNumeros.append(self.bindTexture(QPixmap(':/glparchis/1.png')))
        texNumeros.append(self.bindTexture(QPixmap(':/glparchis/2.png')))
        texNumeros.append(self.bindTexture(QPixmap(':/glparchis/3.png')))
        texNumeros.append(self.bindTexture(QPixmap(':/glparchis/4.png')))
        texNumeros.append(self.bindTexture(QPixmap(':/glparchis/5.png')))
        texNumeros.append(self.bindTexture(QPixmap(':/glparchis/6.png')))
        texNumeros.append(self.bindTexture(QPixmap(':/glparchis/7.png')))
        texNumeros.append(self.bindTexture(QPixmap(':/glparchis/8.png')))
        texNumeros.append(self.bindTexture(QPixmap(':/glparchis/9.png')))
        
        texDecor.append(self.bindTexture(QPixmap(':/glparchis/casillainicial.png')))
        texDecor.append(self.bindTexture(QPixmap(':/glparchis/transwood.png')))
        texDecor.append(self.bindTexture(QPixmap(':/glparchis/seguro.png')))
        texDecor.append(self.bindTexture(QPixmap(':/glparchis/dado_desplegado.png')))
        return texNumeros, texDecor

    def texture(self, ttexture):
        """
            Auxiliar function to be reused in several objects
        """
        if ttexture>=0 and ttexture<1000:
            return self.texNumeros[ttexture]
        elif ttexture>=1000 and ttexture<=2000:
            return self.texDecor[ttexture-1000]

    def initializeGL(self):
            print ("initializeGL")
            self.texNumeros, self.texDecor=self.load_textures()
            glEnable(GL_TEXTURE_2D);
            glShadeModel (GL_SMOOTH);
            glEnable(GL_DEPTH_TEST)
            glEnable(GL_CULL_FACE)
            
            glFrontFace(GL_CCW);

            light_ambient =  [0.3, 0.3, 0.3, 0.1];

            glEnable(GL_LIGHTING)
            lightpos=(0, 0, 50)
            glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)  
            glLightfv(GL_LIGHT0, GL_POSITION, lightpos)  
            glEnable(GL_LIGHT0);
            glEnable(GL_COLOR_MATERIAL);
            glColorMaterial(GL_FRONT,GL_AMBIENT_AND_DIFFUSE);

            glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST);

    def resizeGL(self, width, height):    
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        aspect=width/height
        gluPerspective(60.0, aspect, 1, 400)
        glMatrixMode(GL_MODELVIEW)
    
    

class ObjectRotationManager:
    """
        Allows a basic rotation system in the subclass QGLWidget
        
        In the subclass is mandatory to add as class parameters:
        
        xRotationChanged=pyqtSignal(int)
        yRotationChanged=pyqtSignal(int)
        zRotationChanged=pyqtSignal(int)

    """
    def __init__(self):
        self.xRot = 0
        self.yRot = 0
        self.zRot = 0

        self.lastPos = QPoint()

    def normalizeAngle(self, angle):
        while angle < 0:
            angle += 360 * 16
        while angle > 360 * 16:
            angle -= 360 * 16
        return angle

    def xRotation(self):
        return self.xRot

    def yRotation(self):
        return self.yRot

    def zRotation(self):
        return self.zRot
        
        
    def mousePressEvent(self, event):
        self.lastPos = QPoint(event.pos())

    def mouseMoveEvent(self, event):
        dx = event.x() - self.lastPos.x()
        dy = event.y() - self.lastPos.y()

        if event.buttons() & Qt.LeftButton:
            self.setXRotation(self.xRot + 8 * dy)
            self.setYRotation(self.yRot + 8 * dx)
        elif event.buttons() & Qt.RightButton:
            self.setXRotation(self.xRot + 8 * dy)
            self.setZRotation(self.zRot + 8 * dx)

        self.lastPos = QPoint(event.pos())
        
        
    def setXRotation(self, angle):
        angle = self.normalizeAngle(angle)
        if angle != self.xRot:
            self.xRot = angle
            self.xRotationChanged.emit(angle)
            self.updateGL()

    def setYRotation(self, angle):
        angle = self.normalizeAngle(angle)
        if angle != self.yRot:
            self.yRot = angle
            self.yRotationChanged.emit(angle)
            self.updateGL()

    def setZRotation(self, angle):
        angle = self.normalizeAngle(angle)
        if angle != self.zRot:
            self.zRot = angle
            self.zRotationChanged.emit(angle)
            self.updateGL()

        

class DisplayList:
    tablero=1
    
    def numero():
        return 1

class wdgOGL(myQGLWidget):
    """Clase principal del Juego, aqui esta fundamentalmente la representacion.
   Emite click ficha cuando se realiza"""
    fichaClicked=pyqtSignal()
    doubleClicked=pyqtSignal()
    def __init__(self,  parent=None):
        myQGLWidget.__init__(self, parent)
        self.tablero=None#After assign_mem creation
        self.texNumeros=[]
        self.texDecor=[]
        self.rotX=0
        self.rotY=0
        self.rotZ=0
        self.z=None
        self.rotCenter=0
        
        self.rotatecenter=0#Si es 1 rota en sentido agujas del reloj desde el centro del tablero, si -1 al reves, si 0 no rota desde el centro
        
    def assign_mem(self, mem):
        self.mem=mem
        
        if self.mem.frmMain.isFullScreen():
            fs="FS"
        else:
            fs=""
        if self.mem.maxplayers==8:
            self.z=int(self.mem.settings.value("wdgOGL/z_{}{}".format(fs, self.mem.maxplayers), -85))
        elif self.mem.maxplayers==4:
            self.z=int(self.mem.settings.value("wdgOGL/z_{}{}".format(fs, self.mem.maxplayers), -60))
        elif self.mem.maxplayers==6:
            self.z=int(self.mem.settings.value("wdgOGL/z_{}{}".format(fs, self.mem.maxplayers), -80))
            
        self.tablero=Tablero(mem.maxplayers)
        print("DisplayLists")
        #Como vamos a usar varias lists tenemos que crear una base y luego el orden
        self.displaylists=glGenLists(DisplayList.numero())
        #Tablero
        glNewList(DisplayList.tablero, GL_COMPILE)
        self.tablero.draw(self)
        for c in self.mem.casillas.arr:
            if c.id!=0:
                c.draw(self)
        glEndList()
        




    def paintGL(self):   
        inicio=datetime.datetime.now()
        glLoadIdentity()
        self.qglClearColor(QColor())
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT| GL_STENCIL_BUFFER_BIT)
        if self.mem.maxplayers==8:
            glTranslated(-31.5, -17, self.z)
        elif self.mem.maxplayers==4:
            glTranslated(-31.5, -31.5, self.z)
        elif self.mem.maxplayers==6:
            glTranslated(-31.5, -24, self.z)
            
        if self.rotatecenter==1:
            #Para rotar desde elcentro, hay que llevar el centro al origen
            if self.mem.maxplayers==4:
                glTranslated(31.5, 31.5, 0)
                glRotated(self.rotCenter, 0, 0, 1)
                glTranslated(-31.5, -31.5, 0)
            elif self.mem.maxplayers==6:
                glTranslated(31.5, 24,  0)
                glRotated(self.rotCenter, 0, 0, 1)
                glTranslated(-31.5, -24,  0)
            elif self.mem.maxplayers==8:
                glTranslated(31.5, 17,  0)
                glRotated(self.rotCenter, 0, 0, 1)
                glTranslated(-31.5, -17, 0)
        glRotated(self.rotX, 1,0 , 0)
        glRotated(self.rotY, 0,1 , 0)
        glRotated(self.rotZ, 0,0 , 1)
                
        glCallList(DisplayList.tablero)
        
        for c in self.mem.casillas.arr:
            if c.id!=0:
                c.draw_fichas(self)#Need to draw through Squares to get square position
        self.mem.dado.draw(self)
            
        print("paintGL", datetime.datetime.now()-inicio)


    def keyPressEvent(self, event):
        def save_z():
            if self.mem.frmMain.isFullScreen():
                fs="FS"
            else:
                fs=""
            self.mem.settings.setValue("wdgOGL/z_{}{}".format(fs, self.mem.maxplayers), self.z)
            print(self.z)
            ###########################
        self.rotatecenter=0
        if event.key() == Qt.Key_Plus:
            self.z=self.z+1
            save_z()
        if event.key() == Qt.Key_Minus:
            self.z=self.z-1
            save_z()
        if event.key() == Qt.Key_X: # toggle mode
            self.rotX=self.rotX+5
        if event.key() == Qt.Key_Y: # toggle mode
            self.rotY=self.rotY+5
        if event.key() == Qt.Key_Z: # toggle mode
            self.rotZ=self.rotZ+5
        if event.key() == Qt.Key_Space: # toggle mode
            self.rotX=0
            self.rotY=0
            self.rotZ=0
        if event.key() == Qt.Key_M: # toggle mode
            self.rotatecenter=1
            self.rotCenter=self.rotCenter+5
        self.updateGL()
    
    def mouseDoubleClickEvent(self, event):
        self.doubleClicked.emit()

    def mousePressEvent(self, event):        
        def pickup(event, right):
            """
                Function to get the Name Stack
                right es si el boton pulsado es el derecho
                
                El viewport[3]-event.y() creo que es porque la medida de las Y está invertida
                Los problemas que tenía con windows de tener que hacer varios click se corrigieron sustituyendo la región de selección de 1,1 a 5,5

            """

            viewport=glGetIntegerv(GL_VIEWPORT);
            glMatrixMode(GL_PROJECTION);
            glPushMatrix();
            glSelectBuffer(512);
            glRenderMode(GL_SELECT);
            glLoadIdentity();
            gluPickMatrix(event.x(),viewport[3] -event.y(),5,5, viewport)
            aspect=viewport[2]/viewport[3]
            gluPerspective(60,aspect,1.0,400)
            glMatrixMode(GL_MODELVIEW)
            self.paintGL()
            glMatrixMode(GL_PROJECTION);
            if right==False:
                parseLeftButtonNameStack(glRenderMode(GL_RENDER))
            else:
                parseRightButtonNameStack(glRenderMode(GL_RENDER))
            glPopMatrix();
            glMatrixMode(GL_MODELVIEW); 

        def getObjectByName(id_name):
            """Devuelve un objeto dependiendo del nombre.None si no corresponde
            #Nuevo nombrado fichas 0-31, 32,tablero,33 dado,34- Casillas"""
            if id_name>=0 and id_name<=31:
                return self.mem.pawnsgame.getById(id_name)
            elif id_name==TNames.Board:
                return self.tablero
            elif id_name==TNames.Dice:
                return self.mem.dado
            elif id_name>=34 and id_name<=34+self.mem.casillas.number:
                return self.mem.casillas.find_by_id(id_name-34)
            else:
                return None
                
        def parseLeftButtonNameStack(nameStack):
            """
                nameStack tiene la estructura minDepth, maxDepth, names
            
                Objetos is an int array with the int names of the selected objects.
            """
            objetos=[]
            for minDepth, maxDepth, names in nameStack:
                if len(names)==1:
                    objetos.append(names[0])
            
            print("LEFT", objetos)
            if len(objetos)==1:#Casilla selector
                self.mem.selFicha=None
            elif len(objetos)==2:#Ficha Selector
                objeto=getObjectByName(objetos[1])
                if isinstance(objeto, Ficha):
                    self.mem.selFicha=objeto
                else:
                    self.mem.selFicha=None
                    print(self.tr("I made click to get a Piece but it wasn't one"))

        def parseRightButtonNameStack(nameStack):
            """nameStack tiene la estructura minDepth, maxDepth, names"""
            ############################333
            objetos=[]
            for minDepth, maxDepth, names in nameStack:
                if len(names)==1:
                   objetos.append(names[0])
            print("RIGHT", objetos)
            if len(objetos)==1:
                selCasilla=getObjectByName(objetos[0])
                if isinstance(selCasilla, Casilla):
                    frmshow=frmShowCasilla(self,  Qt.Popup,  selCasilla)
                    frmshow.move(self.mapToGlobal(placePopUp(frmshow)))
                    frmshow.show()
            elif len(objetos)==2:
                selFicha=getObjectByName(objetos[1])
                if isinstance(selFicha, Ficha):
                    frmshow=frmShowFicha(self,  Qt.Popup,  selFicha, self.mem)
                    frmshow. move(self.mapToGlobal(placePopUp(frmshow)))
                    frmshow.show()
                    
        def placePopUp(frmshow):
            """
                Sets the place of the popup in the windows to avoid getout of the screen
                frmshow can be a frmShowCasilla or a frmShowFicha
            """
            resultado=QPoint(event.x(), event.y())
            if event.x()>self.width()-frmshow.width():
                resultado.setX(event.x()-frmshow.width())
            if event.y()>self.height()-frmshow.height():
                resultado.setY(event.y()-frmshow.height())
            return resultado

                
        #########################################
        self.setFocus()
        if event.buttons() & Qt.LeftButton:
            print("Hola")
            pickup(event, False)            
            if self.mem.selFicha!=None:
                self.mem.jugadores.actual.log(self.tr("Se ha hecho click en la ficha {0}".format(self.mem.selFicha.id)))
                self.fichaClicked.emit()
        elif event.buttons() & Qt.RightButton:
            pickup(event, True)                    
        self.updateGL()


class wdgQT(QGLWidget, ObjectRotationManager):
    """
        Qt example class
    """
    xRotationChanged=pyqtSignal(int)
    yRotationChanged=pyqtSignal(int)
    zRotationChanged=pyqtSignal(int)
    def __init__(self, parent=None):
        QGLWidget.__init__(self, parent)
        ObjectRotationManager.__init__(self)
        self.object = 0

        self.trolltechGreen = QColor.fromCmykF(0.40, 0.0, 1.0, 0.0)
        self.trolltechPurple = QColor.fromCmykF(0.39, 0.39, 0.0, 0.0)


    def minimumSizeHint(self):
        return QSize(50, 50)

    def sizeHint(self):
        return QSize(400, 400)

    def initializeGL(self):
        print("WDGQT_initialize")
        self.qglClearColor(self.trolltechPurple.darker())
        self.object = self.makeObject()
        glShadeModel(GL_FLAT)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_CULL_FACE)

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslated(0.0, 0.0, -10.0)
        glRotated(self.xRot / 16.0, 1.0, 0.0, 0.0)
        glRotated(self.yRot / 16.0, 0.0, 1.0, 0.0)
        glRotated(self.zRot / 16.0, 0.0, 0.0, 1.0)
        glCallList(self.object)

    def resizeGL(self, width, height):
        side = min(width, height)
        glViewport(int((width - side) / 2.0), int((height - side) / 2.0), side, side)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-0.5, +0.5, +0.5, -0.5, 4.0, 15.0)
        glMatrixMode(GL_MODELVIEW)


    def makeObject(self):
        genList = glGenLists(1)
        glNewList(genList, GL_COMPILE)

        glBegin(GL_QUADS)

        x1 = +0.06
        y1 = -0.14
        x2 = +0.14
        y2 = -0.06
        x3 = +0.08
        y3 = +0.00
        x4 = +0.30
        y4 = +0.22

        self.quad(x1, y1, x2, y2, y2, x2, y1, x1)
        self.quad(x3, y3, x4, y4, y4, x4, y3, x3)

        self.extrude(x1, y1, x2, y2)
        self.extrude(x2, y2, y2, x2)
        self.extrude(y2, x2, y1, x1)
        self.extrude(y1, x1, x1, y1)
        self.extrude(x3, y3, x4, y4)
        self.extrude(x4, y4, y4, x4)
        self.extrude(y4, x4, y3, x3)

        Pi = 3.14159265358979323846
        NumSectors = 200

        for i in range(NumSectors):
            angle1 = (i * 2 * Pi) / NumSectors
            x5 = 0.30 * math.sin(angle1)
            y5 = 0.30 * math.cos(angle1)
            x6 = 0.20 * math.sin(angle1)
            y6 = 0.20 * math.cos(angle1)

            angle2 = ((i + 1) * 2 * Pi) / NumSectors
            x7 = 0.20 * math.sin(angle2)
            y7 = 0.20 * math.cos(angle2)
            x8 = 0.30 * math.sin(angle2)
            y8 = 0.30 * math.cos(angle2)

            self.quad(x5, y5, x6, y6, x7, y7, x8, y8)

            self.extrude(x6, y6, x7, y7)
            self.extrude(x8, y8, x5, y5)

        glEnd()
        glEndList()

        return genList

    def quad(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.qglColor(self.trolltechGreen)

        glVertex3d(x1, y1, -0.05)
        glVertex3d(x2, y2, -0.05)
        glVertex3d(x3, y3, -0.05)
        glVertex3d(x4, y4, -0.05)

        glVertex3d(x4, y4, +0.05)
        glVertex3d(x3, y3, +0.05)
        glVertex3d(x2, y2, +0.05)
        glVertex3d(x1, y1, +0.05)

    def extrude(self, x1, y1, x2, y2):
        self.qglColor(self.trolltechGreen.darker(250 + int(100 * x1)))

        glVertex3d(x1, y1, +0.05)
        glVertex3d(x2, y2, +0.05)
        glVertex3d(x2, y2, -0.05)
        glVertex3d(x1, y1, -0.05)

class wdgShowObject(myQGLWidget, ObjectRotationManager):
    """
        This class shows different objects in a Widget
    """
    xRotationChanged=pyqtSignal(int)
    yRotationChanged=pyqtSignal(int)
    zRotationChanged=pyqtSignal(int)
    def __init__(self, parent):
        myQGLWidget.__init__(self,  parent)
        ObjectRotationManager.__init__(self)
        self.objeto=0
               
        #Carga el primer objeto    
        self.cas= Casilla(1, 2, Color(0, 0, 255) , (-3.5, -1.5, 0, 0), 0, False, False, 3,  False, (0, 0, 0), False)
        self.casinicio= Casilla(1, 2, Color(255, 0, 0) , (-3.5, -1.5, 0, 0), 0, False, False, 0,  False, (0, 0, 0), False)
        self.ficha=Ficha(None, 0, 1, Color(255, 0, 0), Jugador(None, Color(255, 0, 0)), None)
        self.tablero=Tablero(4)
        self.tablero.position=Coord3D(0, 0, 0)
        self.tablero6=Tablero(6)
        self.tablero6.position=Coord3D(0, 0, 0)
        self.tablero8=Tablero(8)
        self.tablero8.position=Coord3D(0, 0, 0)
        self.dado=Dado()
        self.dado.showing=True
        self.lasttirada=5
        self.z=-10

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Plus:
            self.z=self.z+1
        if event.key() == Qt.Key_Minus:
            self.z=self.z-1
        if event.key() == Qt.Key_X: # toggle mode
            self.xRot=self.xRot+5
        if event.key() == Qt.Key_Y: # toggle mode
            self.yRot=self.yRot+5
        if event.key() == Qt.Key_Z: # toggle mode
            self.zRot=self.zRot+5
        if event.key() == Qt.Key_Space: # toggle mode
            self.xRot=0
            self.yRot=0
            self.zRot=0
        self.updateGL()

    def initializeGL(self): 
        """
            Initialize Opengl for QGLWidget
        """
        self.qglClearColor(QColor(206, 224, 255)) #Sets background color
        myQGLWidget.initializeGL(self)

        
    def showObject(self, obj):
        self.objeto=obj
        print ("Visualizando el objeto: " + str(self.objeto))
        self.paintGL()
        self.updateGL()

    def paintGL(self):  
        glLoadIdentity()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT| GL_STENCIL_BUFFER_BIT)
        glTranslated(0.0, 0.0, self.z)
        glRotated(self.xRot / 16.0, 1.0, 0.0, 0.0)
        glRotated(self.yRot / 16.0, 0.0, 1.0, 0.0)
        glRotated(self.zRot / 16.0, 0.0, 0.0, 1.0)
        if self.objeto==0:
            glScaled(0.1, 0.1,0.1)
            print("Aqui")
            self.tablero.draw(self)
            print("Aqui")
        elif self.objeto==1:
            glScaled(0.1, 0.1,0.1)
            self.tablero6.draw(self)
        elif self.objeto==2:
            glScaled(0.1, 0.1,0.1)
            self.tablero8.draw(self)
        elif self.objeto==3:
            glScaled(1.5, 1.5,1.5)
            self.dado.draw_alone(self)
        elif self.objeto==4:
            glScaled(1.5, 1.5,1.5)
            self.cas.draw(self)
        elif self.objeto==5:
            glScaled(0.4, 0.4,0.4)
            self.casinicio.draw(self)
        elif self.objeto==6:
            glScaled(2, 2,2)
            self.ficha.draw(self, None)

