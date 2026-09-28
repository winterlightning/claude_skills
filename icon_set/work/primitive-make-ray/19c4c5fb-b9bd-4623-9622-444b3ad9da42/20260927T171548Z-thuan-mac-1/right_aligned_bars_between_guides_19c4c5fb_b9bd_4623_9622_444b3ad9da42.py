"""Right Text Alignment.

Plan: Right aligned two capsule bars between guide lines; bounds4,8,44,40. Reduce bars to strokes to protect spacing.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '19c4c5fb-b9bd-4623-9622-444b3ad9da42'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__right-aligned-bars-between-guides/20260927T171300Z-thuan-mac-1/reference/objects align top_19c4c5fb-b9bd-4623-9622-444b3ad9da42.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'right-aligned-bars-between-guides'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('right', 'aligned', 'bars', 'between', 'guides')

    def build(self):
        # Two right-aligned bars sit inside separate horizontal guides.
        self.add_line('top-guide',(4,8),(44,8))
        self.add_line('bar-wide',(14,20),(40,20))
        self.add_line('bar-short',(22,30),(40,30))
        self.add_line('bottom-guide',(4,40),(44,40))
