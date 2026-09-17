"""Lungs with Curved Bronchi.
Plan: (6,6)-(42,42). Mirrored broad lung rims flank trachea; sweeping curved bronchi; open inner lung contours for breathing room.
References: supplied original source; no useful direct Lucide organ match; mirrored sparse source construction.
Human guidance: human_ref/user.svg and full_body_ref.png where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ece421f8-4e92-5be7-9b8f-9de61c6037d9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/specialty breathing_ece421f8-4e92-5be7-9b8f-9de61c6037d9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'lungs-with-curved-bronchi-ece421f8'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    aliases = ('lungs-with-curved-bronchi',)
    keywords = ('lungs', 'with', 'curved', 'bronchi')

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
        stroke("bronchi",(16,27),[((24,18),8,9,False),((32,27),8,9,False)])
        self.relate("connect","trachea","bronchi")

