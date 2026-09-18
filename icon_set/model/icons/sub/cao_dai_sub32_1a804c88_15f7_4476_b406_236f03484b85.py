"""Independent 32px profile of cao-dai.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '1a804c88-15f7-4476-b406-236f03484b85'
SOURCE_PATH = 'pictographic-primitives/religion/cao dai_1a804c88-15f7-4476-b406-236f03484b85.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('1a804c88-15f7-4476-b406-236f03484b85', 'pictographic-primitives/religion/cao dai_1a804c88-15f7-4476-b406-236f03484b85.svg'),)
PROFILE_SOURCE_KEYS = ('solo/cao-dai',)
SOLO_SOURCE_ICON_IDS = ('cao-dai',)
REFERENCE_EXPORT_SHA256 = '8f0b14c0be93c3280fca07bd1dee6d577014a0608fb2808dbedd6b64f1cc113b'

class Drawing(Sub32):
    icon_id = 'cao-dai-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'religion'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (16, 5), (30, 27))
        self.add_line('p1-r1-2', (30, 27), (2, 27))
        self.add_line('p1-r1-3', (2, 27), (16, 5))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (16, 20), (16, 20))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
