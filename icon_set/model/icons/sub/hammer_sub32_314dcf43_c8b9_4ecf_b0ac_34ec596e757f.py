"""Independent 32px profile of hammer.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '314dcf43-c8b9-4ecf-b0ac-34ec596e757f'
SOURCE_PATH = 'pictographic-primitives/interface-essential/hammer_314dcf43-c8b9-4ecf-b0ac-34ec596e757f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('314dcf43-c8b9-4ecf-b0ac-34ec596e757f', 'pictographic-primitives/interface-essential/hammer_314dcf43-c8b9-4ecf-b0ac-34ec596e757f.svg'),)
PROFILE_SOURCE_KEYS = ('solo/hammer',)
SOLO_SOURCE_ICON_IDS = ('hammer',)
REFERENCE_EXPORT_SHA256 = '48dae44b7d52f8d77a57ab4a36955c2e4755daa4841299535e399b9d17244146'

class Drawing(Sub32):
    icon_id = 'hammer-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (30, 30), (16, 17))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (22, 11), (11, 21))
        self.add_line('p2-r1-2', (11, 21), (2, 12))
        self.add_line('p2-r1-3', (2, 12), (12, 2))
        self.add_arc('p2-r1-4', (12, 2), (13, 2), radius_x=27, radius_y=27, large_arc=False, sweep=False)
        self.add_line('p2-r1-5', (13, 2), (22, 11))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
