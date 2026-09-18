"""Independent 32px profile of text-adobe-premiere-pro-video-editor-symbol-55570d4b.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '55570d4b-1ccd-4b43-bac8-4449335b0c0c'
SOURCE_PATH = 'icon_set/dist/text32/text-adobe-premiere-pro-video-editor-symbol-55570d4b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('55570d4b-1ccd-4b43-bac8-4449335b0c0c', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/Pr_55570d4b-1ccd-4b43-bac8-4449335b0c0c.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-adobe-premiere-pro-video-editor-symbol-55570d4b',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-p-uppercase', 'letter-r')
REFERENCE_EXPORT_SHA256 = '2d8a536be0b2f0516f0db9559ca4790b63198f94f7b7ddb10c6b511b0a87fe95'

class Drawing(TextSub32):
    icon_id = 'text-adobe-premiere-pro-video-editor-symbol-55570d4b-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 39
    text_ink_bounds = (0.0, 0.0, 39.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (29, 11), (29, 16))
        self.add_line('p1-r1-2', (29, 16), (29, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_bezier('p2-r1-1', (29, 16), ((29, 13), (32, 11), (35, 11)))
        self.add_line('p2-r1-2', (35, 11), (37, 11))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (2, 30), (2, 2))
        self.add_line('p3-r1-2', (2, 2), (12, 2))
        self.add_bezier('p3-r1-3', (12, 2), ((18, 2), (21, 6), (21, 9)))
        self.add_bezier('p3-r1-4', (21, 9), ((21, 13), (18, 17), (12, 17)))
        self.add_line('p3-r1-5', (12, 17), (2, 17))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-2', 'p2-r1-1')
