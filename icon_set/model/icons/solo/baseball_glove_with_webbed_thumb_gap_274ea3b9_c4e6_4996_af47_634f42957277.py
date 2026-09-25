"""Baseball Catcher Mitt.

Plan: Catcher mitt with rounded finger lobes, deep thumb gap and a single web band.
Construction reference: Lucide hand: rounded finger caps and one smooth palm arc.
Keyshape SQUARE: whole subject uses the exact SOLO48 inset envelope.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '274ea3b9-c4e6-4996-af47-634f42957277'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_05/baseball glove_274ea3b9-c4e6-4996-af47-634f42957277.svg'
AUTHOR = 'gpt-6-astra'

class Drawing(Solo48):
    icon_id = 'baseball-glove-with-webbed-thumb-gap'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('baseball', 'catcher', 'mitt')

    def build(self):

        self.path('thumb',[(6,24),(6,18)])
        self.arc('thumb-top',(6,18),(14,18),4)
        self.add_line('thumb-inner',(14,18),(14,24))
        self.arc('gap',(14,24),(22,24),4,sweep=False)
        self.add_line('finger-left',(22,24),(22,10))
        self.arc('finger-top',(22,10),(30,10),4)
        self.arc('finger-next',(30,10),(38,10),4)
        self.arc('outer-corner',(38,10),(42,14),4)
        self.add_line('outer',(42,14),(42,24))
        self.arc('palm',(42,24),(6,24),18)
        # Merge the temporary runs into one continuous contour.
        self.contours = [c for c in self.contours if not set(c.members).issubset({'outer-corner', 'palm', 'finger-next', 'finger-left', 'gap', 'thumb-inner', 'outer', 'finger-top', 'thumb-top', 'thumb-1'})]
        self.add_contour('mitt','thumb-1','thumb-top','thumb-inner','gap','finger-left','finger-top','finger-next','outer-corner','outer','palm',closed=True)
        self.add_line('web',(14,18),(22,18));self.relate('connect','mitt','web')

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
