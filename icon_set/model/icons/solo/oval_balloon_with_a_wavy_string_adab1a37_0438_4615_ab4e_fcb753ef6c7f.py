"""Balloon with String.

Plan: Oval balloon with a short curving string; omit tiny knot polygon.
Construction reference: Lucide balloon: coherent curved outline and short flowing attached string.
Keyshape VRECT_M: whole subject uses the exact SOLO48 inset envelope.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'adab1a37-0438-4615-ab4e-fcb753ef6c7f'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_05/balloon_adab1a37-0438-4615-ab4e-fcb753ef6c7f.svg'
AUTHOR = 'gpt-6-astra'

class Drawing(Solo48):
    icon_id = 'oval-balloon-with-a-wavy-string'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/misc'
    aliases = ()
    keywords = ('balloon', 'with', 'string')

    def build(self):

        self.arc('balloon-right',(24,4),(24,34),14,15)
        self.arc('balloon-left',(24,34),(24,4),14,15)
        self.add_contour('balloon','balloon-right','balloon-left',closed=True)
        self.arc('string-a',(24,34),(28,39),6,sweep=False)
        self.arc('string-b',(28,39),(24,44),6)
        self.add_contour('string','string-a','string-b')
        self.relate('connect','balloon','string')

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
