import maya.cmds as mc

def SetRenderSubdivs():
    selection = mc.ls(sl=True);
    for y in selection:
        mc.setAttr(y + 'Shape.aiSubdivType', 1);
        mc.setAttr(y + 'Shape.aiSubdivIterations', 3);
        
SetRenderSubdivs();