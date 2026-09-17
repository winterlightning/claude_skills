"""Radiology Beam.
Plan: (4,8)-(44,40). Two broken slanting boundaries widen leftward, facing a short upright detector. Mirrored around y24.
References: supplied original source; Lucide scan: sparse geometric imaging boundaries; original broken beam geometry.
Human guidance: human_ref/user.svg and full_body_ref.png where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '017d154a-41b8-427f-aea1-70e43bc5a903'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/radiology scanner_017d154a-41b8-427f-aea1-70e43bc5a903.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'radiology-beam-017d154a'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    aliases = ('radiology-beam',)
    keywords = ('radiology', 'beam')

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
        for side in (-1,1):
            self.add_line(f"outer-{side}",(4,24+side*16),(20,24+side*10))
            self.add_line(f"inner-{side}",(28,24+side*7),(36,24+side*4))
        self.add_line("detector",(44,16),(44,32))

