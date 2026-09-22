"""Hindi Devanagari Letter A.
User explicitly requested solo geometry for this symbol, independent of typeface.
Two equal radius10 lobes on x12, joined middle branch to the right upright. Headline and stem share node (32,4). Bounds (8,4)-(40,44). Remove only serif flourishes.
Reference: pictographic-primitives/interface-essential/hindi alphabet_0c0b746e-55e7-53d1-8eae-b4ec848b0441.svg. Source supplies topology and arrangement.
Lucide omega supplies coherent bowl-to-stem contour construction, not coordinates.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '0c0b746e-55e7-53d1-8eae-b4ec848b0441'
SOURCE_PATH = 'pictographic-primitives/interface-essential/hindi alphabet_0c0b746e-55e7-53d1-8eae-b4ec848b0441.svg'
AUTHOR = 'gpt-6-astra'

class Symbol(Solo48):
    icon_id = 'hindi-devanagari-letter-a'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ('Hindi Devanagari Letter A',)
    keywords = ('hindi', 'devanagari', 'letter', 'a')

    def build(self):
        self.add_line('upper-tip',(8,4),(12,4))
        self.add_arc('upper-lobe',(12,4),(12,24),radius_x=10)
        self.add_arc('lower-lobe-start',(12,24),(20,28),radius_x=10)
        self.add_arc('lower-lobe-end',(20,28),(12,44),radius_x=10)
        self.add_line('lower-tip',(12,44),(8,44))
        self.add_contour('lobes','upper-tip','upper-lobe','lower-lobe-start','lower-lobe-end','lower-tip')
        self.add_bezier('bridge',(20,28),((24,30),(28,30),(32,24)))
        self.add_polyline('upright',(32,4),(32,24),(32,44))
        self.add_polyline('headline',(24,4),(32,4),(40,4))
        self.relate('connect','bridge','lower-lobe-start','lower-lobe-end')
        self.relate('connect','bridge','upright-1','upright-2')
        self.relate('connect','upright-1','headline-1','headline-2')
