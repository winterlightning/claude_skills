"""Independent 32px profile of workflow-data-table-1-business.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'c8dfe4cb-2c1f-4086-8985-b294567074d5'
SOURCE_PATH = 'pictographic-primitives/business/workflow data table 1_c8dfe4cb-2c1f-4086-8985-b294567074d5.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('c8dfe4cb-2c1f-4086-8985-b294567074d5', 'pictographic-primitives/business/workflow data table 1_c8dfe4cb-2c1f-4086-8985-b294567074d5.svg'),)
PROFILE_SOURCE_KEYS = ('solo/workflow-data-table-1-business',)
SOLO_SOURCE_ICON_IDS = ('workflow-data-table-1-business',)
REFERENCE_EXPORT_SHA256 = '2ac32d16ecefe3bfc57dd0fea54831bcf97c249c35c6bbfb5c6ef98866b7848b'

class Drawing(Sub32):
    icon_id = 'workflow-data-table-1-business-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'business'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (30, 18), (2, 18))
        self.add_line('p1-r1-2', (2, 18), (2, 28))
        self.add_arc('p1-r1-3', (2, 28), (4, 30), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('p1-r1-4', (4, 30), (11, 30))
        self.add_line('p1-r1-5', (11, 30), (11, 8))
        self.add_line('p1-r1-6', (11, 8), (30, 8))
        self.add_line('p1-r1-7', (30, 8), (30, 28))
        self.add_arc('p1-r1-8', (30, 28), (28, 30), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-9', (28, 30), (21, 30))
        self.add_line('p1-r1-10', (21, 30), (21, 8))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', closed=False)
        self.add_line('p2-r1-1', (11, 8), (2, 8))
        self.add_line('p2-r1-2', (2, 8), (2, 18))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (16, 30), (11, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (16, 2), (4, 2))
        self.add_arc('p4-r1-2', (4, 2), (2, 4), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('p4-r1-3', (2, 4), (2, 8))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', closed=False)
        self.add_line('p5-r1-1', (16, 30), (21, 30))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (16, 2), (28, 2))
        self.add_arc('p6-r1-2', (28, 2), (30, 4), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p6-r1-3', (30, 4), (30, 8))
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', 'p6-r1-3', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-2')
        self.relate("connect", 'p1-r1-2', 'p2-r1-2')
        self.relate("connect", 'p1-r1-4', 'p3-r1-1')
        self.relate("connect", 'p1-r1-5', 'p2-r1-1')
        self.relate("connect", 'p1-r1-5', 'p3-r1-1')
        self.relate("connect", 'p1-r1-6', 'p2-r1-1')
        self.relate("connect", 'p1-r1-6', 'p6-r1-3')
        self.relate("connect", 'p1-r1-7', 'p6-r1-3')
        self.relate("connect", 'p1-r1-9', 'p5-r1-1')
        self.relate("connect", 'p1-r1-10', 'p5-r1-1')
        self.relate("connect", 'p2-r1-1', 'p4-r1-3')
        self.relate("connect", 'p2-r1-2', 'p4-r1-3')
        self.relate("connect", 'p3-r1-1', 'p5-r1-1')
        self.relate("connect", 'p4-r1-1', 'p6-r1-1')
