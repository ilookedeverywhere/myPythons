import maya.cmds as mc

def setCameraForScene():
    mc.setAttr("perspShape.nearClipPlane", 10);
    mc.setAttr("perspShape.farClipPlane", 100000);
        
setCameraForScene();