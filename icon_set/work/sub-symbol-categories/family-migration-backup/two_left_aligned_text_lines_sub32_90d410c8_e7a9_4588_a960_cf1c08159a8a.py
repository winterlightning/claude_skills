"""Independent 32px profile of two-left-aligned-text-lines.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '90d410c8-e7a9-4588-a960-cf1c08159a8a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/comment_90d410c8-e7a9-4588-a960-cf1c08159a8a.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('90d410c8-e7a9-4588-a960-cf1c08159a8a', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/comment_90d410c8-e7a9-4588-a960-cf1c08159a8a.svg'),)
PROFILE_SOURCE_KEYS = ('solo/two-left-aligned-text-lines',)
SOLO_SOURCE_ICON_IDS = ('two-left-aligned-text-lines',)
REFERENCE_EXPORT_SHA256 = 'e3ac75771eba9ea828c3d0ebf79d2febdea5e7f9d4fcd7a6c535dcbbb42f32a4'

class Drawing(Sub32):
    icon_id = 'two-left-aligned-text-lines-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/container-components'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 5), (30, 5))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (2, 27), (20, 27))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
