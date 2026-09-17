"""Mechanical Weighing Scale.
Plan: (8,4)-(40,44). Broad arched scale housing and attached pointer over a single dial baseline. Lower decorative arch removed.
References: supplied original source; Lucide weight: compact broad weighted silhouette; source arched dial.
Human guidance: human_ref/user.svg and full_body_ref.png where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '43a2faeb-a2a1-5fc6-8b80-41523f260ab8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/diet scale_43a2faeb-a2a1-5fc6-8b80-41523f260ab8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'mechanical-weighing-scale-43a2faeb'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    aliases = ('mechanical-weighing-scale',)
    keywords = ('mechanical', 'weighing', 'scale')

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
        stroke("body",(8,16),[((24,4),16,12,True),((40,16),16,12,True),((37,40),),((33,44),4,4,True),((15,44),),((11,40),4,4,True),((8,16),)],True)
        self.add_polyline("dial",(18,26),(24,26),(30,26))
        self.add_line("pointer",(24,26),(28,16));self.relate("connect","dial","pointer")

