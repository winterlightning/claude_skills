"""Patient Wearing Oxygen Mask.
Plan: (6,6)-(42,42). Front-facing head, broad lower-face mask, short chest hose and detached shoulder contours. Face/mask bottom32 to shoulders40 gives8 centerline /4 ink.
References: supplied original source; human_ref/user.svg: broad shoulders and round head; Lucide stethoscope: one readable hose.
Human guidance: human_ref/user.svg and full_body_ref.png where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6a37668f-13b0-58ea-bd40-b5dba7f5d7fe'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/oxygen mask head_6a37668f-13b0-58ea-bd40-b5dba7f5d7fe.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'patient-wearing-oxygen-mask-6a37668f'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    aliases = ('patient-wearing-oxygen-mask',)
    keywords = ('patient', 'wearing', 'oxygen', 'mask')

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
        stroke("head",(12,26),[((10,20),),((24,6),14,14,True),((38,20),14,14,True),((36,26),)])
        stroke("mask",(24,18),[((36,26),),((24,32),12,6,True),((12,26),12,6,True),((24,18),)],True)
        self.relate("connect","head","mask")
        stroke("left-shoulder",(6,42),[((14,40),8,2,True),((24,40),)])
        stroke("right-shoulder",(34,40),[((42,42),8,2,True)])
        stroke("hose",(24,32),[((24,40),),((26,42),2,2,False)])
        self.relate("connect","mask","hose");self.relate("connect","hose","left-shoulder")

