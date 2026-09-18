"""Independent 32px profile of syringe.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '61c17587-0f1d-4e91-91d5-9bd53083e084'
SOURCE_PATH = 'pictographic-primitives/symbol/syringe_61c17587-0f1d-4e91-91d5-9bd53083e084.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('61c17587-0f1d-4e91-91d5-9bd53083e084', 'pictographic-primitives/symbol/syringe_61c17587-0f1d-4e91-91d5-9bd53083e084.svg'),)
PROFILE_SOURCE_KEYS = ('solo/syringe',)
SOLO_SOURCE_ICON_IDS = ('syringe',)
REFERENCE_EXPORT_SHA256 = 'efa2fcbd36912863a66e5123405fa1fceecf4ed585ed4ed196ff2bac591fd766'

class Drawing(Sub32):
    icon_id = 'syringe-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 18), (16, 7))
        self.add_line('p1-r1-2', (16, 7), (20, 11))
        self.add_line('p1-r1-3', (20, 11), (24, 14))
        self.add_line('p1-r1-4', (24, 14), (13, 25))
        self.add_arc('p1-r1-5', (13, 25), (8, 24), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('p1-r1-6', (8, 24), (5, 18), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_line('p2-r1-1', (8, 24), (2, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (20, 11), (27, 5))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (24, 2), (27, 5))
        self.add_line('p4-r1-2', (27, 5), (30, 8))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_line('p5-r1-1', (11, 12), (14, 15))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate("connect", 'p1-r1-2', 'p3-r1-1')
        self.relate("connect", 'p1-r1-3', 'p3-r1-1')
        self.relate("connect", 'p1-r1-5', 'p2-r1-1')
        self.relate("connect", 'p1-r1-6', 'p2-r1-1')
        self.relate("connect", 'p3-r1-1', 'p4-r1-1')
        self.relate("connect", 'p3-r1-1', 'p4-r1-2')
