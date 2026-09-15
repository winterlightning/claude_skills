'google-podcast-logo-2: independent smooth-curve repair.\n\nConstruction: Centered waveform: shared horizontal axis and matched outer bars, with deliberate rhythmic height steps.\nKeyshape: VRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/audio-lines.svg and atomic-debug/audio-lines.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'faa1ee65-30bb-4281-aa2f-de340011fbbc'
SOURCE_PATH = 'pictographic-primitives/logos/google podcast logo 2_faa1ee65-30bb-4281-aa2f-de340011fbbc.svg'
AUTHOR = 'gpt-6'


class GooglePodcastLogo2(Solo48):
    icon_id = 'google-podcast-logo-2'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('google', 'podcast', 'logo', 'logos')
    keyshape = Keyshape.VRECT_L

    def build(self):
        for i,(x,half) in enumerate(((8,4),(16,14),(24,20),(32,12),(40,4))):
            line(self,f'bar-{i}',(x,24-half),(x,24+half))
        contacts(self)
