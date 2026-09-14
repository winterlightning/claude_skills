"""Right-facing crocodile above water with a distinct eye, enlarged brow, deeper snout and lower scalloped waves. HRECT_M centerline bounds (4,8)-(44,40). No useful exact Lucide crocodile match."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ca6a591c-ff28-52f1-afee-3a6b95328acd'
SOURCE_PATH = 'pictographic-primitives/animals/reptile crocodile water_ca6a591c-ff28-52f1-afee-3a6b95328acd.svg'
AUTHOR = 'gpt-6'

class CrocodileInWater(Solo48):
    icon_id = 'crocodile-in-water'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals/reptiles'
    aliases = ()
    keywords = ('crocodile', 'alligator', 'water', 'swim', 'river', 'reptile', 'waves', 'submerged')

    def build(self):
        self.add_line('back-1', (4, 18), (6, 18))
        self.add_line('back-2', (6, 18), (10, 14))
        self.add_line('back-3', (10, 14), (14, 18))
        self.add_line('back-4', (14, 18), (17, 18))
        self.add_arc('brow', (17, 18), (37, 18), radius_x=10)
        self.add_line('snout-1', (37, 18), (44, 18))
        self.add_line('snout-2', (44, 18), (44, 27))
        self.add_line('snout-3', (44, 27), (35, 27))
        self.add_contour('crocodile', 'back-1', 'back-2', 'back-3', 'back-4', 'brow', 'snout-1', 'snout-2', 'snout-3')
        self.add_arc('wave-left', (4, 37), (14, 37), radius_x=5, radius_y=3, sweep=False)
        self.add_arc('wave-mid', (14, 37), (30, 37), radius_x=8, radius_y=3, sweep=False)
        self.add_arc('wave-right', (30, 37), (44, 37), radius_x=7, radius_y=3, sweep=False)
        self.add_contour('water', 'wave-left', 'wave-mid', 'wave-right')
        self.add_dot('eye', (27, 18))
