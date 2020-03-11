
import os
from pathlib import Path
import sys
import math

import processing

from qgis.core import QgsProcessingFeedback

FS_NAME = 'FragScape'

FS_ALG_bname = 'meffRaster'
FS_CBC_ALG_bname = 'meffRasterCBC'

FS_ALG = FS_NAME + ":" + FS_ALG_bname
FS_CBC_ALG = FS_NAME + ":" + FS_CBC_ALG_bname

#script_path ='D:/Projets/Meff/Tests/Random/random_unit_tests.py'
#print("script_path = " + str(script_path))
#script_dir = os.path.dirname(script_path)
script_dir = 'C:/Users/mathieu.chailloux/AppData/Roaming/QGIS/QGIS3/profiles/default/python/plugins/FragScape/tests/Random'

rb_bname = "randomBase.tif"
rb0_bname = "randomBaseND0.tif"
rb1_bname = "randomBaseND1.tif"
rb2_bname = "randomBaseND2.tif"
report_bname = "cropLayer.gpkg"

rb_fname = os.path.join(script_dir,rb_bname)
rb0_fname = os.path.join(script_dir,rb0_bname)
rb1_fname = os.path.join(script_dir,rb1_bname)
rb2_fname = os.path.join(script_dir,rb2_bname)
report_fname = os.path.join(script_dir,report_bname)

debug_mode = False
debug_alg_mode = True
error_alg_mode = True

def info(msg):
    print(msg)
    
def debug(msg):
    if debug_mode:
        print("debug : " + msg)
        
def debugAlg(msg):
    if debug_alg_mode:
        print("debug : " + msg)
        
def errorAlg(msg):
    if error_alg_mode:
        print("debug : " + msg)

class BaseFeedback(QgsProcessingFeedback):
    
    def __init__(self):
        super().__init__()
        
    def pushCommandInfo(self,msg):
        debugAlg("commandInfo : " + str(msg))
        
    def pushConsoleInfo(self,msg):
        debugAlg("consoleInfo : " + str(msg))
        
    def pushDebugInfo(self,msg):
        debugAlg(msg)
        
    def pushInfo(self,msg):
        debugAlg(msg)
        
    def reportError(self,error,fatalError=False):
        errorAlg("reportError : " + str(error))
        if fatalError:
            raise Exception(error)
        
def getFSParams(fname,cls):
    return { 'INPUT' : fname,
        'CLASS' : cls,
        'OUTPUT' : 'memory:' }
    
def getFSCBCParams(fname,cls):
    return { 'INPUT' : fname,
        'CLASS' : cls,
        'REPORTING' : report_fname,
        'OUTPUT' : 'memory:'  }


nb_tests_ok = 0  
nb_tests_total = 0
tests_ko = []
    
def launchTest(alg_name,parameters,expected_res,test_name="NA"):
    global error_alg_mode, nb_tests_ok, nb_tests_total, tests_ko
    feedback = BaseFeedback()
    error_alg_mode = (expected_res != None)
    try:
        res = processing.run(alg_name,parameters,feedback=feedback)['OUTPUT_VAL']
    except Exception as e:
        debug(str(e))
        raise e
        res = None
    # TODO : fix * 100
    nb_tests_total += 1
    nbdigits = 5
    if expected_res:
        expected_res = round(expected_res,nbdigits)
    if res == expected_res:
        print("Test " + test_name + " OK")
        nb_tests_ok += 1
        return 1
    else:
        print("Test " + test_name + " KO : " + str(res) + " vs " + str(expected_res))
        tests_ko += [test_name]
        return 0
    
def launchFSAlg(fname,cls,expected_res,test_name="NA"):
    parameters = getFSParams(fname,cls)
    launchTest(FS_ALG,parameters,expected_res,test_name)

def launchFSCBCAlg(fname,cls,expected_res,test_name="NA"):
    parameters = getFSCBCParams(fname,cls)
    launchTest(FS_CBC_ALG,parameters,expected_res,test_name)

    
sum_a0 = 1500
sum_a0_cbc = 1000
sum_a1 = 5200
sum_a1_cbc = 5000
sum_a2 = 1800
sum_2_cbc = 1300
    
launchFSAlg(rb_fname,0,sum_a0/25,"rbC0")
launchFSAlg(rb_fname,1,sum_a1/25,"rbC1")
launchFSAlg(rb_fname,2,sum_a2/25,"rbC2")
launchFSCBCAlg(rb_fname,0,sum_a0_cbc/18,"rbC0CBC")
launchFSCBCAlg(rb_fname,1,sum_a1_cbc/18,"rbC1CBC")
launchFSCBCAlg(rb_fname,2,sum_2_cbc/18,"rbC2CBC")

launchFSAlg(rb0_fname,0,0,"rb0C0")
launchFSAlg(rb0_fname,1,sum_a1/16,"rb0C1")
launchFSAlg(rb0_fname,2,sum_a2/16,"rb0C2")
launchFSCBCAlg(rb0_fname,0,0,"rb0C0CBC")
launchFSCBCAlg(rb0_fname,1,sum_a1_cbc/12,"rb0C1CBC")
launchFSCBCAlg(rb0_fname,2,sum_2_cbc/12,"rb0C2CBC")

launchFSAlg(rb1_fname,0,sum_a0/15,"rb1C0")
launchFSAlg(rb1_fname,1,0,"rb1C1")
launchFSAlg(rb1_fname,2,sum_a2/15,"rb1C2")
launchFSCBCAlg(rb1_fname,0,sum_a0_cbc/10,"rb1C0CBC")
launchFSCBCAlg(rb1_fname,1,0,"rb1C1CBC")
launchFSCBCAlg(rb1_fname,2,sum_2_cbc/10,"rb1C2CBC")

launchFSAlg(rb2_fname,0,sum_a0/19,"rb2C0")
launchFSAlg(rb2_fname,1,sum_a1/19,"rb2C1")
launchFSAlg(rb2_fname,2,0,"rb2C2")
launchFSCBCAlg(rb2_fname,0,sum_a0_cbc/14,"rb2C0CBC")
launchFSCBCAlg(rb2_fname,1,sum_a1_cbc/14,"rb2C1CBC")
launchFSCBCAlg(rb2_fname,2,0,"rb2C2CBC")

print ("Nb tests OK = " + str(nb_tests_ok) + " / " + str(nb_tests_total))
print ("Tests KO : ")
for tn in tests_ko:
    print ("  - " + str(tn))