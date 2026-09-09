# Variant of crocodile-in-water; parent file remains unchanged.
'Crocodile with a raised eye and extended rectangular snout above one smooth wave. HRECT_L (2,8)-(46,40) gives room for the eye and water. Back ridge removed to emphasize the head. Deliberate right-facing asymmetry.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ca6a591c-ff28-52f1-afee-3a6b95328acd'
SOURCE_PATH = 'pictographic-primitives/animals/reptile crocodile water_ca6a591c-ff28-52f1-afee-3a6b95328acd.svg'
AUTHOR = 'gpt-6'

class CrocodileInWaterVariant3(Solo48):
    icon_id = 'crocodile-in-water-v3'
    variant_of = 'crocodile-in-water'
    variant_label = 'Clearer crocodile head'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals/reptiles'
    aliases = ()
    keywords = ('crocodile', 'alligator', 'water', 'swim', 'river', 'reptile', 'waves', 'submerged')

    def build(self) -> None:
        # HRECT_L centerline bounds (2,8)-(46,40). Long jaw, raised eye, water.
        self.add_line('back', (2,20), (8,20))
        self.add_arc('brow-left', (8,20), (16,8), radius_x=8, radius_y=12)
        self.add_arc('brow-right', (16,8), (24,16), radius_x=8)
        self.add_line('snout-top', (24,16), (46,16))
        self.add_line('nose', (46,16), (46,27))
        self.add_line('jaw', (46,27), (19,27))
        self.add_contour('crocodile','back','brow-left','brow-right','snout-top','nose','jaw')
        self.add_dot('eye',(16,17))
        self.add_arc('water-left', (2,38), (24,38), radius_x=11, radius_y=2,sweep=False)
        self.add_arc('water-right', (24,38), (46,38), radius_x=11,radius_y=2,sweep=True)
        self.add_contour('water','water-left','water-right')
