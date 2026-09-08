"""Neptune: three arrow-tipped prongs, curved bowl, and lower cross; mirrored about x=24.

Construction: Lucide venus: clean stem and crossbar attachment.
Keyshape SQUARE; centerline extremes are the visible bounds inset by 2.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a181cba1-7a67-5780-bb8c-0de5147faaca'
SOURCE_PATH = 'pictographic-primitives/culture/batch-05/astrology neptune_a181cba1-7a67-5780-bb8c-0de5147faaca.svg'


class NeptuneAstrologicalSymbol(Solo48):
    icon_id = 'neptune-astrological-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/culture"
    aliases = ()
    keywords = ('neptune', 'astrology', 'planet', 'trident', 'symbol', 'horoscope', 'glyph', 'poseidon')

    def build(self) -> None:
        self.add_polyline("shaft", (24,2), (24,28), (24,38), (24,46))
        self.add_polyline("centre-tip", (19,7), (24,2), (29,7))
        self.add_line("left-prong", (7,11), (7,16))
        self.add_arc("left-bowl", (7,16), (24,28), radius_x=17, radius_y=12, sweep=False)
        self.add_arc("right-bowl", (24,28), (41,16), radius_x=17, radius_y=12, sweep=False)
        self.add_line("right-prong", (41,16), (41,11))
        self.add_contour("fork", "left-prong", "left-bowl", "right-bowl", "right-prong")
        self.add_polyline("left-tip", (2,16), (7,11), (12,16))
        self.add_polyline("right-tip", (36,16), (41,11), (46,16))
        self.add_polyline("crossbar", (16,38), (24,38), (32,38))
        self.relate("connect", "shaft", "centre-tip")
        self.relate("connect", "shaft", "fork")
        self.relate("connect", "shaft", "crossbar")
        self.relate("connect", "fork", "left-tip")
        self.relate("connect", "fork", "right-tip")
