"""Oxygen Mask.
Plan: (8,4)-(40,44). Oval oxygen mask with short nose arch and attached looping hose; tiny outlet reduced to hose junction.
References: supplied original source; Lucide stethoscope: coherent hose loops; source oval mask.
Human guidance: human_ref/user.svg and full_body_ref.png where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '71d7520b-7ad1-5d12-9dab-67a63da93573'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/oxygen mask_71d7520b-7ad1-5d12-9dab-67a63da93573.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'oxygen-mask-71d7520b'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    categories = ("health", "primitives")
    aliases = ('oxygen-mask',)
    keywords = ('oxygen', 'mask')

    def build(self):

        def stroke(name, start, segments, closed=False):
            members=[]
            for j,s in enumerate(segments):
                member=f"{name}-{j}"
                if len(s)==1: self.add_line(member,start,s[0])
                else: self.add_arc(member,start,s[0],radius_x=s[1],radius_y=s[2],sweep=s[3],large_arc=s[4] if len(s)>4 else False)
                members.append(member);start=s[0]
            self.add_contour(name,*members,closed=closed)
        def circle(name,cx,cy,r):
            stroke(name,(cx-r,cy),[((cx+r,cy),r,r,True),((cx-r,cy),r,r,True)],True)
        stroke("mask",(20,4),[((32,18),12,14,True),((20,32),12,14,True),((8,18),12,14,True),((20,4),12,14,True)],True)
        stroke("nose",(17,20),[((23,20),3,4,True)])
        stroke("hose",(20,32),[((20,36),),((28,44),8,8,False),((40,32),12,12,False),((40,26),),((32,18),8,8,False)])
        self.relate("connect","mask","hose")

