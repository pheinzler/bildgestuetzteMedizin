#!/usr/bin/env python
# -*- coding: utf-8 -*-

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersSources import vtkCylinderSource
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    colors = vtkNamedColors()

    # Create a sphere
    cylinderSource = vtkCylinderSource()
    cylinderSource.SetCenter(0.0, 0.0, 0.0)
    cylinderSource.SetRadius(0.5)
    cylinderSource.SetHeight(10)
    cylinderSource.SetResolution(500)
    
    # Create a mapper and actor
    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(cylinderSource.GetOutputPort())
    actor = vtkActor()
    #actor.GetProperty().SetColor(colors.GetColor3d('Cornsilk'))
    actor.GetProperty().SetColor(colors.GetColor3d('LightGreen'))
    actor.SetMapper(mapper)
    actor.RotateX(45.0)

    # Create second sphere
    cylinderSource2 = vtkCylinderSource()
    #cylinderSource2.SetCenter(cylinderSource.GetRadius() + 2.0, 0.0, 0.0)
    cylinderSource2.SetCenter(0.0, 0.0, 0.0)
    cylinderSource2.SetRadius(0.5)
    cylinderSource2.SetHeight(10)
    cylinderSource2.SetResolution(500)

    # Create second mapper and actor
    mapper2 = vtkPolyDataMapper()
    mapper2.SetInputConnection(cylinderSource2.GetOutputPort())
    actor2 = vtkActor()
    actor2.GetProperty().SetColor(colors.GetColor3d('DarkGreen'))
    actor2.SetMapper(mapper2)
    actor2.RotateY(45.0)

    # Create a renderer, render window, and interactor
    renderer = vtkRenderer()
    renderWindow = vtkRenderWindow()
    renderWindow.SetWindowName('Cylinder')
    renderWindow.AddRenderer(renderer)
    renderWindowInteractor = vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)

    # Add the actors to the scene
    renderer.AddActor(actor)
    renderer.AddActor(actor2)
    renderer.SetBackground(colors.GetColor3d('DarkBlue'))

    # Render and interact
    renderWindow.Render()
    renderWindowInteractor.Start()

if __name__ == '__main__':
    main()