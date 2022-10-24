#!/usr/bin/python3
import sys
import vtk
import numpy as np
from PyQt5 import QtCore, QtWidgets
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor



class MainWindow(QtWidgets.QMainWindow):
     
    def __init__(self, parent = None):
        QtWidgets.QMainWindow.__init__(self, parent)
 
        self.frame = QtWidgets.QFrame()
    
        self.vsl = QtWidgets.QVBoxLayout()  #vertical slider layout
        self.vtkWidget = QVTKRenderWindowInteractor(self.frame)
        self.vsl.addWidget(self.vtkWidget)

        #slider hinzufuegen
        groupBox1 = QtWidgets.QGroupBox('Slider für rot')
        self.slider1, display1 = self.createSlider()

        groupBox2 = QtWidgets.QGroupBox('Slider für grün')
        self.slider2, display2 = self.createSlider()

        groupBox3 = QtWidgets.QGroupBox('Slider für blau')
        self.slider3, display3 = self.createSlider()
        
        groupBox4 = QtWidgets.QGroupBox('Choose cylinder')
        self.switch, display4 = self.createSwitch()
        
        #renderer    
        self.ren = vtk.vtkRenderer()
        self.vtkWidget.GetRenderWindow().AddRenderer(self.ren)
        self.iren = self.vtkWidget.GetRenderWindow().GetInteractor()
 
        #Zylinderobjekte erzeugem und höhe und breite setzen
        self.cylinder = vtk.vtkCylinderSource()
        self.cylinder.SetHeight(5)
        self.cylinder.SetRadius(1)
        self.colorCylinder = (0.6,0,0)

        self.cylinder1 = vtk.vtkCylinderSource()
        self.cylinder1.SetHeight(3)
        self.cylinder1.SetRadius(1)
        self.colorCylinder1 = (0,0.5,0)
        # mapper
        cylinderMapper = vtk.vtkPolyDataMapper()
        cylinderMapper.SetInputConnection(self.cylinder.GetOutputPort())

        cylinderMapper1 = vtk.vtkPolyDataMapper()
        cylinderMapper1.SetInputConnection(self.cylinder.GetOutputPort())
 
        #actor
        self.cylinderActor = vtk.vtkActor()
        self.cylinderActor.SetMapper(cylinderMapper)
        self.cylinderActor.GetProperty().SetColor(self.colorCylinder[0],self.colorCylinder[1],self.colorCylinder[2])#rgb
        self.cylinderActor.RotateX(45.0)

        rotx = np.array([1, 0, 0, 0, 0, np.cos(45), (-np.sin(45)), 0, 0, np.sin(45), np.cos(45), 0, 0, 0, 0, 1]).reshape(4,4)

        #self.transform = self.cylinder.vtkTransform()
        #self.cylinderActor.SetUserMatrix(rotx)


        self.cylinder1Actor = vtk.vtkActor()
        self.cylinder1Actor.SetMapper(cylinderMapper)
        self.cylinder1Actor.GetProperty().SetColor(self.colorCylinder1[0],self.colorCylinder1[1],self.colorCylinder1[2])#rgb
        self.cylinder1Actor.RotateY(90.0)
 
        self.ren.AddActor(self.cylinderActor)
        self.ren.AddActor(self.cylinder1Actor)
 
        self.ren.ResetCamera()
        self.ren.SetBackground(0,0,0)
        #layout und handler
        self.slider1.valueChanged.connect(display1.display)
        self.slider1.valueChanged.connect(self.handlerSlider)
        vbox1 = QtWidgets.QVBoxLayout()
        vbox1.addWidget(self.slider1)
        vbox1.addWidget(display1)
        groupBox1.setLayout(vbox1)
        self.vsl.addWidget(groupBox1)

        self.slider2.valueChanged.connect(display2.display)
        self.slider2.valueChanged.connect(self.handlerSlider)
        vbox2 = QtWidgets.QVBoxLayout()
        vbox2.addWidget(self.slider2)
        vbox2.addWidget(display2)
        groupBox2.setLayout(vbox2)
        self.vsl.addWidget(groupBox2)

        self.slider3.valueChanged.connect(display3.display)
        self.slider3.valueChanged.connect(self.handlerSlider)
        vbox3 = QtWidgets.QVBoxLayout()
        vbox3.addWidget(self.slider3)
        vbox3.addWidget(display3)
        groupBox3.setLayout(vbox3)
        self.vsl.addWidget(groupBox3)

        self.switch.valueChanged.connect(display4.display)
        self.switch.valueChanged.connect(self.handlerSwitch)
        vbox4 = QtWidgets.QVBoxLayout()
        vbox4.addWidget(self.switch)
        vbox4.addWidget(display4)
        groupBox4.setLayout(vbox4)
        self.vsl.addWidget(groupBox4)

        #frame setzen
        self.frame.setLayout(self.vsl)
        self.setCentralWidget(self.frame)        
        self.show()
        self.iren.Initialize()

    def createSlider(self):
        '''
            Slider und display, display zeigt ahtuellen wert des sliders an
        '''
        slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        slider.setFocusPolicy(QtCore.Qt.NoFocus)
        #slider.setTickPosition(QSlider.TicksBothSides)
        slider.setRange(0,255)
        slider.setValue(128)
        slider.setSingleStep(1)

        display = QtWidgets.QLCDNumber(3)
        display.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        display.display(128)

        return slider, display

    def createSwitch(self):
        '''
            Switch und display, display zeigt aktuell ausgewähltes Objekt an
        '''
        slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        slider.setFocusPolicy(QtCore.Qt.NoFocus)
        #slider.setTickPosition(QSlider.TicksBothSides)
        slider.setRange(0,1)
        slider.setValue(0)
        slider.setSingleStep(1)

        display = QtWidgets.QLCDNumber(3)
        display.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        display.display(0)

        return slider, display

    
    def handlerSlider(self, decide=0):
        if decide == 1:
            self.slider1.setValue(int(self.colorCylinder[0]*255))
            self.slider2.setValue(int(self.colorCylinder[1]*255))
            self.slider3.setValue(int(self.colorCylinder[2]*255))
            return
        elif decide == 2:
            self.slider1.setValue(int(self.colorCylinder1[0]))
            self.slider2.setValue(int(self.colorCylinder1[1]))
            self.slider3.setValue(int(self.colorCylinder1[2]))
        elif self.switch.value() == 0:
            value = [self.slider1.value(), self.slider2.value(), self.slider3.value()]
            self.cylinderActor.GetProperty().SetColor(value[0]/255, value[1]/255, value[2]/255)
            self.iren.ReInitialize()
        elif self.switch.value() == 1:
            value = [self.slider1.value(), self.slider2.value(), self.slider3.value()]
            self.cylinder1Actor.GetProperty().SetColor(value[0]/255, value[1]/255, value[2]/255)
            self.iren.ReInitialize()
        return
    
    def handlerSwitch(self):
        if self.switch.value() == 0:
            self.colorCylinder1 = (self.cylinderActor.GetProperty().GetColor())
            self.handlerSlider(decide=1)

        else:
            self.colorCylinder = (self.cylinderActor.GetProperty().GetColor())
            self.handlerSlider(2)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
 
    window = MainWindow()
    #window.show()
    sys.exit(app.exec_())