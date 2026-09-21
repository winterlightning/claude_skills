"""Backbone JavaScript Framework Logo.

Plan: Backbone logo: rectangular structural loop crossed by diagonals; deliberate sharp geometry.
Construction reference: No useful exact Lucide match; geometric arc construction.
Keyshape VRECT_M: whole subject uses the exact SOLO48 inset envelope.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ea1369e6-eb5a-4c4d-b81f-f2ee0d7c669a'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_05/backbonejs logo_ea1369e6-eb5a-4c4d-b81f-f2ee0d7c669a.svg'
AUTHOR = 'gpt-6-astra'

class Drawing(Solo48):
    icon_id = 'crossed-diagonals-in-an-upright-rectangle'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/misc'
    aliases = ()
    keywords = ('backbone', 'javascript', 'framework', 'logo')

    def build(self):

        self.path('frame',[(10,4),(38,4),(38,14),(38,34),(38,44),(10,44),(10,34),(10,14)],True)
        self.add_line('diagonal-a',(10,14),(38,34));self.add_line('diagonal-b',(38,14),(10,34))
        for p in ['diagonal-a','diagonal-b']: self.relate('connect','frame',p)
        self.relate('connect','diagonal-a','diagonal-b')

    def circle(self, name, x, y, r, ry=None):
        ry = r if ry is None else ry
        self.add_arc(name+'-top', (x-r,y), (x+r,y), radius_x=r, radius_y=ry)
        self.add_arc(name+'-bottom', (x+r,y), (x-r,y), radius_x=r, radius_y=ry)
        self.add_contour(name, name+'-top', name+'-bottom', closed=True)

    def path(self, name, points, closed=False):
        self.add_polyline(name, *points, closed=closed)

    def arc(self, name, a, b, r, ry=None, sweep=True):
        self.add_arc(name, a, b, radius_x=r, radius_y=r if ry is None else ry, sweep=sweep)

    def rect(self, name, x, y, w, h, r=4):
        points=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),
                (x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        ids=[]
        for i,a in enumerate(points):
            b=points[(i+1)%8]; part=f'{name}-{i}'; ids.append(part)
            if i%2: self.arc(part,a,b,r)
            elif a != b: self.add_line(part,a,b)
            else: ids.pop()
        self.add_contour(name,*ids,closed=True)
