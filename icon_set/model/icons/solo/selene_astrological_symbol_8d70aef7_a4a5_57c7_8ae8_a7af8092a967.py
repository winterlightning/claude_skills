"""Open lunar circle over a cross. Bounds (8,2)-(40,46)."""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8d70aef7-a4a5-57c7-8ae8-a7af8092a967'
SOURCE_PATH = 'pictographic-primitives/culture/batch-06/astrology selene_8d70aef7-a4a5-57c7-8ae8-a7af8092a967.svg'


class SeleneAstrologicalSymbol(Solo48):
    icon_id = 'selene-astrological-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "culture"
    aliases = ()
    keywords = ('selene', 'astrology', 'moon', 'symbol', 'horoscope', 'glyph', 'lunar', 'goddess')

    def build(self) -> None:
        self.add_arc("upper-tip", (8,6), (24,2), radius_x=16, radius_y=4)
        self.add_arc("upper", (24,2), (40,18), radius_x=16)
        self.add_arc("lower", (40,18), (24,34), radius_x=16)
        self.add_arc("lower-tip", (24,34), (8,30), radius_x=16, radius_y=4)
        self.add_contour("moon", "upper-tip", "upper", "lower", "lower-tip")
        self.add_polyline("stem", (24,34), (24,40), (24,46))
        self.add_polyline("crossbar", (17,40), (24,40), (31,40))
        self.relate("connect", "moon", "stem")
        self.relate("connect", "stem", "crossbar")
