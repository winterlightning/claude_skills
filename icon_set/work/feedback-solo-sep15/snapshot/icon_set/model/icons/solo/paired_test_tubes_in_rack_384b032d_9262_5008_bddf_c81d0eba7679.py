"""Two upright test tubes with broad rims and rounded bottoms stand side by side. A horizontal rack bar passes behind their middle sections, and a separate straight base runs below them.

HRECT_XL visible bounds (2,6)-(46,42); two matching tubes, rack behind them, separate base. Lucide test-tubes informed repeated U contours and rim proportions. All structural features retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '384b032d-9262-5008-bddf-c81d0eba7679'
SOURCE_PATH = 'pictographic-primitives/science/lab tubes_384b032d-9262-5008-bddf-c81d0eba7679.svg'
AUTHOR = 'gpt-6'

class PairedTestTubesInRack(Solo48):
    icon_id = 'paired-test-tubes-in-rack'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/science"
    aliases = ()
    keywords = ('test tube', 'rack', 'laboratory', 'pair', 'glass', 'chemistry')

    def segments(self, name, *points):
        for i,(a,b) in enumerate(zip(points,points[1:]),1):
            self.add_line(f'{name}-{i}',a,b)

    def circle(self, name, x, y, r):
        points = [(x-r,y), (x,y-r), (x+r,y), (x,y+r)]
        for i, start in enumerate(points):
            self.add_arc(f'{name}-{i}', start, points[(i+1)%4], radius_x=r)
        self.add_contour(name, *(f'{name}-{i}' for i in range(4)), closed=True)

    def build(self):
        for n,x in [('left',14),('right',34)]:
            self.segments(n+'-left',(x-4,8),(x-4,20),(x-4,27))
            self.add_arc(n+'-bottom',(x-4,27),(x+4,27),radius_x=4,sweep=False)
            self.segments(n+'-right',(x+4,27),(x+4,20),(x+4,8))
            self.add_contour(n+'-tube',n+'-left-1',n+'-left-2',n+'-bottom',n+'-right-1',n+'-right-2')
            self.add_polyline(n+'-rim',(x-7,8),(x-4,8),(x+4,8),(x+7,8))
            self.relate('connect',n+'-tube',n+'-rim')
        for n,a,b in [('left',4,10),('middle',18,30),('right',38,44)]:
            self.add_line('rack-'+n,(a,20),(b,20))
        self.relate('connect','rack-left','left-tube');self.relate('connect','rack-middle','left-tube');self.relate('connect','rack-middle','right-tube');self.relate('connect','rack-right','right-tube')
        self.add_line('base',(4,40),(44,40))
