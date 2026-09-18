"""Independent 32px profile of state32-43b3b89e-0139-4c66-91f6-1ac0c13d9617.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '43b3b89e-0139-4c66-91f6-1ac0c13d9617'
SOURCE_PATH = 'icon_set/assets/combination-state32/43b3b89e-0139-4c66-91f6-1ac0c13d9617.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('43b3b89e-0139-4c66-91f6-1ac0c13d9617', 'icon_set/assets/combination-state32/43b3b89e-0139-4c66-91f6-1ac0c13d9617.svg'),)
PROFILE_SOURCE_KEYS = ()
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '5528bab66070890a9f291e7dde4144380662871574d25a974fa689e7dab894f0'

class Drawing(Sub32):
    icon_id = 'state32-43b3b89e-0139-4c66-91f6-1ac0c13d9617'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (2, 25))
        self.add_bezier('p1-r1-2', (2, 25), ((2, 23), (6.666666666666668, 22), (16, 22)))
        self.add_bezier('p1-r1-3', (16, 22), ((25.333333333333332, 22), (30, 23), (30, 25)))
        self.add_line('p1-r1-4', (30, 25), (30, 30))
        self.add_line('p1-r1-5', (30, 30), (2, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_arc('p2-r1-1', (10, 8), (22, 8), radius_x=6, radius_y=6, large_arc=True, sweep=False)
        self.add_arc('p2-r1-2', (22, 8), (10, 8), radius_x=6, radius_y=6, large_arc=True, sweep=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
