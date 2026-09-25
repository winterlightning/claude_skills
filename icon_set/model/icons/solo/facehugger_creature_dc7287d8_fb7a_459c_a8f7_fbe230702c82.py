"""A small central alien body spreads four long jointed legs to either side. A narrow tail descends from its lower tip, curls left into a broad loop, and then sweeps to the right.

SQUARE visible bounds (4,4)-(44,44); eight jointed legs and looping tail retained around a simple body. No useful Lucide match. Leg pairs mirror; tail curls asymmetrically.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dc7287d8-fb7a-459c-a8f7-fbe230702c82'
SOURCE_PATH = 'pictographic-primitives/science/facehugger_dc7287d8-fb7a-459c-a8f7-fbe230702c82.svg'
AUTHOR = 'gpt-6'

class FacehuggerCreature(Solo48):
    icon_id = 'facehugger-creature'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "science"
    aliases = ()
    keywords = ('facehugger', 'alien', 'creature', 'tail', 'legs', 'fiction')

    def segments(self, name, *points):
        for i,(a,b) in enumerate(zip(points,points[1:]),1):
            self.add_line(f'{name}-{i}',a,b)

    def circle(self, name, x, y, r):
        points = [(x-r,y), (x,y-r), (x+r,y), (x,y+r)]
        for i, start in enumerate(points):
            self.add_arc(f'{name}-{i}', start, points[(i+1)%4], radius_x=r)
        self.add_contour(name, *(f'{name}-{i}' for i in range(4)), closed=True)

    def build(self):
        self.add_polyline('body',(24,10),(30,14),(30,22),(24,26),(18,22),(18,14),closed=True)
        for side in (-1,1):
            def p(x,y): return (24+side*x,y)
            self.add_polyline(f'leg-{side}-1',p(6,14),p(12,6),p(18,6))
            self.add_polyline(f'leg-{side}-2',p(6,14),p(12,14),p(18,18))
            self.add_polyline(f'leg-{side}-3',p(6,22),p(12,24),p(18,28))
            self.add_polyline(f'leg-{side}-4',p(6,22),p(10,30))
            for j in range(1,5):self.relate('connect','body',f'leg-{side}-{j}')
        self.add_line('tail-neck',(24,26),(24,30))
        self.add_arc('tail-turn',(24,30),(12,36),radius_x=12,radius_y=6)
        self.add_arc('tail-left',(12,36),(6,39),radius_x=6,radius_y=3,sweep=False)
        self.add_arc('tail-bottom',(6,39),(12,42),radius_x=6,radius_y=3,sweep=False)
        self.add_arc('tail-end',(12,42),(42,38),radius_x=30,radius_y=4,sweep=False)
        self.add_contour('tail','tail-neck','tail-turn','tail-left','tail-bottom','tail-end')
        self.relate('connect','tail','body')
