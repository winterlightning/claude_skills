"""Independent 32px profile of tactical-game-plan-diagram-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '5b3c2f02-4284-40ca-b61d-77aa84999126'
SOURCE_PATH = 'pictographic-primitives/state/strategy_5b3c2f02-4284-40ca-b61d-77aa84999126.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('5b3c2f02-4284-40ca-b61d-77aa84999126', 'pictographic-primitives/state/strategy_5b3c2f02-4284-40ca-b61d-77aa84999126.svg'),)
PROFILE_SOURCE_KEYS = ('solo/tactical-game-plan-diagram-solo',)
SOLO_SOURCE_ICON_IDS = ('tactical-game-plan-diagram-solo',)
REFERENCE_EXPORT_SHA256 = '1a5497fa2fa112ad7d6880e943ae2a16cc938a1d74da0f85a82980c0a11374c8'

class Drawing(Sub32):
    icon_id = 'tactical-game-plan-diagram-solo-profile32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (6, 2), (26, 2))
        self.add_arc('p1-r1-2', (26, 2), (30, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (30, 6), (30, 26))
        self.add_arc('p1-r1-4', (30, 26), (26, 30), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (26, 30), (6, 30))
        self.add_arc('p1-r1-6', (6, 30), (2, 26), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-7', (2, 26), (2, 6))
        self.add_arc('p1-r1-8', (2, 6), (6, 2), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_arc('p2-r1-1', (9, 21), (14, 21), radius_x=2.5, radius_y=2.5, large_arc=False, sweep=True)
        self.add_arc('p2-r1-2', (14, 21), (9, 21), radius_x=2.5, radius_y=2.5, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_bezier('p3-r1-1', (11, 18), ((11, 18), (12, 18), (12, 18)))
        self.add_bezier('p3-r1-2', (12, 18), ((14, 18), (21, 18), (21, 11)))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (18, 14), (21, 11))
        self.add_line('p4-r1-2', (21, 11), (23, 14))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_line('p5-r1-1', (9, 9), (12, 12))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (9, 12), (12, 9))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.relate("connect", 'p3-r1-2', 'p4-r1-1')
        self.relate("connect", 'p3-r1-2', 'p4-r1-2')
