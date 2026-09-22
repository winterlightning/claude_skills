"""Greek Letter Omega Symbol.
User explicitly requested solo geometry for this symbol, independent of typeface.
One continuous open contour, mirrored about x24. Bowl radius18 and equal outward feet. Exact bounds (6,6)-(42,42); omit micro rounding at foot corners.
Reference: pictographic-primitives/interface-essential/greek alphabet_2f242159-ca9e-43ff-8d0b-a4a49bdb4507.svg. Source supplies topology and arrangement.
Lucide omega supplies coherent bowl-to-stem contour construction, not coordinates.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '2f242159-ca9e-43ff-8d0b-a4a49bdb4507'
SOURCE_PATH = 'pictographic-primitives/interface-essential/greek alphabet_2f242159-ca9e-43ff-8d0b-a4a49bdb4507.svg'
AUTHOR = 'gpt-6-astra'

class Symbol(Solo48):
    icon_id = 'greek-letter-omega-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ('Greek Letter Omega Symbol',)
    keywords = ('greek', 'letter', 'omega', 'symbol')

    def build(self):
        self.add_line('left-foot-1',(6,42),(16,42))
        self.add_line('left-foot-2',(16,42),(16,38))
        self.add_bezier('left-lower',(16,38),((10,34),(6,31),(6,24)))
        self.add_arc('left-upper',(6,24),(24,6),radius_x=18)
        self.add_arc('right-upper',(24,6),(42,24),radius_x=18)
        self.add_bezier('right-lower',(42,24),((42,31),(38,34),(32,38)))
        self.add_line('right-foot-1',(32,38),(32,42))
        self.add_line('right-foot-2',(32,42),(42,42))
        self.add_contour('omega','left-foot-1','left-foot-2','left-lower','left-upper','right-upper','right-lower','right-foot-1','right-foot-2')
