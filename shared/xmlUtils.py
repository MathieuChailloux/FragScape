
import xml.etree.ElementTree as ET

def getChildren(root):
    res = []
    for c in root:
        res.append(c)
    return res
    
def getNbChildren(root):
    res = 0
    for c in root:
        res += 1
    return res
    
def xmlEscape( s ):
    s = s.replace("&", "&amp;")
    s = s.replace("<", "&lt;")
    s = s.replace(">", "&gt;")
    s = s.replace("\"", "&quot;")
    return s