"""An open crosshair ring with four radial ticks. CIRCLE radial extremes 4 and44, radius14 ring. Lucide crosshair informs fourfold repetition; source ticks extend beyond the rim."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9d332ab9-20bd-4d62-ab6e-f4d2685df651'
SOURCE_PATH = 'pictographic-primitives/symbol/focus with target_9d332ab9-20bd-4d62-ab6e-f4d2685df651.svg'
AUTHOR = 'gpt-6'


class Crosshair(Solo48):
    icon_id = 'crosshair'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('crosshair', 'target', 'focus', 'aim', 'locate', 'gps', 'precision', 'scope')

    def build(self) -> None:
        cx, cy, radius = 24, 24, 14
        nodes = [(cx,cy-radius),(cx+radius,cy),(cx,cy+radius),(cx-radius,cy)]
        for i in range(4):
            self.add_arc(f'rim-{i}', nodes[i], nodes[(i+1)%4], radius_x=radius)
        self.add_contour('rim', *(f'rim-{i}' for i in range(4)), closed=True)
        for name, a, b in [('top',(24,6),(24,16)),('right',(42,24),(32,24)),('bottom',(24,42),(24,32)),('left',(6,24),(16,24))]:
            node = {'top': (24,10), 'right': (38,24), 'bottom': (24,38), 'left': (10,24)}[name]
            self.add_polyline('tick-'+name, a, node, b)
            self.relate('connect', 'rim', 'tick-'+name)
