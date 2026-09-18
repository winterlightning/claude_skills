"""Independent 32px profile of diagonal-paintbrush-with-curved-bristles.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'dc5549d8-9b05-4532-8ed4-ef18efdf1b0f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/brush_dc5549d8-9b05-4532-8ed4-ef18efdf1b0f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('dc5549d8-9b05-4532-8ed4-ef18efdf1b0f', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/brush_dc5549d8-9b05-4532-8ed4-ef18efdf1b0f.svg'), ('a0a41169-49c3-4086-a686-b84d4a7eeb92', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/brush_a0a41169-49c3-4086-a686-b84d4a7eeb92.svg'))
PROFILE_SOURCE_KEYS = ('solo/diagonal-paintbrush-with-curved-bristles',)
SOLO_SOURCE_ICON_IDS = ('diagonal-paintbrush-with-curved-bristles',)
REFERENCE_EXPORT_SHA256 = 'eb6248c50044d536c9f23dee3c893cfc9dd5394b08b169fc95148cff18defc3a'

class Drawing(Sub32):
    icon_id = 'diagonal-paintbrush-with-curved-bristles-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/design'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (13, 14), (25, 2))
        self.add_arc('p1-r1-2', (25, 2), (30, 7), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (30, 7), (18, 19))
        self.add_bezier('p1-r1-4', (18, 19), ((18, 21), (19, 22), (19, 23)))
        self.add_bezier('p1-r1-5', (19, 23), ((19, 28), (12, 30), (2, 30)))
        self.add_bezier('p1-r1-6', (2, 30), ((8, 24), (6, 14), (11, 14)))
        self.add_bezier('p1-r1-7', (11, 14), ((11, 14), (12, 14), (13, 14)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
        self.add_line('p2-r1-1', (13, 14), (18, 19))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-3', 'p2-r1-1')
        self.relate("connect", 'p1-r1-4', 'p2-r1-1')
        self.relate("connect", 'p1-r1-7', 'p2-r1-1')
