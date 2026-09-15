"""baht — re-authored in place for smooth SOLO48 geometry."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd48f163d-0715-5aa1-ab17-7c224344ee83'
SOURCE_PATH = 'pictographic-primitives/money/baht_d48f163d-0715-5aa1-ab17-7c224344ee83.svg'
AUTHOR = 'gpt-6'

class Baht(Solo48):
    icon_id = 'baht'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('baht', 'money')

    def build(self):
        # Two equal elliptical bowls share a spine and crossbar.
        # VRECT_L extremes: (8,4)-(40,44); circular/elliptical construction
        # follows Lucide currency's coherent arc runs, preserving the baht sign.
        left, bowl_x, stem = 8, 28, 22
        self.add_line('top', (left, 8), (bowl_x, 8))
        self.add_arc('upper-bowl', (bowl_x, 8), (bowl_x, 24), radius_x=12, radius_y=8)
        self.add_arc('lower-bowl', (bowl_x, 24), (bowl_x, 40), radius_x=12, radius_y=8)
        self.add_line('bottom', (bowl_x, 40), (left, 40))
        self.add_line('spine', (left, 40), (left, 8))
        self.add_contour('outline', 'top', 'upper-bowl', 'lower-bowl', 'bottom', 'spine', closed=True)
        self.add_line('crossbar', (left, 24), (bowl_x, 24))
        self.add_line('currency-stem', (stem, 4), (stem, 44))
        self.relate('connect', 'outline', 'crossbar')
        self.relate('connect', 'outline', 'currency-stem')
        self.relate('connect', 'crossbar', 'currency-stem')
