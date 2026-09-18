"""Independent 32px profile of text-mpg-file-format-text-51747961.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '51747961-07f5-47d7-97cb-f171e1557aa1'
SOURCE_PATH = 'icon_set/dist/text32/text-mpg-file-format-text-51747961.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('51747961-07f5-47d7-97cb-f171e1557aa1', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/mpg (text)_51747961-07f5-47d7-97cb-f171e1557aa1.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-mpg-file-format-text-51747961',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-m-uppercase', 'letter-p-uppercase', 'letter-g-uppercase')
REFERENCE_EXPORT_SHA256 = 'b8c3be9996b812b9637463c9403b74fd9b7d562d481973ff1c728884df821db7'

class DrawingContainerSymbol(TextSub32):
    icon_id = 'text-mpg-file-format-text-51747961-sub32-symbol'
    related_origin_icon_id = 'text-mpg-file-format-text-51747961-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/text-mpg-file-format-text-51747961-sub32'
    counterpart_icon_id = 'text-mpg-file-format-text-51747961-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 86
    text_ink_bounds = (0.0, 0.0, 86.0, 32.0)

    def build(self):
        self.add_bezier('p1-r1-1', (81, 6), ((79, 4), (77, 2), (74, 2)))
        self.add_bezier('p1-r1-2', (74, 2), ((69, 2), (64, 9), (64, 17)))
        self.add_bezier('p1-r1-3', (64, 17), ((64, 18), (64, 20), (64, 21)))
        self.add_bezier('p1-r1-4', (64, 21), ((66, 27), (70, 29), (73, 29)))
        self.add_bezier('p1-r1-5', (73, 29), ((78, 29), (84, 24), (84, 16)))
        self.add_line('p1-r1-6', (84, 16), (76, 16))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_line('p2-r1-1', (36, 30), (36, 2))
        self.add_line('p2-r1-2', (36, 2), (46, 2))
        self.add_bezier('p2-r1-3', (46, 2), ((53, 2), (56, 6), (56, 9)))
        self.add_bezier('p2-r1-4', (56, 9), ((56, 13), (53, 17), (46, 17)))
        self.add_line('p2-r1-5', (46, 17), (36, 17))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.add_line('p3-r1-1', (2, 30), (2, 2))
        self.add_line('p3-r1-2', (2, 2), (15, 20))
        self.add_line('p3-r1-3', (15, 20), (28, 2))
        self.add_line('p3-r1-4', (28, 2), (28, 30))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
