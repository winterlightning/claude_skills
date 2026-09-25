'seismic-waveform: independent smooth-curve repair.\n\nConstruction: Centered waveform: shared horizontal axis and matched outer bars, with deliberate rhythmic height steps.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/audio-lines.svg and atomic-debug/audio-lines.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '0e1d6043-e5db-4554-ada5-3325084ec69e'
SOURCE_PATH = 'pictographic-primitives/weather/earthquake frequency wave graph_0e1d6043-e5db-4554-ada5-3325084ec69e.svg'
AUTHOR = 'gpt-6'


class SeismicWaveform(Solo48):
    icon_id = 'seismic-waveform'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'weather'
    categories = ('weather', 'primitives')
    aliases = ()
    keywords = ('seismic', 'waveform', 'earthquake', 'vibration', 'frequency', 'graph')
    keyshape = Keyshape.HRECT_L

    def build(self):
        for i,(x,half) in enumerate(((4,3),(14,12),(24,16),(34,10),(44,3))):
            line(self,f'bar-{i}',(x,24-half),(x,24+half))
        contacts(self)
