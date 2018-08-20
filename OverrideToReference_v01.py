import maya.cmds as mc

def OverrideToReference():
    selection = mc.ls(sl=True);
    for x in selection:
        mc.setAttr(x + '.overrideEnabled', 1);
        mc.setAttr(x + '.overrideDisplayType', 2);
        
OverrideToReference();