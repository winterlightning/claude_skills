"""Shortened cup tips and lower stem; retained the sickle cup and cross.

Keyshape VRECT_L: visible bounds (6, 2, 42, 46).
Reference: No useful exact match.
"""
# Independent repair of ceres-astrological-symbol; parent preserved.
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '79079df9-e96e-507d-97a5-a334e4f830fb'
SOURCE_PATH = 'pictographic-primitives/culture/batch-01/astrology ceres_79079df9-e96e-507d-97a5-a334e4f830fb.svg'
AUTHOR = 'gpt-6'

class CeresAstrologicalSymbol(Solo48):
    icon_id = 'ceres-astrological-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'culture'
    categories = ('culture', 'primitives')
    aliases = ()
    keywords = ('ceres', 'astrology', 'planet', 'sickle', 'symbol', 'asteroid', 'horoscope', 'glyph')

    # Symbol plan: retain the subject and shared attachment stations;
    # fit the current keyshape by adjusting the owning cap, base or repeat.
    def build(self) -> None:
        self.add_line('cup-left-tip', (8, 4), (8, 8))
        self.add_arc('cup-left', (8, 8), (24, 24), radius_x=16, sweep=False)
        self.add_arc('cup-right', (24, 24), (40, 8), radius_x=16, sweep=False)
        self.add_line('cup-right-tip', (40, 8), (40, 4))
        self.add_contour('cup', 'cup-left-tip', 'cup-left', 'cup-right', 'cup-right-tip')
        self.add_polyline('stem', (24, 24), (24, 38), (24, 44))
        self.add_polyline('crossbar', (14, 38), (24, 38), (34, 38))
        self.relate('connect', 'cup', 'stem')
        self.relate('connect', 'stem', 'crossbar')
