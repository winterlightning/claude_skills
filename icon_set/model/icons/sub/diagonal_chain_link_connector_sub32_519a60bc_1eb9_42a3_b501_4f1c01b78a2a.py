"""Independent 32px profile of diagonal-chain-link-connector.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '519a60bc-1eb9-42a3-b501-4f1c01b78a2a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/hyperlink_519a60bc-1eb9-42a3-b501-4f1c01b78a2a.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('519a60bc-1eb9-42a3-b501-4f1c01b78a2a', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/hyperlink_519a60bc-1eb9-42a3-b501-4f1c01b78a2a.svg'), ('2801d7d4-7df7-460f-b313-f397a066219c', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/hyperlink_2801d7d4-7df7-460f-b313-f397a066219c.svg'))
PROFILE_SOURCE_KEYS = ('solo/diagonal-chain-link-connector', 'solo/diagonal-chain-links-interlocking')
SOLO_SOURCE_ICON_IDS = ('diagonal-chain-link-connector', 'diagonal-chain-links-interlocking')
REFERENCE_EXPORT_SHA256 = '40edea25b8bceccc760427741eb8201f06df59852bac0da04b72ed06dc5c3e19'

class Drawing(Sub32):
    icon_id = 'diagonal-chain-link-connector-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (13, 7), (16, 4))
        self.add_bezier('p1-r1-2', (16, 4), ((18, 2), (19, 2), (21, 2)))
        self.add_arc('p1-r1-3', (21, 2), (30, 11), radius_x=9, radius_y=9, large_arc=False, sweep=True)
        self.add_bezier('p1-r1-4', (30, 11), ((30, 13), (30, 14), (28, 16)))
        self.add_line('p1-r1-5', (28, 16), (25, 19))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (19, 25), (16, 28))
        self.add_bezier('p2-r1-2', (16, 28), ((14, 30), (13, 30), (11, 30)))
        self.add_arc('p2-r1-3', (11, 30), (2, 21), radius_x=9, radius_y=9, large_arc=False, sweep=True)
        self.add_bezier('p2-r1-4', (2, 21), ((2, 19), (2, 18), (4, 16)))
        self.add_line('p2-r1-5', (4, 16), (7, 13))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.add_line('p3-r1-1', (11, 21), (21, 11))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
