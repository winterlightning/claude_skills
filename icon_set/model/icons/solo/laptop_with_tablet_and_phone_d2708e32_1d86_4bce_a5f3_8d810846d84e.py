"""Laptop with Tablet and Phone. Authored from the supplied visual brief."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd2708e32-1d86-4bce-a5f3-8d810846d84e'
SOURCE_PATH = 'pictographic-primitives/websites/responsive design laptop_d2708e32-1d86-4bce-a5f3-8d810846d84e.svg'
AUTHOR = 'gpt-6'

class LaptopWithTabletAndPhone(Solo48):
    icon_id = 'laptop-with-tablet-and-phone'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/technology"
    aliases = ()
    keywords = ('laptop', 'tablet', 'phone', 'responsive', 'devices', 'computer', 'display')

    def build(self):
        self.box('tablet',13,8,26,29,r=2)
        self.box('phone',35,8,44,29,r=2)
        self.add_polyline('laptop',(6,37),(6,20))
        self.add_polyline('base',(6,37),(7,40),(41,40),(42,37))
        self.relate('connect','laptop','base')

    def box(self, name, x0, y0, x1, y1, r=3):
        # One rounded rectangle definition; all corners share a radius.
        points = [(x0+r,y0),(x1-r,y0),(x1,y0+r),(x1,y1-r),
                  (x1-r,y1),(x0+r,y1),(x0,y1-r),(x0,y0+r)]
        members=[]
        for i,p in enumerate(points):
            q=points[(i+1)%8]; part=f'{name}-{i}';members.append(part)
            if i%2: self.add_arc(part,p,q,radius_x=r)
            else: self.add_line(part,p,q)
        self.add_contour(name,*members,closed=True)
