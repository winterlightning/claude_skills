"""A plain-headed woman in an A-line dress stands left of a man. Lucide person-standing informs economical limbs; small arm stubs and trouser seams are reduced."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3f9770e9-9cf6-4ca7-8f89-f37f07aff7a2'
SOURCE_PATH = 'pictographic-primitives/users/multiple man woman_3f9770e9-9cf6-4ca7-8f89-f37f07aff7a2.svg'
AUTHOR = 'gpt-6'


class CoupleStanding(Solo48):
    icon_id = 'couple-standing'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/groups"
    aliases = ()
    keywords = ('couple', 'woman', 'man', 'people', 'pair', 'restroom', 'figures', 'gender')

    def circle(self, name, cx, cy, radius):
        top, bottom = (cx, cy-radius), (cx, cy+radius)
        self.add_arc(name+'-a',top,bottom,radius_x=radius)
        self.add_arc(name+'-b',bottom,top,radius_x=radius)
        self.add_contour(name,name+'-a',name+'-b',closed=True)

    def male_body(self, name, cx, cap_y=29, arm_y=33, base_y=44):
        radius=5
        self.add_arc(name+'-cap',(cx-radius,cap_y),(cx+radius,cap_y),radius_x=radius)
        pts=[(cx+radius,cap_y),(cx+radius,arm_y),(cx+4,arm_y),(cx+4,base_y),(cx-4,base_y),(cx-4,arm_y),(cx-radius,arm_y),(cx-radius,cap_y)]
        members=[name+'-cap']
        for i,(a,b) in enumerate(zip(pts,pts[1:])):
            eid=name+'-'+str(i); self.add_line(eid,a,b); members.append(eid)
        self.add_contour(name,*members,closed=True)

    def female_body(self, name, cx, shoulder_y=24, base_y=44):
        self.add_polyline(name+'-dress',(cx-2,shoulder_y),(cx+2,shoulder_y),(cx+6,35),(cx+4,35),(cx-4,35),(cx-6,35),closed=True)
        self.add_polyline(name+'-legs',(cx-4,35),(cx-4,base_y),(cx+4,base_y),(cx+4,35))
        self.relate('connect',name+'-dress',name+'-legs')


    def build(self) -> None:
        # Portrait centerline extremes (8,6)-(40,42).
        for name,cx in (('woman',14),('man',35)):
            self.circle(name+'-head',cx,9,5)
        self.female_body('woman',14)
        self.male_body('man',35)
