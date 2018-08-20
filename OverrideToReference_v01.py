import maya.cmds as mc

selection = mc.ls(sl=True);

def OverrideToReference():
    for x in selection:
        mc.setAttr(x + '.overrideEnabled', 1);
        mc.setAttr(x + '.overrideDisplayType', 2);
        
OverrideToReference();