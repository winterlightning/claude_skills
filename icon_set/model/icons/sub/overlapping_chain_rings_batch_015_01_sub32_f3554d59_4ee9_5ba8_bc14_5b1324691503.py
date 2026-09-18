"""Independent 32px profile of overlapping-chain-rings-batch-015-01.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'f3554d59-4ee9-5ba8-bc14-5b1324691503'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/attachment_f3554d59-4ee9-5ba8-bc14-5b1324691503.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f3554d59-4ee9-5ba8-bc14-5b1324691503', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/attachment_f3554d59-4ee9-5ba8-bc14-5b1324691503.svg'),)
PROFILE_SOURCE_KEYS = ('solo/overlapping-chain-rings-batch-015-01',)
SOLO_SOURCE_ICON_IDS = ('overlapping-chain-rings-batch-015-01',)
REFERENCE_EXPORT_SHA256 = '0e74914ff6b79089757cc127ea5adcb3a2d4cfb5c2dcca03894b3db6a634718b'

class Drawing(Sub32):
    icon_id = 'overlapping-chain-rings-batch-015-01-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/batch-subjects'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (8, 14), (5, 18))
        self.add_bezier('p1-r1-2', (5, 18), ((2, 21), (2, 22), (2, 24)))
        self.add_bezier('p1-r1-3', (2, 24), ((2, 24), (2, 24), (2, 24)))
        self.add_bezier('p1-r1-4', (2, 24), ((2, 28), (4, 30), (8, 30)))
        self.add_bezier('p1-r1-5', (8, 30), ((11, 30), (13, 28), (15, 26)))
        self.add_line('p1-r1-6', (15, 26), (18, 24))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_line('p2-r1-1', (24, 18), (27, 14))
        self.add_bezier('p2-r1-2', (27, 14), ((30, 11), (30, 10), (30, 8)))
        self.add_bezier('p2-r1-3', (30, 8), ((30, 4), (28, 2), (24, 2)))
        self.add_bezier('p2-r1-4', (24, 2), ((21, 2), (19, 4), (17, 6)))
        self.add_line('p2-r1-5', (17, 6), (14, 8))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.add_line('p3-r1-1', (11, 21), (21, 11))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
