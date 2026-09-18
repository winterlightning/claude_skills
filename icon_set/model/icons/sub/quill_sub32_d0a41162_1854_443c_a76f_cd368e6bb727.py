"""Independent 32px profile of quill.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'd0a41162-1854-443c-a76f-cd368e6bb727'
SOURCE_PATH = 'pictographic-primitives/design/quill_d0a41162-1854-443c-a76f-cd368e6bb727.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('d0a41162-1854-443c-a76f-cd368e6bb727', 'pictographic-primitives/design/quill_d0a41162-1854-443c-a76f-cd368e6bb727.svg'),)
PROFILE_SOURCE_KEYS = ('solo/quill',)
SOLO_SOURCE_ICON_IDS = ('quill',)
REFERENCE_EXPORT_SHA256 = 'b3bc4f3461d4afd2a382f9581921ec27100785f14627c69b248bc4ed322aa721'

class Drawing(Sub32):
    icon_id = 'quill-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'design'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (7, 25), ((7, 23), (7, 22), (7, 21)))
        self.add_bezier('p1-r1-2', (7, 21), ((7, 11), (20, 4), (30, 2)))
        self.add_bezier('p1-r1-3', (30, 2), ((28, 16), (21, 26), (12, 26)))
        self.add_bezier('p1-r1-4', (12, 26), ((11, 26), (9, 25), (7, 25)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (2, 30), (7, 25))
        self.add_line('p2-r1-2', (7, 25), (18, 14))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-1', 'p2-r1-2')
        self.relate("connect", 'p1-r1-4', 'p2-r1-1')
        self.relate("connect", 'p1-r1-4', 'p2-r1-2')
