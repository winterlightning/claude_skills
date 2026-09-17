"""Otoscope.
Plan: (8,4)-(40,44). Rounded examination head, right-facing cone, short neck, and diagonally leaning handle. Small surface details omitted.
References: supplied original source; Lucide syringe: a clear working head and long handle; supplied otoscope silhouette.
Human guidance: human_ref/user.svg and full_body_ref.png where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f70c2406-a544-5580-be96-8973e5704265'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/otoscope_f70c2406-a544-5580-be96-8973e5704265.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'otoscope-f70c2406'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    aliases = ('otoscope',)
    keywords = ('otoscope',)

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
        stroke("head",(12,8),[((16,4),4,4,True),((28,4),),((32,8),4,4,True),((32,16),),((28,20),4,4,True),((17,20),),((16,20),),((12,16),4,4,True),((12,8),)],True)
        self.add_polyline("cone",(32,8),(40,9),(40,18),(32,16));self.relate("connect","head","cone")
        self.add_line("neck",(17,20),(17,29));self.relate("connect","neck","head")
        self.add_polyline("handle",(12,28),(17,29),(22,30),(18,44),(8,42),closed=True);self.relate("connect","neck","handle")

