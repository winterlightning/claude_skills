"""Adjusted the two opposed elliptical bowls; retained the cross between them.

Keyshape VRECT_L: visible bounds (6, 2, 42, 46).
Reference: No useful exact match.
"""
# Independent repair of proserpine-astrological-symbol; parent preserved.
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7f8f9ab3-5fbb-5721-8ab4-02363d3861f3'
SOURCE_PATH = 'pictographic-primitives/culture/batch-06/astrology proserpine_7f8f9ab3-5fbb-5721-8ab4-02363d3861f3.svg'
AUTHOR = 'gpt-6'

class ProserpineAstrologicalSymbol(Solo48):
    icon_id = 'proserpine-astrological-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'culture'
    categories = ('culture', 'primitives')
    aliases = ()
    keywords = ('proserpine', 'astrology', 'planet', 'symbol', 'horoscope', 'glyph', 'persephone', 'asteroid')

    # Symbol plan: retain the subject and shared attachment stations;
    # fit the current keyshape by adjusting the owning cap, base or repeat.
    def build(self) -> None:
        self.add_arc('bowl-left', (8, 4), (24, 18), radius_x=16, radius_y=14, sweep=False)
        self.add_arc('bowl-right', (24, 18), (40, 4), radius_x=16, radius_y=14, sweep=False)
        self.add_contour('bowl', 'bowl-left', 'bowl-right')
        self.add_polyline('stem', (24, 18), (24, 26), (24, 34))
        self.add_polyline('crossbar', (16, 26), (24, 26), (32, 26))
        self.add_arc('dome-left', (8, 44), (24, 34), radius_x=16, radius_y=10)
        self.add_arc('dome-right', (24, 34), (40, 44), radius_x=16, radius_y=10)
        self.add_contour('dome', 'dome-left', 'dome-right')
        self.relate('connect', 'bowl', 'stem')
        self.relate('connect', 'stem', 'crossbar')
        self.relate('connect', 'stem', 'dome')
