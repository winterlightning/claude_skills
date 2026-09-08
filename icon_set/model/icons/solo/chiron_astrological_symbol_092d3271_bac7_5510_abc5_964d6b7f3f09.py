"""Chiron: a K-shaped stem above a broad round key bow."""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '092d3271-bac7-5510-abc5-964d6b7f3f09'
SOURCE_PATH = 'pictographic-primitives/culture/batch-01/astrology chiron_092d3271-bac7-5510-abc5-964d6b7f3f09.svg'


class ChironAstrologicalSymbol(Solo48):
    icon_id = 'chiron-astrological-symbol'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "culture"
    aliases = ()
    keywords = ('chiron', 'astrology', 'key', 'symbol', 'asteroid', 'horoscope', 'glyph', 'healing')

    def build(self) -> None:
        # VRECT_M: visible extremes (9, 0, 39, 48); centerlines inset 2.
        self.add_arc("ring-right", (24,24), (24,46), radius_x=13, radius_y=11)
        self.add_arc("ring-left", (24,46), (24,24), radius_x=13, radius_y=11)
        self.add_contour("ring", "ring-right", "ring-left", closed=True)
        self.add_polyline("stem", (24,2), (24,12), (24,24))
        self.add_polyline("branches", (36,2), (24,12), (36,20))
        self.relate("connect", "stem", "ring")
        self.relate("connect", "stem", "branches")
