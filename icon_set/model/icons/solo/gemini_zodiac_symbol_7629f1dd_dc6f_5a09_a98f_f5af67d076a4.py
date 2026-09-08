"""Gemini: paired uprights and bowed serifs, mirrored around both axes. SQUARE extremes (2,2)-(46,46). No useful local Lucide subject match."""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7629f1dd-dc6f-5a09-a98f-f5af67d076a4'
SOURCE_PATH = 'pictographic-primitives/culture/batch-03/astrology gemini_7629f1dd-dc6f-5a09-a98f-f5af67d076a4.svg'


class GeminiZodiacSymbol(Solo48):
    icon_id = 'gemini-zodiac-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "culture/objects"
    aliases = ()
    keywords = ('gemini', 'zodiac', 'astrology', 'twins', 'horoscope', 'star sign', 'symbol', 'air')

    def build(self) -> None:
        for side in ('top', 'bottom'):
            def p(x,y):
                return (x, y if side == 'top' else 48-y)
            self.add_arc(side+'-left',p(2,2),p(15,7),radius_x=43,sweep=side=='bottom')
            self.add_arc(side+'-middle',p(15,7),p(33,7),radius_x=60,sweep=side=='bottom')
            self.add_arc(side+'-right',p(33,7),p(46,2),radius_x=43,sweep=side=='bottom')
            self.add_contour(side,side+'-left',side+'-middle',side+'-right')
        for x,side in ((15,'left'),(33,'right')):
            self.add_line(side,(x,7),(x,41))
            self.relate('connect',side,'top')
            self.relate('connect',side,'bottom')
