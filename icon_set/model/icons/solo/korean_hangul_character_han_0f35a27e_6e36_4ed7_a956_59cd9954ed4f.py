"""Korean Hangul Character Han.
User explicitly requested solo geometry for this symbol, independent of typeface.
Circle radius6 at (16,22), top crossbar and short tick, right upright with arm, lower left angle. Exact bounds (8,4)-(40,44). Circle-to-crossbar centerline gap8. Preserve deliberately unequal component extents.
Reference: pictographic-primitives/interface-essential/korean alphabet_0f35a27e-6e36-4ed7-a956-59cd9954ed4f.svg. Source supplies topology and arrangement.
Lucide omega supplies coherent bowl-to-stem contour construction, not coordinates.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '0f35a27e-6e36-4ed7-a956-59cd9954ed4f'
SOURCE_PATH = 'pictographic-primitives/interface-essential/korean alphabet_0f35a27e-6e36-4ed7-a956-59cd9954ed4f.svg'
AUTHOR = 'gpt-6-astra'

class Symbol(Solo48):
    icon_id = 'korean-hangul-character-han'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ('Korean Hangul Character Han',)
    keywords = ('korean', 'hangul', 'character', 'han')

    def build(self):
        self.add_polyline('top-bar',(8,8),(16,8),(24,8))
        self.add_line('top-tick',(16,4),(16,8))
        self.relate('connect','top-tick','top-bar-1','top-bar-2')
        self.add_arc('ring-top',(10,22),(22,22),radius_x=6)
        self.add_arc('ring-bottom',(22,22),(10,22),radius_x=6)
        self.add_contour('ring','ring-top','ring-bottom',closed=True)
        self.add_polyline('right-upright',(32,16),(32,24),(32,32))
        self.add_line('right-arm',(32,24),(40,24))
        self.relate('connect','right-arm','right-upright-1','right-upright-2')
        self.add_polyline('lower-angle',(8,36),(8,44),(32,44))
