"""Injection Syringe.
Plan: Centerline bounds (10,4)-(38,44). Mirrored barrel/plunger; split flange at true attachments; two measurement ticks; rounded barrel bottom and needle.
References: supplied original source; Lucide syringe: straight barrel, flanges, needle, and minimal measurement marks.
Human guidance: human_ref/user.svg and full_body_ref.png where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '938a87be-bbb1-55be-bf83-4c3930a0c140'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/instrument syringe_938a87be-bbb1-55be-bf83-4c3930a0c140.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'injection-syringe-938a87be'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    aliases = ('injection-syringe',)
    keywords = ('injection', 'syringe')

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
        stroke("barrel",(16,14),[((16,30),),((24,38),8,8,False),((32,30),8,8,False),((32,22),),((32,14),)])
        self.add_polyline("flange",(10,14),(16,14),(20,14),(28,14),(32,14),(38,14))
        self.relate("connect","barrel","flange")
        self.add_polyline("plunger-top",(16,4),(20,4),(28,4),(32,4))
        for x in (20,28):
            self.add_line(f"plunger-{x}",(x,4),(x,14))
            self.relate("connect",f"plunger-{x}","flange")
            self.relate("connect",f"plunger-{x}","plunger-top")
        for y in (22,30):
            self.add_line(f"tick-{y}",(32,y),(26,y));self.relate("connect","barrel",f"tick-{y}")
        self.add_line("needle",(24,38),(24,44));self.relate("connect","barrel","needle")

