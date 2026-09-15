"music-sound: distinct review variant.\n\nConstruction: Music sound represented by two beamed notes at staggered heights; preserve the symbol's intentional asymmetry.\nKeyshape: VRECT_L; exact SOLO48 envelope.\nConstruction reference: audio-lines from the previously inspected Lucide original and atomic-debug library.\nPrevious canonical model is preserved."
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'd924d40c-7b79-5735-8f6d-9d6949cbf2eb'
SOURCE_PATH = 'pictographic-primitives/audio/music sound_d924d40c-7b79-5735-8f6d-9d6949cbf2eb.svg'
AUTHOR = 'gpt-6'


class MusicSoundVariant2(Solo48):
    icon_id = 'music-sound-v2'
    variant_of = 'music-sound'
    variant_label = 'Distinct subject and smooth curves'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'audio'
    aliases = ()
    keywords = ('music', 'sound', 'audio')
    keyshape = Keyshape.VRECT_L

    def build(self):
        ellipse(self,'left-note',14,38,6)
        ellipse(self,'right-note',34,30,6)
        poly(self,'beam',(20,38),(20,10),(40,4),(40,30))
        contacts(self)
