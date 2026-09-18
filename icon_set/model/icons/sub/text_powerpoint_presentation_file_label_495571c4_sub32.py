"""Independent 32px profile of text-powerpoint-presentation-file-label-495571c4.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '495571c4-175f-4ca1-8ff7-2328080ce061'
SOURCE_PATH = 'icon_set/dist/text32/text-powerpoint-presentation-file-label-495571c4.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('495571c4-175f-4ca1-8ff7-2328080ce061', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/ppt (text)_495571c4-175f-4ca1-8ff7-2328080ce061.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-powerpoint-presentation-file-label-495571c4',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-p-uppercase', 'letter-p-uppercase', 'letter-t-uppercase')
REFERENCE_EXPORT_SHA256 = '2c65de0ce29cd3453448967878cd028fdc205cead1a50b0e27e8505fe1036bde'

class Drawing(TextSub32):
    icon_id = 'text-powerpoint-presentation-file-label-495571c4-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 80
    text_ink_bounds = (0.0, 0.0, 80.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (57, 2), (78, 2))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (67, 2), (67, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (29, 30), (29, 2))
        self.add_line('p3-r1-2', (29, 2), (39, 2))
        self.add_bezier('p3-r1-3', (39, 2), ((46, 2), (49, 6), (49, 9)))
        self.add_bezier('p3-r1-4', (49, 9), ((49, 13), (46, 17), (39, 17)))
        self.add_line('p3-r1-5', (39, 17), (29, 17))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', closed=False)
        self.add_line('p4-r1-1', (2, 30), (2, 2))
        self.add_line('p4-r1-2', (2, 2), (12, 2))
        self.add_bezier('p4-r1-3', (12, 2), ((18, 2), (21, 6), (21, 9)))
        self.add_bezier('p4-r1-4', (21, 9), ((21, 13), (18, 17), (12, 17)))
        self.add_line('p4-r1-5', (12, 17), (2, 17))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', 'p4-r1-5', closed=False)
