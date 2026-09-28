"""Baguette and Loaf of Bread.

Plan: Bread basket with tall baguette and round loaf; omit scoring lines in the small loaves.
Construction reference: No useful exact Lucide match; geometric arc construction.
Keyshape SQUARE: whole subject uses the exact SOLO48 inset envelope.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8c71bf77-2ef0-42a0-ab5c-2fba761c31e4'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_08/bread baguette_8c71bf77-2ef0-42a0-ab5c-2fba761c31e4.svg'
AUTHOR = 'gpt-6-astra'

class Drawing(Solo48):
    icon_id = 'baguette-and-loaf-in-basket'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/misc'
    aliases = ()
    keywords = ('baguette', 'and', 'loaf', 'of', 'bread')

    def build(self):

        self.path('baguette',[(6,28),(6,12)])
        self.arc('bread-top',(6,12),(18,12),6)
        self.add_line('bread-side',(18,12),(18,28))
        # Merge the temporary runs into one continuous contour.
        self.contours = [c for c in self.contours if not set(c.members).issubset({'bread-side', 'bread-top', 'baguette-1'})]
        self.add_contour('long-loaf','baguette-1','bread-top','bread-side')
        self.arc('round-loaf',(28,28),(42,28),7)
        self.add_line('rim',(6,28),(42,28))
        self.arc('basket',(42,28),(6,28),18,14)
        # Merge the temporary runs into one continuous contour.
        self.contours = [c for c in self.contours if not set(c.members).issubset({'basket', 'rim'})]
        self.add_contour('basket-body','rim','basket',closed=True)
        self.relate('connect','basket-body','long-loaf');self.relate('connect','basket-body','round-loaf')

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
