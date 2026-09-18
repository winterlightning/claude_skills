"""Independent 32px profile of text-dollar-sign-document-b37bb9fc.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = None
SOURCE_PATH = 'icon_set/dist/text28/text-dollar-sign-document-b37bb9fc.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = ()
PROFILE_SOURCE_KEYS = ('text/text-dollar-sign-document-b37bb9fc',)
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '0b60805075825de6351c29d4ad4035fbc7ce8a6d67f23913d395e446d19d9831'

class Drawing(TextSub32):
    icon_id = 'text-dollar-sign-document-b37bb9fc-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 26
    text_ink_bounds = (0.0, 0.0, 26.0, 32.0)

    def build(self):
        self.add_bezier('p1-r1-1', (16, 12), ((15, 11), (14, 10), (12, 10)))
        self.add_bezier('p1-r1-2', (12, 10), ((10, 10), (8, 11), (8, 13)))
        self.add_bezier('p1-r1-3', (8, 13), ((8, 13), (8, 13), (8, 13)))
        self.add_bezier('p1-r1-4', (8, 13), ((8, 17), (16, 15), (16, 19)))
        self.add_bezier('p1-r1-5', (16, 19), ((16, 19), (16, 19), (16, 19)))
        self.add_bezier('p1-r1-6', (16, 19), ((16, 22), (14, 23), (12, 23)))
        self.add_bezier('p1-r1-7', (12, 23), ((10, 23), (8, 22), (8, 21)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
        self.add_line('p2-r1-1', (12, 8), (12, 24))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (2, 2), (19, 2))
        self.add_line('p3-r1-2', (19, 2), (24, 7))
        self.add_line('p3-r1-3', (24, 7), (24, 30))
        self.add_line('p3-r1-4', (24, 30), (2, 30))
        self.add_line('p3-r1-5', (2, 30), (2, 2))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', closed=False)
