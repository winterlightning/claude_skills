"""MRI Scanner.
Plan: (6,6)-(42,42). Broad scanner arch surrounds open tunnel; projecting examination table with paired feet.
References: supplied original source; Lucide scan: clear imaging opening; supplied source arch and projecting table.
Human guidance: human_ref/user.svg and full_body_ref.png where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8aee0fb9-5ea5-44ef-bda3-d4be71ff2418'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/radiology scan mri_8aee0fb9-5ea5-44ef-bda3-d4be71ff2418.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'mri-scanner-8aee0fb9'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    aliases = ('mri-scanner',)
    keywords = ('mri', 'scanner')

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
        stroke("housing",(6,42),[((6,24),),((24,6),18,18,True),((42,24),18,18,True),((42,42),)])
        stroke("tunnel",(17,28),[((17,24),),((31,24),7,7,True),((31,28),)])
        stroke("table",(17,28),[((31,28),),((33,36),),((30,36),),((18,36),),((15,36),),((17,28),)],True)
        self.relate("connect","tunnel","table")
        for x in (18,30):self.add_line(f"leg-{x}",(x,36),(x,42));self.relate("connect","table",f"leg-{x}")

