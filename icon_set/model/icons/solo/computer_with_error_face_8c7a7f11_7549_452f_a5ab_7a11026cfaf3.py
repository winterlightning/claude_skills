"""Computer with Error Face. Authored from the supplied visual brief."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8c7a7f11-7549-452f-a5ab-7a11026cfaf3'
SOURCE_PATH = 'pictographic-primitives/websites/server error desktop_8c7a7f11-7549-452f-a5ab-7a11026cfaf3.svg'
AUTHOR = 'gpt-6'

class ComputerWithErrorFace(Solo48):
    icon_id = 'computer-with-error-face'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/technology"
    aliases = ()
    keywords = ('computer', 'error', 'face', 'monitor', 'crash', 'tongue', 'desktop')

    def build(self):
        self.box('monitor',6,6,42,36,r=2)
        for side,cx in [('left',17),('right',31)]:
            self.add_polyline(side+'-a',(cx-2,15),(cx,17),(cx+2,19))
            self.add_polyline(side+'-b',(cx+2,15),(cx,17),(cx-2,19))
            self.relate('connect',side+'-a',side+'-b')
        self.add_line('mouth',(18,27),(30,27))
        self.add_line('stand',(24,36),(24,42))
        self.add_polyline('foot',(14,42),(24,42),(34,42))
        self.relate('connect','stand','monitor')
        self.relate('connect','stand','foot')

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
