"""Independent 32px profile of text-lpg-fuel-text-4eb87d01.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '4eb87d01-c899-416e-bc96-396611363e1e'
SOURCE_PATH = 'icon_set/dist/text32/text-lpg-fuel-text-4eb87d01.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('4eb87d01-c899-416e-bc96-396611363e1e', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/lpg (text)_4eb87d01-c899-416e-bc96-396611363e1e.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-lpg-fuel-text-4eb87d01',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-l-uppercase', 'letter-p-uppercase', 'letter-g-uppercase')
REFERENCE_EXPORT_SHA256 = 'c0cb7a4eca87c7f3068fed28670ac911bfe9cac4b90f8674523d114bbf98f142'

class Drawing(TextSub32):
    icon_id = 'text-lpg-fuel-text-4eb87d01-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 76
    text_ink_bounds = (0.0, 0.0, 76.0, 32.0)

    def build(self):
        self.add_bezier('p1-r1-1', (71, 6), ((69, 4), (67, 2), (64, 2)))
        self.add_bezier('p1-r1-2', (64, 2), ((59, 2), (54, 9), (54, 17)))
        self.add_bezier('p1-r1-3', (54, 17), ((54, 18), (54, 20), (54, 21)))
        self.add_bezier('p1-r1-4', (54, 21), ((56, 27), (59, 29), (63, 29)))
        self.add_bezier('p1-r1-5', (63, 29), ((68, 29), (74, 24), (74, 16)))
        self.add_line('p1-r1-6', (74, 16), (66, 16))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_line('p2-r1-1', (26, 30), (26, 2))
        self.add_line('p2-r1-2', (26, 2), (36, 2))
        self.add_bezier('p2-r1-3', (36, 2), ((43, 2), (46, 6), (46, 9)))
        self.add_bezier('p2-r1-4', (46, 9), ((46, 13), (43, 17), (36, 17)))
        self.add_line('p2-r1-5', (36, 17), (26, 17))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.add_line('p3-r1-1', (2, 2), (2, 30))
        self.add_line('p3-r1-2', (2, 30), (18, 30))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
