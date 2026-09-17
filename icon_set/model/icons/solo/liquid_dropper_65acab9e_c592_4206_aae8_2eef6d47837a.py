"""Liquid Dropper.
Plan: (6,6)-(42,42). Diagonal bulb with transverse seam and narrow rounded tip. Separate short solid drop at lower-right; minimum geometry only.
References: supplied original source; Lucide pipette: diagonal working axis with a clear bulb/shaft division.
Human guidance: human_ref/user.svg and full_body_ref.png where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '65acab9e-c592-4206-aae8-2eef6d47837a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/instrument sampler_65acab9e-c592-4206-aae8-2eef6d47837a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'liquid-dropper-65acab9e'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    aliases = ('liquid-dropper',)
    keywords = ('liquid', 'dropper')

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
        stroke("bulb",(10,24),[((22,8),10,10,True),((26,16),10,10,True),((34,24),),((24,34),8,8,True),((16,26),),((10,24),10,10,True)],True)
        self.add_line("seam",(10,24),(22,8));self.relate("connect","bulb","seam")
        self.add_line("drop",(40,38),(42,42))

