"""Beetle Insect Symbol.

Plan: Beetle with divided wing cases, rounded head, paired antennae and three mirrored legs.
Construction reference: Lucide bug: shared shell, central seam and three mirrored leg attachments.
Keyshape SQUARE: whole subject uses the exact SOLO48 inset envelope.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c2f25e0c-a7a3-42f1-a324-58dcfcc899f6'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_06/beetle_c2f25e0c-a7a3-42f1-a324-58dcfcc899f6.svg'
AUTHOR = 'gpt-6-astra'

class Drawing(Solo48):
    icon_id = 'oval-beetle-with-six-bent-legs'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/misc'
    aliases = ()
    keywords = ('beetle', 'insect', 'symbol')

    def build(self):
        # One continuous head/body outline; each leg meets a vertical wall.
        self.arc('head',(16,18),(32,18),8)
        self.arc('top-right',(32,18),(34,20),2)
        self.add_line('right-wall',(34,20),(34,32))
        self.arc('bottom-right',(34,32),(32,38),10)
        self.arc('bottom',(32,38),(16,38),10)
        self.arc('bottom-left',(16,38),(14,32),10)
        self.add_line('left-wall',(14,32),(14,20))
        self.arc('top-left',(14,20),(16,18),2)
        self.add_contour('outline','head','top-right','right-wall','bottom-right','bottom','bottom-left','left-wall','top-left',closed=True)
        self.add_line('seam',(24,20),(24,42));self.relate('connect','outline','seam')
        for side,sgn in [('left',-1),('right',1)]:
            self.add_line('antenna-'+side,(24,10),(24+sgn*10,6))
            self.relate('connect','outline','antenna-'+side)
            for i,y in enumerate((22,30,38)):
                self.add_line(f'{side}-leg-{i}',(24+sgn*(8 if i==2 else 10),y),(24+sgn*18,y+(i-1)*4))
                self.relate('connect','outline',f'{side}-leg-{i}')
        self.relate('connect','antenna-left','antenna-right')

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
