"""Leo sign with small circular loop and long curled tail. Extremes (2,2)-(46,46). No useful Lucide match; directional asymmetry retained."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f909b4b5-36ec-56b9-97c5-2e94aec05d2b'
SOURCE_PATH = 'pictographic-primitives/culture/batch-04/astrology leo_f909b4b5-36ec-56b9-97c5-2e94aec05d2b.svg'
AUTHOR = 'astra-chatgpt'

class LeoZodiacSymbol(Solo48):
    icon_id = 'leo-zodiac-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/culture"
    aliases = ()
    keywords = ('leo', 'zodiac', 'astrology', 'lion', 'mane', 'horoscope', 'star sign', 'symbol')

    def build(self) -> None:
        self.add_arc('loop-top',(16,39),(2,39),radius_x=7,sweep=False)
        self.add_arc('loop-bottom',(2,39),(16,39),radius_x=7,sweep=False)
        self.add_contour('loop','loop-top','loop-bottom',closed=True)
        self.add_line('rise',(16,39),(12,16))
        self.add_arc('arch',(12,16),(36,16),radius_x=12,radius_y=14)
        self.add_line('fall',(36,16),(32,39))
        self.add_arc('tail',(32,39),(46,39),radius_x=7,sweep=False)
        self.add_contour('mane','rise','arch','fall','tail')
        self.relate('connect','loop','mane')
