# Variant of crocodile-in-water-v2; parent file remains unchanged.
'A crocodile in water with a single horizontal snout line. HRECT_M extremes (2,11)-(46,37) preserve the low aquatic profile. The rectangular mouth return is removed; brow, eye and waves remain. No useful local Lucide crocodile match. Right-facing asymmetry is intentional.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ca6a591c-ff28-52f1-afee-3a6b95328acd'
SOURCE_PATH = 'pictographic-primitives/animals/reptile crocodile water_ca6a591c-ff28-52f1-afee-3a6b95328acd.svg'
AUTHOR = 'gpt-6'

class CrocodileInWaterVariant4(Solo48):
    icon_id = 'crocodile-in-water-v4'
    variant_of = 'crocodile-in-water-v2'
    variant_label = 'Single horizontal mouth'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals/reptiles'
    aliases = ()
    keywords = ('crocodile', 'alligator', 'water', 'swim', 'river', 'reptile', 'waves', 'submerged')

    def build(self) -> None:
        self.add_line('water-left', (2, 19), (10, 19))
        self.add_line('ridge-up', (10, 19), (14, 15))
        self.add_line('ridge-down', (14, 15), (18, 19))
        self.add_line('back', (18, 19), (19, 19))
        self.add_arc('brow', (19, 19), (35, 19), radius_x=8, radius_y=8, sweep=True)
        self.add_line('snout-top', (35, 19), (46, 19))
        self.add_contour('crocodile', 'water-left', 'ridge-up', 'ridge-down', 'back', 'brow', 'snout-top')
        self.add_dot('eye', (27, 19))
        self.add_arc('wave-left', (2, 32), (16, 32), radius_x=7, radius_y=5, sweep=False)
        self.add_arc('wave-middle', (16, 32), (32, 32), radius_x=8, radius_y=5, sweep=False)
        self.add_arc('wave-right', (32, 32), (46, 32), radius_x=7, radius_y=5, sweep=False)
        self.add_contour('water', 'wave-left', 'wave-middle', 'wave-right')
