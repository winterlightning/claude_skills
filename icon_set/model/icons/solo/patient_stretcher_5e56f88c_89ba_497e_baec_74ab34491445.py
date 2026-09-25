"""Patient Stretcher.
Plan: (4,8)-(44,40). Long bed, left headrest, right rail, crossed folding frame and paired wheels. Padding reduced to a clear top rail.
References: supplied original source; no useful direct Lucide match; source bed, scissor frame and wheels.
Human guidance: human_ref/user.svg and full_body_ref.png where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5e56f88c-89ba-497e-baec-74ab34491445'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/instrument ambulance bed_5e56f88c-89ba-497e-baec-74ab34491445.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'patient-stretcher-5e56f88c'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    categories = ("health", "primitives")
    aliases = ('patient-stretcher',)
    keywords = ('patient', 'stretcher')

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
        self.add_polyline("bed",(4,18),(6,18),(12,18),(16,18),(26,18),(36,18),(40,18),(44,18))
        self.add_polyline("headrest",(6,18),(6,8),(16,8),(16,18));self.relate("connect","headrest","bed")
        self.add_polyline("rail",(26,18),(26,10),(40,10),(40,18));self.relate("connect","rail","bed")
        self.add_polyline("support-a",(12,18),(24,25),(36,32));self.add_polyline("support-b",(36,18),(24,25),(12,32));self.relate("connect","support-a","support-b")
        self.add_polyline("base",(8,32),(12,32),(36,32),(40,32))
        for s in ("support-a","support-b"):self.relate("connect",s,"bed");self.relate("connect",s,"base")
        for x in (8,40):
            stroke(f"wheel-{x}",(x,32),[((x+4,36),4,4,True),((x,40),4,4,True),((x-4,36),4,4,True),((x,32),4,4,True)],True)
            self.relate("connect","base",f"wheel-{x}")

