"""Independent 32px profile of horizontal-chain-link.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'b4c96571-b91a-5c18-ae5c-9991078d4792'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/hyperlink_b4c96571-b91a-5c18-ae5c-9991078d4792.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('b4c96571-b91a-5c18-ae5c-9991078d4792', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/hyperlink_b4c96571-b91a-5c18-ae5c-9991078d4792.svg'),)
PROFILE_SOURCE_KEYS = ('solo/horizontal-chain-link',)
SOLO_SOURCE_ICON_IDS = ('horizontal-chain-link',)
REFERENCE_EXPORT_SHA256 = '96613f489f00818202b8110f36cef6070c09c6ab562561a713e0d742ae86ea76'

class Drawing(Sub32):
    icon_id = 'horizontal-chain-link-sub32'
    keyshape = Keyshape.HRECT_L
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (13, 6), (8, 6))
        self.add_arc('p1-r1-2', (8, 6), (2, 12), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_line('p1-r1-3', (2, 12), (2, 20))
        self.add_arc('p1-r1-4', (2, 20), (8, 26), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_line('p1-r1-5', (8, 26), (13, 26))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (19, 6), (24, 6))
        self.add_arc('p2-r1-2', (24, 6), (30, 12), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('p2-r1-3', (30, 12), (30, 20))
        self.add_arc('p2-r1-4', (30, 20), (24, 26), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('p2-r1-5', (24, 26), (19, 26))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.add_line('p3-r1-1', (9, 16), (23, 16))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
