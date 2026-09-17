"""Lungs with Branching Airway.
Plan: (6,6)-(42,42). Mirrored broad lung rims flank trachea; straight branching bronchi; open inner lung contours for breathing room.
References: supplied original source; no useful direct Lucide organ match; mirrored sparse source construction.
Human guidance: human_ref/user.svg and full_body_ref.png where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '00c3e678-a99f-4c0d-b05f-7b0ed40e7b2d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/specialty lungs_00c3e678-a99f-4c0d-b05f-7b0ed40e7b2d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'lungs-with-branching-airway-00c3e678'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    aliases = ('lungs-with-branching-airway',)
    keywords = ('lungs', 'with', 'branching', 'airway')

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
            def p(x,y):return(24+side*x,y)
            stroke(f"lung-{side}",p(9,14),[(p(18,34),9,20,side>0),(p(10,42),8,8,side>0),(p(8,40),2,2,side>0),(p(8,36),)])
        self.add_line("trachea",(24,6),(24,18))
        self.add_polyline("bronchi",(16,27),(24,18),(32,27))
        self.relate("connect","trachea","bronchi")

