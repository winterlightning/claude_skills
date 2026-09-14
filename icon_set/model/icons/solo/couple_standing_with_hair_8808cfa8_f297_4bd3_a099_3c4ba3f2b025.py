"""A short-haired man stands left of a long-haired woman in a dress. Lucide person-standing informs reduced bodies; the tiny fringe is represented by a simple hair part."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8808cfa8-f297-4bd3-a099-3c4ba3f2b025'
SOURCE_PATH = 'pictographic-primitives/users/multiple man woman 1_8808cfa8-f297-4bd3-a099-3c4ba3f2b025.svg'
AUTHOR = 'gpt-6'


class CoupleStandingWithHair(Solo48):
    icon_id = 'couple-standing-with-hair'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/groups"
    aliases = ()
    keywords = ('couple', 'man', 'woman', 'people', 'pair', 'partners', 'figures', 'family')

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
        # Square centerline extremes (6,6)-(42,42).
        for name,cx in (('man',12),('woman',36)):
            self.circle(name+'-head',cx,12,6)
        self.add_line('man-fringe',(6,12),(18,12))
        self.relate('connect','man-head','man-fringe')
        for side,x in (('left',30),('right',42)):
            self.add_line('woman-hair-'+side,(x,12),(x,19))
            self.relate('connect','woman-head','woman-hair-'+side)
        self.male_body('man',12,cap_y=32,arm_y=35,base_y=42)
        self.female_body('woman',36,shoulder_y=27,base_y=42)
