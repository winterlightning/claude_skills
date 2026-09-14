"""Reduced both elliptical heights together; retained the left-facing opening.

Keyshape VRECT_L: visible bounds (6, 2, 42, 46).
Reference: moon: coherent outer and inner curves.
"""
# Independent repair of crescent-moon; parent preserved.
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1f947813-75bf-523b-bb36-5f6abbd3d57b'
SOURCE_PATH = 'pictographic-primitives/culture/batch-02/astrology moon_1f947813-75bf-523b-bb36-5f6abbd3d57b.svg'
AUTHOR = 'gpt-6'

class CrescentMoon(Solo48):
    icon_id = 'crescent-moon'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/culture'
    aliases = ()
    keywords = ('moon', 'crescent', 'lunar', 'night', 'astrology', 'symbol', 'sky', 'phase')

    # Symbol plan: retain the subject and shared attachment stations;
    # fit the current keyshape by adjusting the owning cap, base or repeat.
    def build(self) -> None:
        self.add_arc('outer', (8, 4), (8, 44), radius_x=32, radius_y=20, sweep=True)
        self.add_arc('inner', (8, 44), (8, 4), radius_x=17, radius_y=20, sweep=False)
        self.add_contour('crescent', 'outer', 'inner', closed=True)
