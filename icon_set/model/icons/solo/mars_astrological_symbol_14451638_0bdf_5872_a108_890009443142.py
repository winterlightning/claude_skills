"""Mars circle and northeast arrow. Extremes (2,2)-(46,46). Lucide mars circular ring and open arrowhead, re-authored on the integer grid."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '14451638-0bdf-5872-a108-890009443142'
SOURCE_PATH = 'pictographic-primitives/culture/batch-04/astrology mars_14451638-0bdf-5872-a108-890009443142.svg'
AUTHOR = 'astra-chatgpt'

class MarsAstrologicalSymbol(Solo48):
    icon_id = 'mars-astrological-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/culture"
    aliases = ()
    keywords = ('mars', 'astrology', 'planet', 'arrow', 'symbol', 'horoscope', 'glyph', 'masculine')

    def build(self) -> None:
        self.add_arc('ring-a',(29,22),(32,31),radius_x=15)
        self.add_arc('ring-b',(32,31),(17,46),radius_x=15)
        self.add_arc('ring-c',(17,46),(2,31),radius_x=15)
        self.add_arc('ring-d',(2,31),(17,16),radius_x=15)
        self.add_arc('ring-e',(17,16),(29,22),radius_x=15)
        self.add_contour('ring','ring-a','ring-b','ring-c','ring-d','ring-e',closed=True)
        self.add_line('shaft',(29,22),(46,2))
        self.add_polyline('head',(33,2),(46,2),(46,15))
        self.relate('connect','ring','shaft')
        self.relate('connect','shaft','head')
