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
    cylinderSource.SetHeight(1.0)
    cylinderSource.SetResolution(500)
    
    # Create a mapper and actor
    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(cylinderSource.GetOutputPort())
    actor = vtkActor()
    #actor.GetProperty().SetColor(colors.GetColor3d('Cornsilk'))
    actor.GetProperty().SetColor(colors.GetColor3d('LightGreen'))
    actor.SetMapper(mapper)

    # Create a renderer, render window, and interactor
    renderer = vtkRenderer()
    renderWindow = vtkRenderWindow()
    renderWindow.SetWindowName('Cylinder')
    renderWindow.AddRenderer(renderer)
    renderWindowInteractor = vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)

    # Add the actors to the scene
    renderer.AddActor(actor)
    renderer.SetBackground(colors.GetColor3d('DarkBlue'))

    # Render and interact
    renderWindow.Render()
    renderWindowInteractor.Start()

if __name__ == '__main__':
    main()