"""Mouthwash Bottle.
Plan: (8,4)-(40,44). Capped narrow neck, broad rounded shoulders, and label band; mirrored bottle outline.
References: supplied original source; Lucide milk: narrow neck and broad bottle with one intrinsic label band.
Human guidance: human_ref/user.svg and full_body_ref.png where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '88443da7-00a5-49de-8d71-8411759a21c4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/mouthwash bottle_88443da7-00a5-49de-8d71-8411759a21c4.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'mouthwash-bottle-88443da7'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    aliases = ('mouthwash-bottle',)
    keywords = ('mouthwash', 'bottle')

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
        stroke("bottle",(16,4),[((32,4),),((32,12),),((32,14),),((40,22),8,8,True),((40,24),),((40,34),),((40,38),),((34,44),6,6,True),((14,44),),((8,38),6,6,True),((8,34),),((8,24),),((8,22),),((16,14),8,8,True),((16,12),),((16,4),)],True)
        self.add_line("cap",(16,12),(32,12));self.relate("connect","cap","bottle")
        for y in (24,34):self.add_line(f"label-{y}",(8,y),(40,y));self.relate("connect",f"label-{y}","bottle")

