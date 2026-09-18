"""Independent 32px profile of sound-interface-essential.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '7fcea682-f705-4648-b91c-f4d4d43e6872'
SOURCE_PATH = 'pictographic-primitives/interface-essential/sound_7fcea682-f705-4648-b91c-f4d4d43e6872.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('7fcea682-f705-4648-b91c-f4d4d43e6872', 'pictographic-primitives/interface-essential/sound_7fcea682-f705-4648-b91c-f4d4d43e6872.svg'),)
PROFILE_SOURCE_KEYS = ('solo/sound-interface-essential',)
SOLO_SOURCE_ICON_IDS = ('sound-interface-essential',)
REFERENCE_EXPORT_SHA256 = '70e5f819cb8ea7ae6b3e0557c89ab41c69bfacf552ca6c1d6d0c514ac54dc1ef'

class Drawing(Sub32):
    icon_id = 'sound-interface-essential-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 11), (2, 21))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (11, 2), (11, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (21, 7), (21, 25))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (30, 14), (30, 18))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
