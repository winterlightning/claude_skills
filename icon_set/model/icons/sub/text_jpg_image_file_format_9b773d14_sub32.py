"""Independent 32px profile of text-jpg-image-file-format-9b773d14.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '9b773d14-9d90-491b-9303-5f391fe84672'
SOURCE_PATH = 'icon_set/dist/text32/text-jpg-image-file-format-9b773d14.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('9b773d14-9d90-491b-9303-5f391fe84672', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/jpg (text)_9b773d14-9d90-491b-9303-5f391fe84672.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-jpg-image-file-format-9b773d14',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-j-uppercase', 'letter-p-uppercase', 'letter-g-uppercase')
REFERENCE_EXPORT_SHA256 = '3fdface11821d3ae05ba4ff0b7660e3ce8d28dc7937b4453abafd30b8d8dcb49'

class Drawing(TextSub32):
    icon_id = 'text-jpg-image-file-format-9b773d14-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 75
    text_ink_bounds = (0.0, 0.0, 75.0, 32.0)

    def build(self):
        self.add_bezier('p1-r1-1', (70, 6), ((68, 4), (66, 2), (64, 2)))
        self.add_bezier('p1-r1-2', (64, 2), ((58, 2), (53, 9), (53, 17)))
        self.add_bezier('p1-r1-3', (53, 17), ((53, 18), (53, 20), (54, 21)))
        self.add_bezier('p1-r1-4', (54, 21), ((55, 27), (59, 29), (63, 29)))
        self.add_bezier('p1-r1-5', (63, 29), ((68, 29), (73, 24), (73, 16)))
        self.add_line('p1-r1-6', (73, 16), (65, 16))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_line('p2-r1-1', (26, 30), (26, 2))
        self.add_line('p2-r1-2', (26, 2), (36, 2))
        self.add_bezier('p2-r1-3', (36, 2), ((42, 2), (45, 6), (45, 9)))
        self.add_bezier('p2-r1-4', (45, 9), ((45, 13), (42, 17), (36, 17)))
        self.add_line('p2-r1-5', (36, 17), (26, 17))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.add_line('p3-r1-1', (6, 2), (18, 2))
        self.add_line('p3-r1-2', (18, 2), (18, 21))
        self.add_bezier('p3-r1-3', (18, 21), ((18, 27), (14, 30), (9, 30)))
        self.add_bezier('p3-r1-4', (9, 30), ((6, 30), (3, 28), (2, 24)))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
