"""Ceres as an open sickle cup above a crossed stem."""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '79079df9-e96e-507d-97a5-a334e4f830fb'
SOURCE_PATH = 'pictographic-primitives/culture/batch-01/astrology ceres_79079df9-e96e-507d-97a5-a334e4f830fb.svg'


class CeresAstrologicalSymbol(Solo48):
    icon_id = 'ceres-astrological-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "culture"
    aliases = ()
    keywords = ('ceres', 'astrology', 'planet', 'sickle', 'symbol', 'asteroid', 'horoscope', 'glyph')

    def build(self) -> None:
        # VRECT_L: visible extremes (6, 0, 42, 48); centerlines inset 2.
        self.add_line("cup-left-tip", (8,2), (8,8))
        self.add_arc("cup-left", (8,8), (24,24), radius_x=16, sweep=False)
        self.add_arc("cup-right", (24,24), (40,8), radius_x=16, sweep=False)
        self.add_line("cup-right-tip", (40,8), (40,2))
        self.add_contour("cup", "cup-left-tip", "cup-left", "cup-right", "cup-right-tip")
        self.add_polyline("stem", (24,24), (24,38), (24,46))
        self.add_polyline("crossbar", (14,38), (24,38), (34,38))
        self.relate("connect", "cup", "stem")
        self.relate("connect", "stem", "crossbar")
