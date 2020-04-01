
import os
from pathlib import Path
import sys
import math

import processing

from qgis.core import QgsProcessingFeedback

FS_NAME = 'FragScape'

FS_R_ALG_bname = 'meffRaster'
FS_R_CBC_ALG_bname = 'meffRasterCBC'
FS_V_ALG_bname = 'meffVectorGlobal'

FS_R_ALG = FS_NAME + ":" + FS_R_ALG_bname
FS_R_CBC_ALG = FS_NAME + ":" + FS_R_CBC_ALG_bname
FS_V_ALG = FS_NAME + ":" + FS_V_ALG_bname

#script_path ='D:/Projets/Meff/Tests/Random/random_unit_tests.py'
#print("script_path = " + str(script_path))
#script_dir = os.path.dirname(script_path)
# script_dir = 'C:/Users/mathieu.chailloux/AppData/Roaming/QGIS/QGIS3/profiles/default/python/plugins/FragScape/tests/Random'
script_dir = 'C:/Users/fdrmc/Projets/IRSTEA/FragScape/FragScape/tests/Random'

rb_bname = "randomBase.tif"
rb0_bname = "randomBaseND0.tif"
rb1_bname = "randomBaseND1.tif"
rb2_bname = "randomBaseND2.tif"
v_bname = "randomBaseVector.gpkg"
v0_bname = "randomBaseV0.gpkg"
v1_bname = "randomBaseV1.gpkg"
v2_bname = "randomBaseV2.gpkg"
report_bname = "cropLayer.gpkg"
report_v_bname = "vectorMeshCropDissolve.gpkg"

rb_fname = os.path.join(script_dir,rb_bname)
rb0_fname = os.path.join(script_dir,rb0_bname)
rb1_fname = os.path.join(script_dir,rb1_bname)
rb2_fname = os.path.join(script_dir,rb2_bname)
v_fname = os.path.join(script_dir,v_bname)
v0_fname = os.path.join(script_dir,v0_bname)
v1_fname = os.path.join(script_dir,v1_bname)
v2_fname = os.path.join(script_dir,v2_bname)
report_fname = os.path.join(script_dir,report_bname)
report_v_fname = os.path.join(script_dir,report_v_bname)

debug_mode = True
debug_alg_mode = True
error_alg_mode = True

nbdigits = 5
    
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
  
def getFSRParams(fname,cls=None):
    return { 'INPUT' : fname,
        'CLASS' : cls,
        'UNIT' : 0,
        'OUTPUT' : 'memory:' }
    
def getFSRCBCParams(fname,cls=None):
    return { 'INPUT' : fname,
        'CLASS' : cls,
        'REPORTING' : report_fname,
        'UNIT' : 0,
        'OUTPUT' : 'memory:' }
    
def getFSVParams(fname):
    return { 'INPUT' : fname,
        'REPORTING' : v_fname,
        'INCLUDE_CBC' : False,
        'CRS' : 'EPSG:2154',
        'UNIT' : 0,
        'OUTPUT' : 'memory:' }
    
def getFSVCBCParams(fname):
    return { 'INPUT' : fname,
        'REPORTING' : report_v_fname,
        'INCLUDE_CBC' : True,
        'CRS' : 'EPSG:2154',
        'UNIT' : 0,
        'OUTPUT' : 'memory:'  }


nb_tests_ok = 0  
nb_tests_total = 0
tests_ko = []
    
def launchTest(alg_name,parameters,expected_res,check_res_func,test_name="NA"):
    global error_alg_mode, nb_tests_ok, nb_tests_total, tests_ko
    feedback = BaseFeedback()
    # error_alg_mode = (expected_res != None)
    debug("params = " + str(parameters))
    try:
        res = processing.run(alg_name,parameters,feedback=feedback)['OUTPUT_VAL']
    except Exception as e:
        debug(str(e))
        raise e
        res = None
    # TODO : fix * 100
    nb_tests_total += 1
    # nbdigits = 5
    # if expected_res:
        # expected_res = round(expected_res,nbdigits)
    debug("res = " + str(res))
    if check_res_func(res,expected_res):
        print("Test " + test_name + " OK")
        nb_tests_ok += 1
        return 1
    else:
        print("Test " + test_name + " KO : " + str(res) + " vs " + str(expected_res))
        tests_ko += [test_name]
        return 0
        
def checkTestR(res,expected_res):
    expected_res = round(expected_res,nbdigits)
    return (res == expected_res)
    
def checkTestV(res,expected_res):
    expected_res = round(expected_res,nbdigits)
    return (res == expected_res)
    # res_val = res['OUTPUT_VAL']
        
