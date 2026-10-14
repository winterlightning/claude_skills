"""Independent 32px profile of signature-sign-interface-essential.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'c8c50287-9505-4d7a-9b3a-91b9a790ffa6'
SOURCE_PATH = 'pictographic-primitives/interface-essential/signature sign_c8c50287-9505-4d7a-9b3a-91b9a790ffa6.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('c8c50287-9505-4d7a-9b3a-91b9a790ffa6', 'pictographic-primitives/interface-essential/signature sign_c8c50287-9505-4d7a-9b3a-91b9a790ffa6.svg'),)
PROFILE_SOURCE_KEYS = ('solo/signature-sign-interface-essential',)
SOLO_SOURCE_ICON_IDS = ('signature-sign-interface-essential',)
REFERENCE_EXPORT_SHA256 = '68d19f827c26741ee8476de576396b8a5579d08f2f840118b92d79a834ac3d01'

class Drawing(Sub32):
    icon_id = 'signature-sign-interface-essential-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Signature: one flowing squiggle.
        self.add_bezier('scribble', (2, 16), ((6, 0), (10, 0), (14, 16)), ((18, 32), (22, 32), (26, 16)), ((27, 12), (29, 10), (30, 10)))
