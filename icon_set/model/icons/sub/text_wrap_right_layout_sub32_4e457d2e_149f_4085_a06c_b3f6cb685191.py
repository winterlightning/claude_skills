"""Independent 32px profile of text-wrap-right-layout.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '4e457d2e-149f-4085-a06c-b3f6cb685191'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/lines with small square_4e457d2e-149f-4085-a06c-b3f6cb685191.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('4e457d2e-149f-4085-a06c-b3f6cb685191', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/lines with small square_4e457d2e-149f-4085-a06c-b3f6cb685191.svg'),)
PROFILE_SOURCE_KEYS = ('solo/text-wrap-right-layout',)
SOLO_SOURCE_ICON_IDS = ('text-wrap-right-layout',)
REFERENCE_EXPORT_SHA256 = '892bd42ce288804ac3889669d5f947de82a83dc2fc79cc77348377592f2716f2'

class Drawing(Sub32):
    icon_id = 'text-wrap-right-layout-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/container-components'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (19, 5), (30, 5))
        self.add_line('p1-r1-2', (30, 5), (30, 16))
        self.add_line('p1-r1-3', (30, 16), (19, 16))
        self.add_line('p1-r1-4', (19, 16), (19, 5))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (2, 5), (12, 5))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (2, 16), (12, 16))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (2, 27), (30, 27))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
