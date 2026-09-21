"""Awareness Ribbon Symbol.

Plan: Loop ribbon with diagonal crossing and two broad tails; remove redundant fold lines.
Construction reference: Lucide ribbon: top loop with crossed flat-cut tails.
Keyshape VRECT_L: whole subject uses the exact SOLO48 inset envelope.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8d04928d-83dd-4d17-a7ec-1662a74d856b'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_32/ribbon_8d04928d-83dd-4d17-a7ec-1662a74d856b.svg'
AUTHOR = 'gpt-6-astra'

class Drawing(Solo48):
    icon_id = 'folded-awareness-ribbon'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/misc'
    aliases = ()
    keywords = ('awareness', 'ribbon', 'symbol')

    def build(self):
        self.arc('loop',(14,14),(34,14),10)
        self.add_line('tail-left',(34,14),(8,44))
        self.add_line('tail-right',(14,14),(40,44))
        for tail in ['tail-left','tail-right']: self.relate('connect','loop',tail)
        self.relate('connect','tail-left','tail-right')

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
