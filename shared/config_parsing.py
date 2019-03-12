# -*- coding: utf-8 -*-
"""
/***************************************************************************
 BioDispersal
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


from . import utils

import xml.etree.ElementTree as ET

# config_models = None
config_parsers = None

# def setConfigModels(model_dict):
    # global config_models
    # config_models = model_dict
def setConfigParsers(parsers):
    global config_parsers
    config_parsers = parsers

def getParserByName(name):
    for parser in config_parsers:
        if parser.parser_name == name:
            return parser
    utils.internal_error("No parser named " + str(name))

# def parseConfig(config_file):
    # utils.info("Parsing configuration from file '" + str(config_file) + "'")
    # tree = ET.parse(config_file)
    # root = tree.getroot()
    # for model in root:
        # parseModel(model)
    # utils.info("Configuration parsing successful")
def parseConfig(config_file):
    utils.info("Parsing configuration from file '" + str(config_file) + "'")
    tree = ET.parse(config_file)
    root = tree.getroot()
    for parser in root:
        parseModel(parser)
    utils.info("Configuration parsing successful")

# Parse model from XML root.
# Updates models stored in 'config_models'.
# def parseModel(model_root):
    # global config_models, mk_item
    # model_tag = model_root.tag
    # utils.debug("parseModel " + str(model_tag))
    # utils.debug("config_models " + str(config_models))
    # if model_tag not in config_models:
        # utils.user_error("Unknown Model '" + model_tag + "'")
    # model = config_models[model_tag]
    # try:
        # utils.debug("cas 1")
        # utils.debug("config_models " + str(config_models))
        # model.fromXMLRoot(model_root)
        # return model
    # except AttributeError:
        # utils.debug("cas 2")
        # model.fromXMLAttribs(root.attrib)
        # for item in model_root:
            # utils.debug("iter")
            # dict = item.attrib
            # fields = dict.keys()
            # item = model.mkItemFromDict(dict)
            # model.addItem(item)
        # model.layoutChanged.emit()
        # return model
# Parse model from XML root.
# Updates parsers stored in 'config_parsers'.
def parseModel(parser_root):
    global config_parsers, mk_item
    parser_tag = parser_root.tag
    utils.debug("parse " + str(parser_tag))
    utils.debug("config_parsers " + str(config_parsers))
    parser = getParserByName(parser_tag)
    utils.debug("cas 1")
    utils.debug("config_parsers " + str(config_parsers))
    parser.fromXMLRoot(parser_root)
        