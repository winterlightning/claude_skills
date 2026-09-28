"""A pointing hand selecting a house above it.
Plan: VRECT_L suits the upright index finger and raised house. Visible ink bounds: (6, 2, 42, 46).
Reduction: Door and palm creases omitted; folded fingers merged into one curve. Index finger and thumb opening widened.
Construction: Lucide hand: rounded fingertip and coherent palm; house: peaked outline. Shared human references inspected for body-part vocabulary."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'eb4e4433-41fd-4f9e-9779-df93d4b8c025'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_32/real estate search house 2_eb4e4433-41fd-4f9e-9779-df93d4b8c025.svg'
AUTHOR = 'gpt-6'
PLAN = 'A pointing hand selecting a house above it.'
OMISSIONS = 'Door and palm creases omitted; folded fingers merged into one curve. Index finger and thumb opening widened.'
CONSTRUCTION_REFERENCES = 'Lucide hand: rounded fingertip and coherent palm; house: peaked outline. Shared human references inspected for body-part vocabulary.'
KEYSHAPE_INK_BOUNDS = (6, 2, 42, 46)

class Drawing(Solo48):
    icon_id = 'real-estate-search-house-2'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('real', 'estate', 'search', 'house', '2')

    def build(self):
        self.add_polyline('house', (28, 10), (34, 4), (40, 10), (40, 14), (28, 14), closed=True)
        self.add_arc('palm-round', (16, 44), (8, 36), radius_x=8)
        self.add_line('palm-left', (8, 36), (8, 26))
        self.relate('connect', 'palm-round', 'palm-left')
        self.add_polyline('thumb-index', (8, 26), (16, 32), (16, 24))
        self.add_arc('index-tip', (16, 24), (24, 24), radius_x=4)
        self.add_line('index-right', (24, 24), (24, 32))
        self.add_bezier('folded-fingers', (24, 32), ((28, 28), (36, 28), (36, 32)))
        self.add_bezier('palm-right', (36, 32), ((36, 36), (34, 40), (34, 44)))
        self.relate('connect', 'palm-left', 'thumb-index')
        self.relate('connect', 'thumb-index', 'index-tip')
        self.relate('connect', 'index-tip', 'index-right')
        self.relate('connect', 'index-right', 'folded-fingers')
        self.relate('connect', 'folded-fingers', 'palm-right')
