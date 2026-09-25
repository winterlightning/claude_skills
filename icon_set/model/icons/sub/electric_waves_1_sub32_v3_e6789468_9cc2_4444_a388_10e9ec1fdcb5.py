# Variant of electric-waves-1-sub32-v2; parent file remains unchanged.
"""Independent 32px profile of electric-waves-1.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'e6789468-9cc2-4444-a388-10e9ec1fdcb5'
SOURCE_PATH = 'pictographic-primitives/state/electric waves 1_e6789468-9cc2-4444-a388-10e9ec1fdcb5.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e6789468-9cc2-4444-a388-10e9ec1fdcb5', 'pictographic-primitives/state/electric waves 1_e6789468-9cc2-4444-a388-10e9ec1fdcb5.svg'),)
PROFILE_SOURCE_KEYS = ('solo/electric-waves-1',)
SOLO_SOURCE_ICON_IDS = ('electric-waves-1',)
REFERENCE_EXPORT_SHA256 = '881a581a00a906eed54f90344ffc38c3a3805d31f6febfbd161e6e588a59eda0'

class DrawingVariant3(Sub32):
    icon_id = 'electric-waves-1-sub32-v3'
    variant_of = 'electric-waves-1-sub32-v2'
    variant_label = 'Redraw proportions and source features'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Broad paired signal arcs with an evenly centered dot.
        self.add_bezier('outer',(2,12),((9,4),(23,4),(30,12)))
        self.add_bezier('inner',(9,19),((13,15),(19,15),(23,19)))
        self.add_dot('signal',(16,26))
