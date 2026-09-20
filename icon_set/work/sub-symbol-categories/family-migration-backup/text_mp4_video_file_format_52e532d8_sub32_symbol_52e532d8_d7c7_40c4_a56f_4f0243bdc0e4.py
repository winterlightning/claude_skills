# Independent container symbol; edit separately from linked side sub-icon.
"""Independent 32px profile of text-mp4-video-file-format-52e532d8.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32
SOURCE_ICON_ID = '52e532d8-d7c7-40c4-a56f-4f0243bdc0e4'
SOURCE_PATH = 'icon_set/dist/text32/text-mp4-video-file-format-52e532d8.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('52e532d8-d7c7-40c4-a56f-4f0243bdc0e4', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/mp4 (text)_52e532d8-d7c7-40c4-a56f-4f0243bdc0e4.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-mp4-video-file-format-52e532d8',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-m-uppercase', 'letter-p-uppercase', 'digit-4')
REFERENCE_EXPORT_SHA256 = 'fd8bda7a8a41f3373d6080756c4dcda4b5ab58fc72cdb44c02977ae1009c7395'

class DrawingContainerSymbol(TextSub32):
    icon_id = 'text-mp4-video-file-format-52e532d8-sub32-symbol'
    variant_of = 'text-mp4-video-file-format-52e532d8-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/text-mp4-video-file-format-52e532d8-sub32'
    counterpart_icon_id = 'text-mp4-video-file-format-52e532d8-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 89
    text_ink_bounds = (0.0, 0.0, 89.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (64, 2), (64, 20))
        self.add_bezier('p1-r1-2', (64, 20), ((64, 20), (64, 20), (64, 20)))
        self.add_line('p1-r1-3', (64, 20), (87, 20))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (82, 2), (82, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (36, 30), (36, 2))
        self.add_line('p3-r1-2', (36, 2), (46, 2))
        self.add_bezier('p3-r1-3', (46, 2), ((53, 2), (56, 6), (56, 9)))
        self.add_bezier('p3-r1-4', (56, 9), ((56, 13), (53, 17), (46, 17)))
        self.add_line('p3-r1-5', (46, 17), (36, 17))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', closed=False)
        self.add_line('p4-r1-1', (2, 30), (2, 2))
        self.add_line('p4-r1-2', (2, 2), (15, 20))
        self.add_line('p4-r1-3', (15, 20), (28, 2))
        self.add_line('p4-r1-4', (28, 2), (28, 30))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', closed=False)
