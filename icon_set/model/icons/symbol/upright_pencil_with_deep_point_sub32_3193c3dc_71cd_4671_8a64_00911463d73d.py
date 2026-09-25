"""Independent 32px profile of upright-pencil-with-deep-point.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '3193c3dc-71cd-4671-8a64-00911463d73d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/design monitor pencil_3193c3dc-71cd-4671-8a64-00911463d73d.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('3193c3dc-71cd-4671-8a64-00911463d73d', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/design monitor pencil_3193c3dc-71cd-4671-8a64-00911463d73d.svg'),)
PROFILE_SOURCE_KEYS = ('solo/upright-pencil-with-deep-point',)
SOLO_SOURCE_ICON_IDS = ('upright-pencil-with-deep-point',)
REFERENCE_EXPORT_SHA256 = '33066ddd625dd665720fea632b90db8c19731784c8ff33e2cf8994a35ac804f7'

class Drawing(Sub32):
    icon_id = 'upright-pencil-with-deep-point-sub32'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'design'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (16, 2), (26, 16))
        self.add_line('p1-r1-2', (26, 16), (26, 30))
        self.add_line('p1-r1-3', (26, 30), (6, 30))
        self.add_line('p1-r1-4', (6, 30), (6, 16))
        self.add_line('p1-r1-5', (6, 16), (16, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (6, 16), (16, 20))
        self.add_line('p2-r1-2', (16, 20), (26, 16))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-2')
        self.relate('connect', 'p1-r1-2', 'p2-r1-2')
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
        self.relate('connect', 'p1-r1-5', 'p2-r1-1')
