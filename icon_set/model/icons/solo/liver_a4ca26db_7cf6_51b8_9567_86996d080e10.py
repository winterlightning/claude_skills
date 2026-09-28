"""Liver.
Plan: (4,10)-(44,38). Large rounded left lobe, tapering right lobe and single attached division. Gallbladder omitted to preserve open negative space.
References: supplied original source; no direct useful Lucide match; broad organic curves from original.
Human guidance: human_ref/user.svg and full_body_ref.png where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a4ca26db-7cf6-51b8-9567-86996d080e10'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/specialty liver_a4ca26db-7cf6-51b8-9567-86996d080e10.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'liver-a4ca26db'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    categories = ("health", "primitives")
    aliases = ('liver',)
    keywords = ('liver',)

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
        stroke("liver",(4,26),[((20,10),16,16,True),((30,10),),((40,10),),((44,14),4,4,True),((38,24),12,12,True),((20,34),),((8,38),),((4,34),4,4,True),((4,26),)],True)
        stroke("division",(30,10),[((26,18),8,8,False),((26,28),)])
        self.relate("connect","liver","division")

