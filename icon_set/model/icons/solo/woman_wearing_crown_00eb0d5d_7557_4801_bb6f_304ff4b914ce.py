"""A front-facing woman's head wears a tall three-pointed crown with round tips. Center-parted hair curls outward at the jaw, and the face has small eyes and a short mouth.
Lucide crown points and user head construction. Three-point crown and outward hair curls retained. Center part, tip beads and eyes omitted; bilateral symmetry retained.
VRECT_L: centerline extremes (8,6)-(40,42); freshly authored on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '00eb0d5d-7557-4801-bb6f-304ff4b914ce'
SOURCE_PATH = 'pictographic-primitives/work/workflow manager female crown_00eb0d5d-7557-4801-bb6f-304ff4b914ce.svg'
AUTHOR = 'gpt-6'

class WomanWearingCrown(Solo48):
    icon_id = 'woman-wearing-crown'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'work'
    aliases = ()
    keywords = ('woman', 'crown', 'queen', 'leader', 'head', 'royalty')

    def build(self) -> None:
        # Height repair: exact SOLO48 keyshape extremes; original subject and stroke retained.
        self.add_polyline('crown', (14, 18), (10, 4), (18, 10), (24, 4), (30, 10), (38, 4), (34, 18), (24, 18), closed=True)
        self.add_polyline('hair-left', (14, 18), (14, 28), (14, 30), (8, 38), (16, 38), closed=False)
        self.add_arc('chin', (16, 38), (32, 38), radius_x=8, radius_y=6, sweep=False, large_arc=False)
        self.add_polyline('hair-right', (32, 38), (40, 38), (34, 30), (34, 28), (34, 18), closed=False)
        self.relate('connect', 'hair-left', 'crown')
        self.relate('connect', 'hair-left', 'chin')
        self.relate('connect', 'chin', 'hair-right')
        self.relate('connect', 'hair-right', 'crown')
        self.add_line('mouth', (22, 32), (26, 32))
