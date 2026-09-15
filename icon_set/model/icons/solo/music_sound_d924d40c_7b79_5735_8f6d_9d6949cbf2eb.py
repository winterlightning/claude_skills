'music-sound: independent smooth-curve repair.\n\nConstruction: Centered waveform: shared horizontal axis and matched outer bars, with deliberate rhythmic height steps.\nKeyshape: VRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/audio-lines.svg and atomic-debug/audio-lines.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'd924d40c-7b79-5735-8f6d-9d6949cbf2eb'
SOURCE_PATH = 'pictographic-primitives/audio/music sound_d924d40c-7b79-5735-8f6d-9d6949cbf2eb.svg'
AUTHOR = 'gpt-6'


class MusicSound(Solo48):
    icon_id = 'music-sound'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'audio'
    aliases = ()
    keywords = ('music', 'sound', 'audio')
    keyshape = Keyshape.VRECT_L

    def build(self):
        for i,(x,half) in enumerate(((8,4),(16,14),(24,20),(32,12),(40,4))):
            line(self,f'bar-{i}',(x,24-half),(x,24+half))
        contacts(self)
