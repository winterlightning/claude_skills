'A short tap extends from the upper-right and drops water into an open drinking glass below. A wavy waterline crosses the glass above its rounded base and sloping sides.\n\nConstruction: Angular tap over an open glass, with one falling drop. Bounds (8,4)-(40,44).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5bc18c17-387b-4bc2-86e7-a3fd9d5fed98'
SOURCE_PATH = 'pictographic-primitives/wayfinding/water fountain fill_5bc18c17-387b-4bc2-86e7-a3fd9d5fed98.svg'
AUTHOR = 'gpt-6'

class TapFillingGlass(Solo48):
    icon_id = 'tap-filling-glass'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    aliases = ()
    keywords = ('tap', 'glass', 'water', 'filling', 'drink', 'faucet')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_line('tap-1', (12, 15), (12, 8))
        self.add_line('tap-2', (12, 8), (16, 4))
        self.add_line('tap-3', (16, 4), (40, 4))
        self.add_line('spout', (12, 15), (20, 15))
        self.add_line('drop', (20, 24), (20, 24))
        self.add_line('glass-1', (8, 30), (12, 44))
        self.add_line('glass-2', (12, 44), (36, 44))
        self.add_line('glass-3', (36, 44), (40, 30))
        self.add_contour('tap', 'tap-1', 'tap-2', 'tap-3', closed=False)
        self.add_contour('glass', 'glass-1', 'glass-2', 'glass-3', closed=False)
        self.relate('connect', 'spout', 'tap')
