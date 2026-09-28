"""Moved the lunar arc as one unit and shortened the lower stem.

Keyshape VRECT_L: visible bounds (6, 2, 42, 46).
Reference: moon: coherent lunar curve.
"""
# Independent repair of selene-astrological-symbol; parent preserved.
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '8d70aef7-a4a5-57c7-8ae8-a7af8092a967'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__selene-astrological-symbol/20260927T091411Z-thuan-mac-1/reference/astrology selene_8d70aef7-a4a5-57c7-8ae8-a7af8092a967.svg'
AUTHOR = 'gpt-6'

class SeleneAstrologicalSymbol(Solo48):
    icon_id = 'selene-astrological-symbol'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'culture'
    categories = ('culture', 'primitives')
    aliases = ()
    keywords = ('selene', 'astrology', 'moon', 'symbol', 'horoscope', 'glyph', 'lunar', 'goddess')

    # Symbol plan: retain the subject and shared attachment stations;
    # fit the current keyshape by adjusting the owning cap, base or repeat.
    # Revision plan: The rejected glyph had only a narrow right crescent. Restore the broad open lunar C and lower cross. Lucide moon informs the continuous lunar curve.
    # Revision plan: The rejected glyph had only a narrow right crescent. Restore the broad open lunar C and lower cross. Lucide moon informs the continuous lunar curve.
    # Revision plan: The rejected glyph had only a narrow right crescent. Restore the broad open lunar C and lower cross. Lucide moon informs the continuous lunar curve.
    # Revision plan: The rejected glyph had only a narrow right crescent. Restore the broad open lunar C and lower cross. Lucide moon informs the continuous lunar curve.
    # Revision plan: The rejected glyph had only a narrow right crescent. Restore the broad open lunar C and lower cross. Lucide moon informs the continuous lunar curve.
    def build(self):
        # Open lunar loop and the lower cross form one astrologic glyph.
        self.add_bezier('moon-top', (16, 8), ((30, 4), (40, 14), (40, 22)))
        self.add_bezier('moon-lower-right', (40, 22), ((40, 30), (32, 34), (24, 34)))
        self.add_bezier('moon-tail', (24, 34), ((21, 34), (18, 33), (16, 32)))
        self.add_contour('moon', 'moon-top', 'moon-lower-right', 'moon-tail')
        self.add_line('stem', (24, 34), (24, 44))
        self.add_line('crossbar', (18, 42), (30, 42))
        self.relate('connect', 'moon', 'stem')
        self.relate('connect', 'stem', 'crossbar')
