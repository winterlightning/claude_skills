'sound: independent smooth-curve repair.\n\nConstruction: Centered waveform: shared horizontal axis and matched outer bars, with deliberate rhythmic height steps.\nKeyshape: VRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/audio-lines.svg and atomic-debug/audio-lines.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '515cc7f7-bcd9-45db-903d-f6e55e4d3b45'
SOURCE_PATH = 'pictographic-primitives/interface-essential/sound_515cc7f7-bcd9-45db-903d-f6e55e4d3b45.svg'
AUTHOR = 'gpt-6'


class Sound(Solo48):
    icon_id = 'sound'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('sound', 'interface-essential')
    keyshape = Keyshape.VRECT_L

    def build(self):
        for i,(x,half) in enumerate(((8,4),(16,14),(24,20),(32,12),(40,4))):
            line(self,f'bar-{i}',(x,24-half),(x,24+half))
        contacts(self)
