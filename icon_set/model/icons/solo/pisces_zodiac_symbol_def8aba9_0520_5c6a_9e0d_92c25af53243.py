"""Pisces: paired inward-bowing arcs joined by a horizontal bar; no identity detail omitted.

Construction: No useful Lucide subject match found.
Keyshape VRECT_XL; centerline extremes are the visible bounds inset by 2.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'def8aba9-0520-5c6a-9e0d-92c25af53243'
SOURCE_PATH = 'pictographic-primitives/culture/batch-05/astrology cancer_def8aba9-0520-5c6a-9e0d-92c25af53243.svg'


class PiscesZodiacSymbol(Solo48):
    icon_id = 'pisces-zodiac-symbol'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/culture"
    aliases = ()
    keywords = ('pisces', 'zodiac', 'astrology', 'fish', 'horoscope', 'star sign', 'symbol', 'water')

    def build(self) -> None:
        self.add_arc("left-top", (5, 2), (15, 24), radius_x=10, radius_y=22)
        self.add_arc("left-bottom", (15, 24), (5, 46), radius_x=10, radius_y=22)
        self.add_contour("left", "left-top", "left-bottom")
        self.add_arc("right-top", (43, 2), (33, 24), radius_x=10, radius_y=22, sweep=False)
        self.add_arc("right-bottom", (33, 24), (43, 46), radius_x=10, radius_y=22, sweep=False)
        self.add_contour("right", "right-top", "right-bottom")
        self.add_polyline("bar", (7,24), (15,24), (33,24), (41,24))
        self.relate("connect", "bar", "left")
        self.relate("connect", "bar", "right")
