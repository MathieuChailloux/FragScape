# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Meff
                                 A QGIS plugin
 Computes ecological continuities based on environments permeability
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2018-04-12
        git sha              : $Format:%H$
        copyright            : (C) 2018 by IRSTEA
        email                : mathieu.chailloux@irstea.fr
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os.path
import pathlib

from qgis.core import QgsCoordinateReferenceSystem, QgsRectangle, QgsProject, QgsCoordinateTransform
from qgis.gui import QgsFileWidget
from PyQt5.QtCore import QVariant, QAbstractTableModel, QModelIndex, Qt
from PyQt5.QtWidgets import QAbstractItemView, QFileDialog, QHeaderView

from ..shared import utils, qgsUtils, qgsTreatments, abstract_model

# Meff global parameters

# ParamsModel from which parameters are retrieved
params = None

# Default CRS is set to epsg:2154 (France area, metric system)
defaultCrs = QgsCoordinateReferenceSystem("EPSG:2154")

# Checks that workspace is intialized and is an existing directory.
# def checkWorkspaceInit():
    # if not params.workspace:
        # utils.user_error("Workspace parameter not initialized")
    # if not os.path.isdir(params.workspace):
        # utils.user_error("Workspace directory '" + params.workspace + "' does not exist")
        
# Returns relative path w.r.t. workspace directory.
# File separator is set to common slash '/'.
# def normalizePath(path):
    # checkWorkspaceInit()
    # if not path:
        # utils.user_error("Empty path")
    # norm_path = utils.normPath(path)
    # if os.path.isabs(norm_path):
        # rel_path = os.path.relpath(norm_path,params.workspace)
    # else:
        # rel_path = norm_path
    # final_path = utils.normPath(rel_path)
    # return final_path
        
# Returns absolute path from normalized path (cf 'normalizePath' function)
# def getOrigPath(path):
    # checkWorkspaceInit()
    # if path == "":
        # utils.user_error("Empty path")
    # elif os.path.isabs(path):
        # return path
    # else:
        # return os.path.normpath(utils.joinPath(params.workspace,path))
    
# Checks that all parameters are initialized
# def checkInit():
    # checkWorkspaceInit()
    # if not params.territoryLayer:
        # utils.user_error("Territory layer parameter not initialized")
    # utils.checkFileExists(getOrigPath(params.territoryLayer),"Territory layer ")
    # if not params.crs:
        # utils.user_error("CRS parameter not initialized")
    # if not params.crs.isValid():
        # utils.user_error("Invalid CRS")

# Returns normalized path from QgsMapLayerComboBox
# def getPathFromLayerCombo(combo):
    # layer = combo.currentLayer()
    # layer_path = normalizePath(qgsUtils.pathOfLayer(layer))
    # return layer_path
        
# def getTerritoryLayer():
    # utils.debug("PARAMS clip flag = " + str(getDataClipFlag()))
    # if getDataClipFlag():
        # return getOrigPath(params.territoryLayer)
    # else:
        # return None
    
# def getDataClipFlag():
    # return params.dataClipFlag

# def mkOutputFile(name):
    # checkWorkspaceInit()
    # new_path = utils.joinPath(params.outputDir,name)
    # return new_path
        
