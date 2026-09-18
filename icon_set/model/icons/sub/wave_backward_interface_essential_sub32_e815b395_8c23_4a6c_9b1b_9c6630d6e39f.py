"""Independent 32px profile of wave-backward-interface-essential.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'e815b395-8c23-4a6c-9b1b-9c6630d6e39f'
SOURCE_PATH = 'pictographic-primitives/interface-essential/wave backward_e815b395-8c23-4a6c-9b1b-9c6630d6e39f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e815b395-8c23-4a6c-9b1b-9c6630d6e39f', 'pictographic-primitives/interface-essential/wave backward_e815b395-8c23-4a6c-9b1b-9c6630d6e39f.svg'),)
PROFILE_SOURCE_KEYS = ('solo/wave-backward-interface-essential',)
SOLO_SOURCE_ICON_IDS = ('wave-backward-interface-essential',)
REFERENCE_EXPORT_SHA256 = 'c9eae89019e3e2de1db111e5b01ee8b9ab19a13eb8720e59dffbd5000475cd60'

class Drawing(Sub32):
    icon_id = 'wave-backward-interface-essential-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (15, 2), ((9, 6), (5, 10), (5, 16)))
        self.add_bezier('p1-r1-2', (5, 16), ((5, 22), (9, 26), (15, 30)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_bezier('p2-r1-1', (27, 6), ((23, 9), (20, 13), (20, 16)))
        self.add_bezier('p2-r1-2', (20, 16), ((20, 20), (23, 23), (27, 26)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
