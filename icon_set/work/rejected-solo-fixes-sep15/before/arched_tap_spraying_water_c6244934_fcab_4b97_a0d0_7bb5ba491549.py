'A tall tap curves over into a downward-facing spout with a short side lever near its base. Three short diverging streams appear beneath the open nozzle.\n\nConstruction: Arched faucet with two spreading spray marks. Bounds (8,4)-(40,44).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c6244934-fcab-4b97-a0d0-7bb5ba491549'
SOURCE_PATH = 'pictographic-primitives/wayfinding/water fountain jet_c6244934-fcab-4b97-a0d0-7bb5ba491549.svg'
AUTHOR = 'gpt-6'

class ArchedTapSprayingWater(Solo48):
    icon_id = 'arched-tap-spraying-water'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/wayfinding'
    aliases = ()
    keywords = ('tap', 'faucet', 'spray', 'water', 'plumbing', 'lever')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_line('outer-stem', (8, 44), (8, 20))
        self.add_arc('arch', (8, 20), (40, 20), radius_x=16, radius_y=16, large_arc=False, sweep=True)
        self.add_line('inner-stem-1', (40, 20), (30, 20))
        self.add_line('inner-stem-2', (30, 20), (30, 18))
        self.add_arc('inner-arch', (30, 18), (18, 18), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_line('inner-upright', (18, 18), (18, 44))
        self.add_line('base', (18, 44), (8, 44))
        self.add_line('water-28', (28, 30), (27, 34))
        self.add_line('water-40', (40, 30), (40, 34))
        self.add_contour('tap', 'outer-stem', 'arch', 'inner-stem-1', 'inner-stem-2', 'inner-arch', 'inner-upright', 'base', closed=True)
