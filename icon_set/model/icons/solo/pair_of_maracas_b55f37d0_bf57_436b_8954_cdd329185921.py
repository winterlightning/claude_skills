"""Two equal round shaker heads and matching slender handles. Keep both heads, open the handles into an uncrossed pair to avoid a tight crossing. Shared x series; extremes (6,6)-(42,42)."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b55f37d0-bf57-436b-8954-cdd329185921'
SOURCE_PATH = 'pictographic-primitives/music/maracas_b55f37d0-bf57-436b-8954-cdd329185921.svg'
AUTHOR = 'gpt-6'

class PairOfMaracas(Solo48):
    icon_id = 'pair-of-maracas'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "music"
    aliases = ()
    keywords = ('maracas', 'percussion', 'shaker', 'instrument', 'latin', 'rhythm', 'music')

    def build(self):
        cx, cy, radius = 13, 13, 7
        points = ((cx-radius,cy),(cx,cy-radius),(cx+radius,cy),(cx,cy+radius))
        for n in range(4):
            self.add_arc(f'left-head-{n}',points[n],points[(n+1)%4],radius_x=radius)
        self.add_contour('left-head', *[f'left-head-{n}' for n in range(4)], closed=True)
        cx, cy, radius = 35, 13, 7
        points = ((cx-radius,cy),(cx,cy-radius),(cx+radius,cy),(cx,cy+radius))
        for n in range(4):
            self.add_arc(f'right-head-{n}',points[n],points[(n+1)%4],radius_x=radius)
        self.add_contour('right-head', *[f'right-head-{n}' for n in range(4)], closed=True)
        for name,x in (('left',13),('right',35)):
            self.add_line(f'{name}-handle',(x,20),(x,42))
            self.relate('connect',f'{name}-handle',f'{name}-head')
