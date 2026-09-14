'A tall gooseneck tap has a short side lever projecting right from its upright base. Three long downward water streams hang below the curved spout, with the outer streams slightly bowed.\n\nConstruction: Arched faucet with two parallel water streams. Bounds (8,4)-(40,44).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'caf31cea-0aee-4442-aafd-b4d8cfd90818'
SOURCE_PATH = 'pictographic-primitives/wayfinding/water fountain jet_caf31cea-0aee-4442-aafd-b4d8cfd90818.svg'
AUTHOR = 'gpt-6'

class ArchedTapRunningWater(Solo48):
    icon_id = 'arched-tap-running-water'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/wayfinding'
    aliases = ()
    keywords = ('tap', 'faucet', 'water', 'stream', 'plumbing', 'lever')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_line('outer-stem', (8, 44), (8, 20))
        self.add_arc('arch', (8, 20), (40, 20), radius_x=16, radius_y=16, large_arc=False, sweep=True)
        self.add_line('inner-stem-1', (40, 20), (30, 20))
        self.add_line('inner-stem-2', (30, 20), (30, 18))
        self.add_arc('inner-arch', (30, 18), (18, 18), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_line('inner-upright', (18, 18), (18, 44))
        self.add_line('base', (18, 44), (8, 44))
        self.add_line('water-28', (28, 30), (28, 38))
        self.add_line('water-40', (40, 30), (40, 38))
        self.add_contour('tap', 'outer-stem', 'arch', 'inner-stem-1', 'inner-stem-2', 'inner-arch', 'inner-upright', 'base', closed=True)
