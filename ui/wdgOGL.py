 
from PyQt5.QtCore import *
from PyQt5.QtOpenGL import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from OpenGL.GL import *
from OpenGL.GLU import *
from libglparchis import *
from frmShowCasilla import *
from frmShowFicha import *

class DisplayList:
    tablero=1
    
    def numero():
        return 1

class wdgOGL(QGLWidget):
    """Clase principal del Juego, aqui esta fundamentalmente la representacion.
   Emite click ficha cuando se realiza"""
    fichaClicked=pyqtSignal()
    doubleClicked=pyqtSignal()
    def __init__(self,  parent=None,  filename=None):
        QGLWidget.__init__(self, parent)
        self.tablero=None#After assign_mem creation
        self.texNumeros=[]
        self.texDecor=[]
        self.rotX=0
        self.rotY=0
        self.rotZ=0
        self.rotCenter=0
        self.lock=False
        
        self.rotatecenter=0#Si es 1 rota en sentido agujas del reloj desde el centro del tablero, si -1 al reves, si 0 no rota desde el centro
        
    def assign_mem(self, mem):
        self.mem=mem
        self.tablero=Tablero(mem.maxplayers)
        print("DisplayLists")
        #Como vamos a usar varias lists tenemos que crear una base y luego el orden
        self.displaylists=glGenLists(DisplayList.numero())
        #Tablero
        glNewList(DisplayList.tablero, GL_COMPILE)
        self.tablero.dibujar(self)
        for c in self.mem.casillas.arr:
            if c.id!=0:
                c.dibujar(self)
        glEndList()
        
    def initializeGL(self):
        #LAS TEXTURAS SE DEBEN CRAR AQUÍ ES LO PRIMERO QUE SE EJECUTA
        self.texNumeros.append(self.bindTexture(QtGui.QPixmap(':/glparchis/0.png')))
        self.texNumeros.append(self.bindTexture(QtGui.QPixmap(':/glparchis/1.png')))
        self.texNumeros.append(self.bindTexture(QtGui.QPixmap(':/glparchis/2.png')))
        self.texNumeros.append(self.bindTexture(QtGui.QPixmap(':/glparchis/3.png')))
        self.texNumeros.append(self.bindTexture(QtGui.QPixmap(':/glparchis/4.png')))
        self.texNumeros.append(self.bindTexture(QtGui.QPixmap(':/glparchis/5.png')))
        self.texNumeros.append(self.bindTexture(QtGui.QPixmap(':/glparchis/6.png')))
        self.texNumeros.append(self.bindTexture(QtGui.QPixmap(':/glparchis/7.png')))
        self.texNumeros.append(self.bindTexture(QtGui.QPixmap(':/glparchis/8.png')))
        self.texNumeros.append(self.bindTexture(QtGui.QPixmap(':/glparchis/9.png')))
        
        self.texDecor.append(self.bindTexture(QtGui.QPixmap(':/glparchis/casillainicial.png')))
        self.texDecor.append(self.bindTexture(QtGui.QPixmap(':/glparchis/transwood.png')))
        self.texDecor.append(self.bindTexture(QtGui.QPixmap(':/glparchis/seguro.png')))
        self.texDecor.append(self.bindTexture(QtGui.QPixmap(':/glparchis/dado_desplegado.png')))
        
        print ("initializeGL")
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
        

    def paintGL(self):   
        inicio=datetime.datetime.now()
        glLoadIdentity()
        self.qglClearColor(QColor())

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT| GL_STENCIL_BUFFER_BIT)
        if self.mem.maxplayers==8:
            glTranslated(-31.5, -17,  -85)
        elif self.mem.maxplayers==4:
            glTranslated(-31.5, -31.5,  -60)
        elif self.mem.maxplayers==6:
            glTranslated(-31.5, -24,  -80)
            
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
                c.dibujar_fichas(self)
        self.mem.dado.dibujar(self)
            
        print("paintGL", datetime.datetime.now()-inicio)

    def resizeGL(self, width, height):
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        aspect=width/height
        gluPerspective(60.0, aspect, 1, 400)
        glMatrixMode(GL_MODELVIEW)

    def keyPressEvent(self, event):
        self.rotatecenter=0
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
        if self.lock==False:
            self.lock=True
            self.doubleClicked.emit()
            self.lock=False
        else:
            print ("Double click event ignored")

    def mousePressEvent(self, event):        
        def pickup(event, right):
            """right es si el boton pulsado en el derecho"""
            viewport=glGetIntegerv(GL_VIEWPORT);
            glMatrixMode(GL_PROJECTION);
            glPushMatrix();
            glSelectBuffer(512);
            glRenderMode(GL_SELECT);
            glLoadIdentity();
            gluPickMatrix(event.x(),viewport[3] -event.y(),1,1, viewport)
            aspect=viewport[2]/viewport[3]
            gluPerspective(60,aspect,1.0,400)
            glMatrixMode(GL_MODELVIEW)
            self.paintGL()
            glMatrixMode(GL_PROJECTION);
            if right==False:
                process(glRenderMode(GL_RENDER))
            else:
                processright(glRenderMode(GL_RENDER))
            glPopMatrix();
            glMatrixMode(GL_MODELVIEW);           
 
            
        def object(mem, id_name):
            """Devuelve un objeto dependiendo del nombre.None si no corresponde
            #Nuevo nombrado fichas 0-31, 32,tablero,33 dado,34- Casillas"""
            if id_name>=0 and id_name<=31: #fichas van de 0 a 15
                return mem.fichas(id_name)
            elif id_name==32:#tablero 16
                return self.tablero
            elif id_name==33:#casillas de 17 a 121
                return mem.dado
            elif id_name>=34 and id_name<=34+self.mem.casillas.number:#casillas de 17 a 121
                return mem.casillas.find_by_id(id_name-34)
            else:
                return None
                
        def process(nameStack):
            """nameStack tiene la estructura minDepth, maxDepth, names"""
            objetos=[]
            for minDepth, maxDepth, names in nameStack:
                if len(names)==1:
                    objetos.append(names[0])
            
            if len(objetos)==1:
                self.mem.selFicha=None
            elif len(objetos)==2:
                objeto=object(self.mem, objetos[1])
                if isinstance(objeto, Ficha):
                    self.mem.selFicha=objeto
                else:
                    self.mem.selFicha=None
                
                
        def processright(nameStack):
            """nameStack tiene la estructura minDepth, maxDepth, names"""
            def placePopUp():
                resultado=QPoint(event.x(), event.y())
                if event.x()>self.width()-a.width():
                    resultado.setX(event.x()-a.width())
                if event.y()>self.height()-a.height():
                    resultado.setY(event.y()-a.height())
                return resultado
            ############################333
            objetos=[]
            for minDepth, maxDepth, names in nameStack:
                if len(names)==1:
                   objetos.append(names[0])
            if len(objetos)==1:
                selCasilla=object(self.mem, objetos[0])
                if isinstance(selCasilla, Casilla):
                    a=frmShowCasilla(self,  Qt.Popup,  selCasilla)
                    a. move(self.mapToGlobal(placePopUp() ))
                    a.show()
            elif len(objetos)==2:
                selFicha=object(self.mem, objetos[1])
                if isinstance(selFicha, Ficha):
                    a=frmShowFicha(self,  Qt.Popup,  selFicha, self.mem)
                    a. move(self.mapToGlobal(placePopUp()))
                    a.show()
                
        #########################################
        self.setFocus()
        if event.buttons() & Qt.LeftButton:
            pickup(event, False)            
            if self.mem.selFicha!=None:
                self.mem.jugadores.actual.log(self.tr("Se ha hecho click en la ficha {0}".format(self.mem.selFicha.id)))
                self.fichaClicked.emit()
        elif event.buttons() & Qt.RightButton:
            pickup(event, True)                    
        self.updateGL()

