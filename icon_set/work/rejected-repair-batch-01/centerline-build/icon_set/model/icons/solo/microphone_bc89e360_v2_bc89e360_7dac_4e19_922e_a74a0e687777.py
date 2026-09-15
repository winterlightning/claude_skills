'microphone-bc89e360: independent smooth-curve repair.\n\nConstruction: Centered waveform: shared horizontal axis and matched outer bars, with deliberate rhythmic height steps.\nKeyshape: VRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/audio-lines.svg and atomic-debug/audio-lines.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'bc89e360-7dac-4e19-922e-a74a0e687777'
SOURCE_PATH = 'pictographic-primitives/audio/microphone_bc89e360-7dac-4e19-922e-a74a0e687777.svg'
AUTHOR = 'gpt-6'


class MicrophoneBc89e360Variant2(Solo48):
    icon_id = 'microphone-bc89e360-v2'
    variant_of = 'microphone-bc89e360'
    variant_label = 'Smooth curves and symmetry'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'audio'
    aliases = ()
    keywords = ('microphone', 'audio')
    keyshape = Keyshape.VRECT_L

    def build(self):
        for i,(x,half) in enumerate(((8,4),(16,14),(24,20),(32,12),(40,4))):
            line(self,f'bar-{i}',(x,24-half),(x,24+half))
        contacts(self)