#class ParamsModel(abstract_model.AbstractGroupModel):
class ParamsModel(QAbstractTableModel):

    WORKSPACE = "workspace"
    CLIP = "clip"
    TERRITORY = "territoryLayer"
    PROJECT = "projectFile"
    CRS = "crs"

    def __init__(self,fsModel):
        self.parser_name = "Params"
        self.fsModel = fsModel
        self.workspace = None
        self.outputDir = None
        self.territoryLayer = None
        self.dataClipFlag = True
        self.projectFile = ""
        self.crs = defaultCrs
        self.fields = [self.WORKSPACE,self.TERRITORY,self.PROJECT,self.CRS]
        QAbstractTableModel.__init__(self)
        
    """ Getters and setters """
    def setTerritoryLayer(self,path):
        path = self.normalizePath(path)
        utils.info("Setting territory layer to " + str(path))
        self.territoryLayer = path
        #self.layoutChanged.emit()
        
    def getTerritoryLayer(self):
        if self.dataClipFlag:
            return self.getOrigPath(self.territoryLayer)
        else:
            return None
        
    def setDataClipFalg(self,val):
        self.dataClipFlag = val
        
    def switchDataClipFlag(self):
        self.dataClipFlag = not self.dataClipFlag
        
    def setCrs(self,crs):
        utils.info("Setting extent CRS to " + crs.description())
        self.crs = crs
        self.layoutChanged.emit()
        
    def getCrsStr(self):
        return self.crs.authid().lower()

    def getTransformator(self,in_crs):
        transformator = QgsCoordinateTransform(in_crs,self.crs,QgsProject.instance())
        return transformator
    
    # def getBoundingBox(self,in_extent_rect,in_crs):
        # transformator = self.getTransformator(in_crs)
        # out_extent_rect = transformator.transformBoundingBox(in_extent_rect)
        # return out_extent_rect
        
    def setWorkspace(self,path):
        norm_path = utils.normPath(path)
        self.workspace = norm_path
        utils.info("Workspace directory set to '" + norm_path)
        if not os.path.isdir(norm_path):
            utils.user_error("Directory '" + norm_path + "' does not exist")
        self.outputDir = utils.createSubdir(norm_path,"outputs")
        
    """ Path/workspace utils """
    # Checks that workspace is intialized and is an existing directory.
    def checkWorkspaceInit(self):
        if not self.workspace:
            utils.user_error("Workspace parameter not initialized")
        if not os.path.isdir(self.workspace):
            utils.user_error("Workspace directory '" + self.workspace + "' does not exist")
            
    # Returns relative path w.r.t. workspace directory.
    # File separator is set to common slash '/'.
    def normalizePath(self,path):
        self.checkWorkspaceInit()
        if not path:
            utils.user_error("Empty path")
        norm_path = utils.normPath(path)
        if os.path.isabs(norm_path):
            rel_path = os.path.relpath(norm_path,self.workspace)
        else:
            rel_path = norm_path
        final_path = utils.normPath(rel_path)
        return final_path
            
    # Returns absolute path from normalized path (cf 'normalizePath' function)
    def getOrigPath(self,path):
        self.checkWorkspaceInit()
        if path == "":
            utils.user_error("Empty path")
        elif os.path.isabs(path):
            return path
        else:
            return os.path.normpath(utils.joinPath(self.workspace,path))
    
    def mkOutputFile(self,name):
        self.checkWorkspaceInit()
        new_path = utils.joinPath(self.outputDir,name)
        return new_path
        
    """ MVC functions """
    def rowCount(self,parent=QModelIndex()):
        return len(self.fields)
        
    def columnCount(self,parent=QModelIndex()):
        return 1
              
    def getNItem(self,n):
        items = [self.workspace,
                 self.territoryLayer,
                 self.projectFile,
                 self.crs.description(),
                 ""]
        return items[n]
            
    def data(self,index,role):
        if not index.isValid():
            return QVariant()
        row = index.row()
        item = self.getNItem(row)
        if role != Qt.DisplayRole:
            return QVariant()
        elif row < self.rowCount():
            return(QVariant(item))
        else:
            return QVariant()
            
    def flags(self, index):
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable
        
    def headerData(self,col,orientation,role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return QVariant("value")
        elif orientation == Qt.Vertical and role == Qt.DisplayRole:
            return QVariant(self.fields[col])
        return QVariant()
        
    """ XML """
    def fromXMLRoot(self,root):
        dict = root.attrib
        utils.debug("params dict = " + str(dict))
        return self.fromXMLDict(dict)

    def fromXMLDict(self,dict):
        if self.WORKSPACE in dict:
            if os.path.isdir(dict[self.WORKSPACE]):
                self.setWorkspace(dict[self.WORKSPACE])
        if self.TERRITORY in dict:
            self.setTerritoryLayer(dict[self.TERRITORY])
        if self.CLIP in dict:
            # Cast with bool() not working
            flag = dict[self.CLIP] == "True"
            self.dataClipFlag = flag
        #self.model.layoutChanged.emit()
        
    def toXML(self,indent=""):
        xmlStr = indent + "<" + self.parser_name
        if self.workspace:
            xmlStr += " " + self.WORKSPACE + "=\"" + str(self.workspace) + "\""
        xmlStr += " " + self.CLIP + "=\"" + str(self.dataClipFlag) + "\""
        if self.territoryLayer:
            xmlStr += " " + self.TERRITORY + "=\"" + str(self.territoryLayer) + "\""
        xmlStr += "/>"
        return xmlStr

class ParamsConnector:

    def __init__(self,dlg,paramsModel):
        self.parser_name = "Params"
        self.dlg = dlg
        self.model = paramsModel
        #self.model = ParamsModel()
        
    def initGui(self):
        self.dlg.paramsView.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.dlg.territoryLayer.setFilter(qgsUtils.getVectorFilters())
        self.dlg.paramsCrs.setCrs(defaultCrs)
        
    def connectComponents(self):
        self.dlg.paramsView.setModel(self.model)
        self.dlg.territoryLayer.setStorageMode(QgsFileWidget.GetFile)
        self.dlg.territoryLayer.fileChanged.connect(self.model.setTerritoryLayer)
        self.dlg.dataClipFlag.stateChanged.connect(self.model.switchDataClipFlag)
        self.dlg.workspace.setStorageMode(QgsFileWidget.GetDirectory)
        self.dlg.workspace.fileChanged.connect(self.model.setWorkspace)
        self.dlg.paramsCrs.crsChanged.connect(self.model.setCrs)
        header = self.dlg.paramsView.horizontalHeader()     
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        self.model.layoutChanged.emit()
        
    def updateUI(self):
        self.dlg.workspace.setFilePath(self.model.workspace)
        self.dlg.territoryLayer.setFilePath(self.model.territoryLayer)
        checkState = 2 if self.model.dataClipFlag else 0
        self.dlg.dataClipFlag.setCheckState(checkState)
        self.dlg.paramsCrs.setCrs(self.model.crs)

    def fromXMLRoot(self,root):
        self.model.fromXMLRoot(root)
        self.updateUI()

    # def fromXMLDict(self,dict):
        # self.model.fromXMLDict(dict)
        # checkState = 2 if self.model.dataClipFlag else 0
        # self.dlg.dataClipFlag.setCheckState(checkState)
        # self.model.layoutChanged.emit()
        # if "workspace" in dict:
            # if os.path.isdir(dict["workspace"]):
                # self.model.setWorkspace(dict["workspace"])
        # if "territoryLayer" in dict:
            # self.model.setTerritoryLayer(dict["territoryLayer"])
        # if "dataClipFlag" in dict:
            # flag = dict["dataClipFlag"] == "True"
            # if flag == True:
                # self.dlg.dataClipFlag.setCheckState(2)
            # else:
                # self.dlg.dataClipFlag.setCheckState(0)
        # self.model.layoutChanged.emit()

    def toXML(self,indent=""):
        return self.model.toXML(indent)
        # xmlStr = indent + "<" + self.parser_name
        # if self.model.workspace:
            # xmlStr += " " + ParamsModel.WORKSPACE + "=\"" + str(self.model.workspace) + "\""
        # xmlStr += " " + ParamsModel.CLIP + "=\"" + str(self.model.dataClipFlag) + "\""
        # if self.model.territoryLayer:
            # xmlStr += " " + ParamsModel.TERRITORY + "=\"" + str(self.model.territoryLayer) + "\""
        # xmlStr += "/>"
        # return xmlStr
        