def launchTestR(alg_name,parameters,expected_res,test_name="NA"):
    launchTest(alg_name,parameters,expected_res,checkTestR,test_name)
        
def launchTestV(alg_name,parameters,expected_res,test_name="NA"):
    launchTest(alg_name,parameters,expected_res,checkTestV,test_name)
    
def launchFSRAlg(fname,cls,expected_res,test_name="NA"):
    parameters = getFSRParams(fname,cls)
    launchTestR(FS_R_ALG,parameters,expected_res,test_name)

def launchFSRCBCAlg(fname,cls,expected_res,test_name="NA"):
    parameters = getFSRCBCParams(fname,cls)
    launchTestR(FS_R_CBC_ALG,parameters,expected_res,test_name)
    
def launchFSVAlg(fname,expected_res,test_name="NA"):
    parameters = getFSVParams(fname)
    launchTestV(FS_V_ALG,parameters,expected_res,test_name)
    
def launchFSVCBCAlg(fname,expected_res,test_name="NA"):
    parameters = getFSVCBCParams(fname)
    launchTestV(FS_V_ALG,parameters,expected_res,test_name)

    
sum_ai = 8500
sum_ai_cbc = 7300
sum_a0 = 1500
sum_a0_cbc = 1000
sum_a1 = 5200
sum_a1_cbc = 5000
sum_a2 = 1800
sum_a2_cbc = 1300
tot_area = 25
report_area = 18
    
launchFSVAlg(v_fname,sum_ai/tot_area,"v")
launchFSVCBCAlg(v_fname,sum_ai_cbc/report_area,"vCBC")
launchFSVAlg(v0_fname,sum_a0/tot_area,"v0")
launchFSVCBCAlg(v0_fname,sum_a0_cbc/report_area,"v0CBC")
launchFSVAlg(v1_fname,sum_a1/tot_area,"v1")
launchFSVCBCAlg(v1_fname,sum_a1_cbc/report_area,"v1CBC")
launchFSVAlg(v2_fname,sum_a2/tot_area,"v2")
launchFSVCBCAlg(v2_fname,sum_a2_cbc/report_area,"v2CBC")
    
launchFSRAlg(rb_fname,0,sum_a0/25,"rbC0")
launchFSRAlg(rb_fname,1,sum_a1/25,"rbC1")
launchFSRAlg(rb_fname,2,sum_a2/25,"rbC2")
launchFSRCBCAlg(rb_fname,0,sum_a0_cbc/18,"rbC0CBC")
launchFSRCBCAlg(rb_fname,1,sum_a1_cbc/18,"rbC1CBC")
launchFSRCBCAlg(rb_fname,2,sum_a2_cbc/18,"rbC2CBC")

launchFSRAlg(rb0_fname,0,0,"rb0C0")
launchFSRAlg(rb0_fname,1,sum_a1/16,"rb0C1")
launchFSRAlg(rb0_fname,2,sum_a2/16,"rb0C2")
launchFSRCBCAlg(rb0_fname,0,0,"rb0C0CBC")
launchFSRCBCAlg(rb0_fname,1,sum_a1_cbc/12,"rb0C1CBC")
launchFSRCBCAlg(rb0_fname,2,sum_a2_cbc/12,"rb0C2CBC")

launchFSRAlg(rb1_fname,0,sum_a0/15,"rb1C0")
launchFSRAlg(rb1_fname,1,0,"rb1C1")
launchFSRAlg(rb1_fname,2,sum_a2/15,"rb1C2")
launchFSRCBCAlg(rb1_fname,0,sum_a0_cbc/10,"rb1C0CBC")
launchFSRCBCAlg(rb1_fname,1,0,"rb1C1CBC")
launchFSRCBCAlg(rb1_fname,2,sum_a2_cbc/10,"rb1C2CBC")

launchFSRAlg(rb2_fname,0,sum_a0/19,"rb2C0")
launchFSRAlg(rb2_fname,1,sum_a1/19,"rb2C1")
launchFSRAlg(rb2_fname,2,0,"rb2C2")
launchFSRCBCAlg(rb2_fname,0,sum_a0_cbc/14,"rb2C0CBC")
launchFSRCBCAlg(rb2_fname,1,sum_a1_cbc/14,"rb2C1CBC")
launchFSRCBCAlg(rb2_fname,2,0,"rb2C2CBC")

print ("Nb tests OK = " + str(nb_tests_ok) + " / " + str(nb_tests_total))
print ("Tests KO : ")
for tn in tests_ko:
    print ("  - " + str(tn))