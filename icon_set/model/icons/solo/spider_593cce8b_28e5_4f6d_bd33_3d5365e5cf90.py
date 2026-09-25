from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '593cce8b-28e5-4f6d-bd33-3d5365e5cf90'
SOURCE_PATH = 'pictographic-primitives/animals/spider_593cce8b-28e5-4f6d-bd33-3d5365e5cf90.svg'
AUTHOR = 'gpt-6'


class Spider(Solo48):
    icon_id = 'spider'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ()
    keywords = ('spider', 'arachnid', 'eight legs', 'bug', 'web', 'halloween', 'tarantula', 'insect')

    def build(self):
        # Spider: two tangent round body sections and eight clean legs meeting their exact extrema.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        def c(name, x, y, radius):
            a(name+'-top', (x-radius,y), (x+radius,y), radius)
            a(name+'-bottom', (x+radius,y), (x-radius,y), radius)
            self.add_contour(name, name+'-top', name+'-bottom', closed=True)

        c('abdomen',24,32,10)
        c('head',24,14,8)
        link('connect','abdomen','head')
        for side in (-1,1):
            for j,(x,y,ex,ey) in enumerate(((24,6,12,6),(16,14,6,18),(14,32,6,28),(24,42,10,42))):
                start=(x if side<0 else 48-x,y)
                end=(ex if side<0 else 48-ex,ey)
                l(f'leg-{side}-{j}',start,end)
                link('connect',f'leg-{side}-{j}','head' if j<2 else 'abdomen')
        link('connect','leg--1-0','leg-1-0')
        link('connect','leg--1-3','leg-1-3')
