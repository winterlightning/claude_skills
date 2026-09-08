"""Opposed bowls joined by a crossed stem. Bounds (8,2)-(40,46)."""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7f8f9ab3-5fbb-5721-8ab4-02363d3861f3'
SOURCE_PATH = 'pictographic-primitives/culture/batch-06/astrology proserpine_7f8f9ab3-5fbb-5721-8ab4-02363d3861f3.svg'


class ProserpineAstrologicalSymbol(Solo48):
    icon_id = 'proserpine-astrological-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "culture"
    aliases = ()
    keywords = ('proserpine', 'astrology', 'planet', 'symbol', 'horoscope', 'glyph', 'persephone', 'asteroid')

    def build(self) -> None:
        self.add_arc("bowl-left", (8,2), (24,18), radius_x=16, sweep=False)
        self.add_arc("bowl-right", (24,18), (40,2), radius_x=16, sweep=False)
        self.add_contour("bowl", "bowl-left", "bowl-right")
        self.add_polyline("stem", (24,18), (24,26), (24,34))
        self.add_polyline("crossbar", (16,26), (24,26), (32,26))
        self.add_arc("dome-left", (8,46), (24,34), radius_x=16, radius_y=12)
        self.add_arc("dome-right", (24,34), (40,46), radius_x=16, radius_y=12)
        self.add_contour("dome", "dome-left", "dome-right")
        self.relate("connect", "bowl", "stem")
        self.relate("connect", "stem", "crossbar")
        self.relate("connect", "stem", "dome")
