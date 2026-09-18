"""Independent 32px profile of text-mp3-audio-file-format-6ce39310.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '6ce39310-958b-449e-89cd-de3d5185c1de'
SOURCE_PATH = 'icon_set/dist/text32/text-mp3-audio-file-format-6ce39310.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('6ce39310-958b-449e-89cd-de3d5185c1de', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/mp3 (text)_6ce39310-958b-449e-89cd-de3d5185c1de.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-mp3-audio-file-format-6ce39310',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-m-uppercase', 'letter-p-uppercase', 'digit-3')
REFERENCE_EXPORT_SHA256 = '03d0c22bfba1708ff37be5f26208f76e8159cdb99368b58a205d67292b909a8c'

class DrawingContainerSymbol(TextSub32):
    icon_id = 'text-mp3-audio-file-format-6ce39310-sub32-symbol'
    related_origin_icon_id = 'text-mp3-audio-file-format-6ce39310-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/text-mp3-audio-file-format-6ce39310-sub32'
    counterpart_icon_id = 'text-mp3-audio-file-format-6ce39310-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 84
    text_ink_bounds = (0.0, 0.0, 84.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (64, 2), (75, 2))
        self.add_bezier('p1-r1-2', (75, 2), ((79, 2), (82, 5), (82, 9)))
        self.add_bezier('p1-r1-3', (82, 9), ((82, 13), (79, 16), (75, 16)))
        self.add_line('p1-r1-4', (75, 16), (70, 16))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (71, 16), (75, 16))
        self.add_bezier('p2-r1-2', (75, 16), ((79, 16), (82, 19), (82, 23)))
        self.add_bezier('p2-r1-3', (82, 23), ((82, 27), (79, 30), (75, 30)))
        self.add_line('p2-r1-4', (75, 30), (64, 30))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
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
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
        self.relate('connect', 'p1-r1-3', 'p2-r1-2')
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
        self.relate('connect', 'p1-r1-4', 'p2-r1-2')
