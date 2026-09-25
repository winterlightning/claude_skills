"""Laptop with Two Upright Screens. Authored from the supplied visual brief."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3d2cca23-b331-4167-99c3-f5d15d9a0822'
SOURCE_PATH = 'pictographic-primitives/websites/responsive design laptop_3d2cca23-b331-4167-99c3-f5d15d9a0822.svg'
AUTHOR = 'gpt-6'

class LaptopWithTwoUprightScreens(Solo48):
    icon_id = 'laptop-with-two-upright-screens'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "websites"
    categories = ("websites", "primitives")
    aliases = ()
    keywords = ('laptop', 'screens', 'responsive', 'devices', 'computer', 'display', 'mobile')

    def build(self):
        axis=24
        for name,x in [('left',6),('right',29)]: self.box(name,x,6,x+13,30,r=2)
        self.add_line('link',(19,18),(29,18))
        for name in ['left','right']: self.relate('connect','link',name)
        for name,x in [('left',12),('right',2*axis-12)]:
            self.add_line(name+'-support',(x,30),(x,42))
            self.relate('connect',name+'-support',name)
        self.add_polyline('base',(6,39),(9,42),(12,42),(36,42),(39,42),(42,39))
        for name in ['left','right']: self.relate('connect',name+'-support','base')

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
