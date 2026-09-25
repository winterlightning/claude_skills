"""A rounded parachute canopy sits above a tapered capsule, connected by two sloping suspension lines. The capsule flares toward a curved bottom and carries a small clipped-corner window on its front.

VRECT_XL visible bounds (6,2)-(42,46); rounded canopy, paired suspension lines and tapered reentry capsule. Clipped-corner window simplified to a dot. No useful Lucide parachute match; symmetric composition.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3cd91e8d-ab76-4982-b9f9-d0b1a3b11c1b'
SOURCE_PATH = 'pictographic-primitives/science/space capsule_3cd91e8d-ab76-4982-b9f9-d0b1a3b11c1b.svg'
AUTHOR = 'gpt-6'

class SpaceCapsuleWithParachute(Solo48):
    icon_id = 'space-capsule-with-parachute'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "science"
    aliases = ()
    keywords = ('capsule', 'parachute', 'space', 'reentry', 'window', 'landing')

    def segments(self, name, *points):
        for i,(a,b) in enumerate(zip(points,points[1:]),1):
            self.add_line(f'{name}-{i}',a,b)

    def circle(self, name, x, y, r):
        points = [(x-r,y), (x,y-r), (x+r,y), (x,y+r)]
        for i, start in enumerate(points):
            self.add_arc(f'{name}-{i}', start, points[(i+1)%4], radius_x=r)
        self.add_contour(name, *(f'{name}-{i}' for i in range(4)), closed=True)

    def build(self):
        self.add_arc('canopy',(8,16),(40,16),radius_x=16,radius_y=12)
        self.add_line('canopy-rim',(40,16),(8,16))
        self.add_contour('parachute','canopy','canopy-rim',closed=True)
        self.add_line('line-left',(8,16),(16,24));self.add_line('line-right',(40,16),(32,24))
        self.relate('connect','line-left','parachute');self.relate('connect','line-right','parachute')
        self.add_line('capsule-top',(16,24),(32,24));self.add_line('capsule-right',(32,24),(38,40))
        self.add_arc('capsule-bottom',(38,40),(10,40),radius_x=14,radius_y=4)
        self.add_line('capsule-left',(10,40),(16,24))
        self.add_contour('capsule','capsule-top','capsule-right','capsule-bottom','capsule-left',closed=True)
        self.relate('connect','capsule','line-left');self.relate('connect','capsule','line-right')
        self.add_dot('window',(24,33))
