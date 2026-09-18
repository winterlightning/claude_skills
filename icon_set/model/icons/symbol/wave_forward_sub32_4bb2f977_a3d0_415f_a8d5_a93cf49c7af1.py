"""Independent 32px profile of wave-forward.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '4bb2f977-a3d0-415f-a8d5-a93cf49c7af1'
SOURCE_PATH = 'pictographic-primitives/interface-essential/wave forward_4bb2f977-a3d0-415f-a8d5-a93cf49c7af1.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('4bb2f977-a3d0-415f-a8d5-a93cf49c7af1', 'pictographic-primitives/interface-essential/wave forward_4bb2f977-a3d0-415f-a8d5-a93cf49c7af1.svg'),)
PROFILE_SOURCE_KEYS = ('solo/wave-forward',)
SOLO_SOURCE_ICON_IDS = ('wave-forward',)
REFERENCE_EXPORT_SHA256 = 'a4a4958633a7d280dc62ba78cda60751483fd15f954bdaf5376620c18ed61692'

class Drawing(Sub32):
    icon_id = 'wave-forward-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (17, 2), ((23, 6), (27, 10), (27, 16)))
        self.add_bezier('p1-r1-2', (27, 16), ((27, 22), (23, 26), (17, 30)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_bezier('p2-r1-1', (5, 6), ((9, 9), (12, 13), (12, 16)))
        self.add_bezier('p2-r1-2', (12, 16), ((12, 20), (9, 23), (5, 26)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
