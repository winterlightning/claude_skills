'microphone-sound: independent smooth-curve repair.\n\nConstruction: Centered waveform: shared horizontal axis and matched outer bars, with deliberate rhythmic height steps.\nKeyshape: VRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/audio-lines.svg and atomic-debug/audio-lines.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'f991ef0f-2aa9-4924-9670-c07e3215f3a9'
SOURCE_PATH = 'pictographic-primitives/state/microphone sound_f991ef0f-2aa9-4924-9670-c07e3215f3a9.svg'
AUTHOR = 'gpt-6'


class MicrophoneSoundVariant2(Solo48):
    icon_id = 'microphone-sound-v2'
    variant_of = 'microphone-sound'
    variant_label = 'Smooth curves and symmetry'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('microphone', 'sound', 'state')
    keyshape = Keyshape.VRECT_L

    def build(self):
        for i,(x,half) in enumerate(((8,4),(16,14),(24,20),(32,12),(40,4))):
            line(self,f'bar-{i}',(x,24-half),(x,24+half))
        contacts(self)
