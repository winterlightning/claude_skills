"""Molar Tooth.
Plan: (8,4)-(40,44). Paired crown lobes and equal rounded roots with a deep open central notch; crown groove omitted.
References: supplied original source; Lucide bone: rounded biological ends; original molar twin-root silhouette.
Human guidance: human_ref/user.svg and full_body_ref.png where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6120fd88-df4b-5d97-b808-229a95697404'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/tooth_6120fd88-df4b-5d97-b808-229a95697404.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'molar-tooth-6120fd88'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    aliases = ('molar-tooth',)
    keywords = ('molar', 'tooth')

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
        stroke("tooth",(8,12),[((16,4),8,8,True),((24,8),8,4,True),((32,4),8,4,True),((40,12),8,8,True),((36,40),),((28,40),4,4,True),((28,32),),((20,32),4,4,False),((20,40),),((12,40),4,4,True),((8,12),)],True)

