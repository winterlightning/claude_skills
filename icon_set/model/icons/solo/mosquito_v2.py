# Review candidate; original preserved.
"""mosquito: reconstructed at native SOLO48 size."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0145bda3-5e60-4e2f-b201-09ab64a9f332'
SOURCE_PATH = 'pictographic-primitives/animals/dragonfly_0145bda3-5e60-4e2f-b201-09ab64a9f332.svg'
AUTHOR = 'gpt-6'

class MosquitoVariant2(Solo48):
    icon_id = 'mosquito-v2'
    variant_of = 'mosquito'
    variant_label = 'Roomier openings — pending review'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('mosquito', 'insect', 'bug', 'wings', 'pest', 'bite', 'fly', 'antennae')

    def build(self):
        """Opening repair: Broadened both wings symmetrically to open their pointed counters."""
        self.add_arc('head-1', (24, 11), (24, 21), radius_x=5, radius_y=5, sweep=True)
        self.add_arc('head-2', (24, 21), (24, 11), radius_x=5, radius_y=5, sweep=True)
        self.add_contour('head', 'head-1', 'head-2', closed=True)
        self.add_line('proboscis', (24, 6), (24, 11))
        self.relate('connect', 'proboscis', 'head')
        self.add_line('abdomen', (24, 21), (24, 42))
        self.relate('connect', 'head', 'abdomen')
        self.add_arc('leg-left', (13, 10), (6, 6), radius_x=13, radius_y=13, sweep=True)
        self.add_line('wing-left-1', (24, 21), (6, 31))
        self.add_arc('wing-left-2', (6, 31), (8, 42), radius_x=6, radius_y=9, sweep=False)
        self.add_line('wing-left-3', (8, 42), (24, 21))
        self.add_contour('wing-left', 'wing-left-1', 'wing-left-2', 'wing-left-3', closed=True)
        self.relate('connect', 'wing-left', 'head')
        self.relate('connect', 'wing-left', 'abdomen')
        self.add_arc('leg-right', (35, 10), (42, 6), radius_x=13, radius_y=13, sweep=False)
        self.add_line('wing-right-1', (24, 21), (42, 31))
        self.add_arc('wing-right-2', (42, 31), (40, 42), radius_x=6, radius_y=9, sweep=True)
        self.add_line('wing-right-3', (40, 42), (24, 21))
        self.add_contour('wing-right', 'wing-right-1', 'wing-right-2', 'wing-right-3', closed=True)
        self.relate('connect', 'wing-right', 'head')
        self.relate('connect', 'wing-right', 'abdomen')
        self.relate('connect', 'wing-left', 'wing-right')
