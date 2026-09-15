"""Four detached vertical strokes grow toward a tall central peak and then shorten again. A final short upright segment turns into a horizontal tail on the right.

Preserved five unequal vertical amplitudes and right-hand tail.
Construction reference: No useful exact local match; equally spaced straight series.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0e1d6043-e5db-4554-ada5-3325084ec69e'
SOURCE_PATH = 'pictographic-primitives/weather/earthquake frequency wave graph_0e1d6043-e5db-4554-ada5-3325084ec69e.svg'
AUTHOR = 'gpt-6'

class SeismicWaveform(Solo48):
    icon_id = 'seismic-waveform'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/weather"
    aliases = ()
    keywords = ('seismic', 'waveform', 'earthquake', 'vibration', 'frequency', 'graph')

    def build(self) -> None:
        # Live HRECT_XL visible bounds: (2, 6, 46, 42).
        self.add_line('pulse-0', (4, 20), (4, 28))
        self.add_line('pulse-1', (14, 12), (14, 36))
        self.add_line('pulse-2', (24, 8), (24, 40))
        self.add_line('pulse-3', (34, 16), (34, 32))
        self.add_polyline('tail', (44, 21), (44, 28), (44, 28), closed=False)
