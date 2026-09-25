# Variant of microphone-sound-sub32-v2; parent file remains unchanged.
"""Independent 32px profile of microphone-sound.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'f991ef0f-2aa9-4924-9670-c07e3215f3a9'
SOURCE_PATH = 'pictographic-primitives/state/microphone sound_f991ef0f-2aa9-4924-9670-c07e3215f3a9.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f991ef0f-2aa9-4924-9670-c07e3215f3a9', 'pictographic-primitives/state/microphone sound_f991ef0f-2aa9-4924-9670-c07e3215f3a9.svg'),)
PROFILE_SOURCE_KEYS = ('solo/microphone-sound',)
SOLO_SOURCE_ICON_IDS = ('microphone-sound',)
REFERENCE_EXPORT_SHA256 = '9e7fec83b02b08562b88ecacdb030ebc8e249ff66efdd4a60e87a68ebe0fad84'

class DrawingVariant3(Sub32):
    icon_id = 'microphone-sound-sub32-v3'
    variant_of = 'microphone-sound-sub32-v2'
    variant_label = 'Redraw proportions and source features'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Restore the original five-bar sound-wave composition instead of substituting a microphone.
        for i,half in enumerate([3,8,12,8,3]):
         x=2+i*7;self.add_line(f'bar-{i}',(x,16-half),(x,16+half))
