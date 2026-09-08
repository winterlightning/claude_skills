"""Jupiter sign with curved upper stroke and long crossed stem. Extremes (5,2)-(43,46). No close Lucide subject; intentional directional asymmetry."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '57680136-9b34-5273-871a-73ba089a1d22'
SOURCE_PATH = 'pictographic-primitives/culture/batch-04/astrology jupiter_57680136-9b34-5273-871a-73ba089a1d22.svg'
AUTHOR = 'astra-chatgpt'

class JupiterAstrologicalSymbol(Solo48):
    icon_id = 'jupiter-astrological-symbol'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/culture"
    aliases = ()
    keywords = ('jupiter', 'astrology', 'planet', 'symbol', 'horoscope', 'glyph', 'zeus', 'expansion')

    def build(self) -> None:
        self.add_line('crest',(5,2),(12,2))
        self.add_arc('hook',(12,2),(22,12),radius_x=10)
        self.add_arc('sweep',(22,12),(17,23),radius_x=16)
        self.add_line('diagonal',(17,23),(7,32))
        self.add_line('bar-left',(7,32),(33,32))
        self.add_line('bar-right',(33,32),(43,32))
        self.add_contour('bowl','crest','hook','sweep','diagonal','bar-left','bar-right')
        self.add_line('stem-top',(33,12),(33,32))
        self.add_line('stem-bottom',(33,32),(33,46))
        self.add_contour('stem','stem-top','stem-bottom')
        self.relate('connect','bowl','stem')
