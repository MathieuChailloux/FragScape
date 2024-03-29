# -*- coding: utf-8 -*-
"""
/***************************************************************************
 FragScape
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

from qgis.core import (QgsCoordinateReferenceSystem,
                        QgsUnitTypes,
                        QgsProcessingUtils,
                        QgsMapLayerProxyModel)
from qgis.gui import QgsFileWidget
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QAbstractItemView, QHeaderView

from ..qgis_lib_mc import utils, qgsUtils, abstract_model

# FragScape global parameters

# ParamsModel from which parameters are retrieved
params = None

# Default CRS is set to epsg:2154 (France area, metric system)
defaultCrs = QgsCoordinateReferenceSystem("epsg:2154")
    
def mkTmpLayerPath(layer_name):
    if params is None:
        utils.warn.generateTempFilename("Parameter module not initialized")
        path = QgsProcessingUtils(layer_name)
    elif params.tmpDir is None:
        utils.warn("Output directories not initialized")
        path = QgsProcessingUtils.generateTempFilename(layer_name)
    elif params.save_tmp:
        path = utils.joinPath(params.tmpDir,layer_name)
    else:
        path = QgsProcessingUtils.generateTempFilename(layer_name)
    return path
        
        
class ParamsModel(abstract_model.NormalizingParamsModel):

    MODE = "mode"
    SAVE_TMP = "saveTmpFiles"
    
    VECTOR_MODE = 0
    RASTER_MODE = 1
    
    def __init__(self,fsModel):
        self.parser_name = "Params"
        self.fsModel = fsModel
        super().__init__()
        self.mode = self.VECTOR_MODE
        self.save_tmp = False
        #self.workspace = None
        self.outputDir = None
        self.tmpDir = None
        #self.resolution = 0.0
        #self.projectFile = ""
        #self.crs = defaultCrs
        #fields = [self.WORKSPACE,self.EXTENT_LAYER,
        #    self.RESOLUTION,self.PROJECT,self.CRS,self.MODE]
        # super().__init__(fields)
        abstract_model.NormalizingParamsModel.__init__(self,feedback=fsModel.feedback)
        
    def getNItem(self,n):
        items = [self.workspace,
                 self.extentLayer,
                 self.resolution,
                 self.projectFile,
                 self.crs.description(),
                 self.mode]
        return items[n]

    # Checks that all parameters are initialized
    def checkInit(self,check_res=True):
        self.checkWorkspaceInit()
        self.checkExtentInit()
        if check_res:
            self.checkResolutionInit()
        self.checkCrsInit()
    
    def setWorkspace(self,path):
        norm_path = super().setWorkspace(path)
        self.outputDir = utils.createSubdir(norm_path,"outputs")
        utils.info("Outputs directory set to '" + str(norm_path))
        self.tmpDir = utils.createSubdir(norm_path,"tmp")
        utils.info("Temporary directory set to '" + str(self.tmpDir))
        
    def setCrs(self,crs):
        excluded_units = [ QgsUnitTypes.DistanceDegrees,
            QgsUnitTypes.DistanceUnknownUnit ]
        if crs:
            unit = crs.mapUnits()
            if unit in excluded_units:
                utils.user_error("Unexpected projection system "
                    + str(crs) + ", please chose a metric system")
        super().setCrs(crs)
        
    def setSaveTmp(self,state):
        if state == 0:
            self.save_tmp = False
        elif state == 2:
            self.save_tmp = True
        else:
            utils.internal_error("Unexpected state for save_tmp checkbox : " + str(state))
        self.layoutChanged.emit()
        
    def setMode(self,mode):
        try:
            self.mode = int(mode)
        except ValueError:
            utils.user_error("Unexpected mode : " + str(mode))
        self.layoutChanged.emit()
        
    def modeIsVector(self):
        return (self.mode == self.VECTOR_MODE)
        
    def mkOutputFile(self,name):
        self.checkWorkspaceInit()
        new_path = utils.joinPath(self.outputDir,name)
        return new_path
       
    def fromXMLDict(self,dict):
        super().fromXMLDict(dict)
        if self.MODE in dict:
            self.setMode(dict[self.MODE])
        
    def toXML(self,indent=""):
        xmlStr = indent + "<" + self.parser_name
        xmlStr += super().getXMLStr()
        xmlStr += " " + self.MODE + "=\"" + str(self.mode) + "\""
        xmlStr += "/>"
        return xmlStr
        

class ParamsConnector:

    def __init__(self,dlg,paramsModel):
        self.parser_name = "Params"
        self.dlg = dlg
        self.model = paramsModel
        
    def initGui(self):
        self.dlg.paramsView.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.dlg.paramsCrs.setCrs(self.model.DEFAULT_CRS)
        
    def connectComponents(self):
        self.dlg.paramsView.setModel(self.model)
        self.dlg.paramsMode.currentIndexChanged.connect(self.switchMode)
        self.dlg.rasterResolution.valueChanged.connect(self.model.setResolution)
        self.dlg.extentLayer.fileChanged.connect(self.model.setExtentLayer)
        self.dlg.workspace.setStorageMode(QgsFileWidget.GetDirectory)
        self.dlg.workspace.fileChanged.connect(self.model.setWorkspace)
        self.dlg.paramsCrs.crsChanged.connect(self.model.setCrs)
        self.dlg.saveTmpResultsFlag.stateChanged.connect(self.model.setSaveTmp)
        # header
        header = self.dlg.paramsView.horizontalHeader()     
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        self.model.layoutChanged.emit()
        
    def tr(self, message):
        return QCoreApplication.translate('BioDispersal', message)
        
    def refreshProjectName(self):
        fname = self.model.projectFile
        basename = os.path.basename(fname)
        if basename:
            self.dlg.projectName.setText(self.tr("Projet BioDispersal : ") + basename)
        else:
            self.dlg.projectName.setText(self.tr("Pas de projet BioDispersal"))
            
    def setProjectFile(self,fname):
        self.model.projectFile = fname
        self.refreshProjectName()
        
    # Switch between vector and raster modes.
    # Widgets are updated (enable, filters, ...)
    def switchMode(self,mode):
        utils.debug("switchMode " + str(mode))
        vector_widgets = self.dlg.getVectorWidgets()
        raster_widgets = self.dlg.getRasterWidgets()
        layer_combos = [ self.dlg.resultsInputLayer]
        layer_combo_dlg = [self.dlg.landuseConnector.layerComboDlg,
            self.dlg.fragmConnector.layerComboDlg ]
        # layer_combo_dlg = [ ]
        if mode == self.model.VECTOR_MODE:
            for w in vector_widgets:
                w.setEnabled(True)
            for w in raster_widgets:
                w.setEnabled(False)
            for lc in layer_combos:
                lc.setFilters(QgsMapLayerProxyModel.VectorLayer)
            for lcd in layer_combo_dlg:
                lcd.setVectorMode()
        elif mode == self.model.RASTER_MODE:
            for w in vector_widgets:
                w.setEnabled(False)
            for w in raster_widgets:
                w.setEnabled(True)
            for lc in layer_combos:
                lc.setFilters(QgsMapLayerProxyModel.RasterLayer)
            for lcd in layer_combo_dlg:
                lcd.setBothMode()
        else:
            utils.internal_error("Unexpected mode : " + str(mode))
        self.dlg.landuseSelectionMode.setCurrentIndex(0)
        self.model.setMode(mode)
        
    def updateUI(self):
        self.dlg.workspace.setFilePath(self.model.workspace)
        self.dlg.paramsMode.setCurrentIndex(self.model.mode)
        self.dlg.paramsCrs.setCrs(self.model.crs)
        
    def updateFromXML(self,root,feedback=None):
        self.model.updateFromXML(root)
        self.updateUI()
        
