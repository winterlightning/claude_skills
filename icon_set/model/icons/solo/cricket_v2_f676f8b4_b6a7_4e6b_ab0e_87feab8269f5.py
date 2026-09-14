"""Left-facing cricket with deeper wing/body opening, raised folded hind leg and separated feet. HRECT_L centerline bounds (4,8)-(44,40). Lucide bug informed sparse attached limbs; preserve asymmetric profile."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f676f8b4-b6a7-4e6b-ab0e-87feab8269f5'
SOURCE_PATH = 'pictographic-primitives/animals/insect cricket body_f676f8b4-b6a7-4e6b-ab0e-87feab8269f5.svg'
AUTHOR = 'gpt-6'

class CricketVariant2(Solo48):
    icon_id = 'cricket-v2'
    variant_of = 'cricket'
    variant_label = 'Roomier spacing — review 03'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ()
    keywords = ('cricket', 'grasshopper', 'insect', 'locust', 'bug', 'jump', 'legs', 'chirp')

    def build(self):
        self.add_line('wing-1', (4, 20), (20, 20))
        self.add_line('wing-2', (20, 20), (30, 24))
        self.add_arc('wing-bottom', (30, 24), (24, 32), radius_x=6, radius_y=8)
        self.add_line('belly', (24, 32), (16, 32))
        self.add_arc('chest', (16, 32), (4, 20), radius_x=12, radius_y=12)
        self.add_contour('body', 'wing-1', 'wing-2', 'wing-bottom', 'belly', 'chest', closed=True)
        self.add_polyline('hind-leg', (20, 20), (34, 8), (44, 40))
        self.add_polyline('front-leg', (16, 32), (8, 40), (4, 40))
        self.add_polyline('middle-leg', (24, 32), (24, 40), (16, 40))
        self.add_line('antenna', (4, 20), (4, 8))
        for part in ('hind-leg', 'front-leg', 'middle-leg', 'antenna'):
            self.relate('connect', 'body', part)
