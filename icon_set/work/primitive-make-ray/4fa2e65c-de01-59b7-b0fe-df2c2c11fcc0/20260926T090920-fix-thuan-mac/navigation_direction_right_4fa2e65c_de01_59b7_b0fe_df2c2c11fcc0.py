"""Navigation direction right (interface-essential), redrawn as one smooth U-turn arrow on SQUARE."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '4fa2e65c-de01-59b7-b0fe-df2c2c11fcc0'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__navigation-direction-right/20260926T085631Z-thuan-mac/reference/navigation direction right_4fa2e65c-de01-59b7-b0fe-df2c2c11fcc0.svg'
AUTHOR = "claude-opus-5-5"

class NavigationDirectionRight(Solo48):
    icon_id = 'navigation-direction-right'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('navigation', 'direction', 'right', 'interface-essential')

    def build(self):
        # Plan (review: one smooth curve): a U-turn arrow on SQUARE (6,6)-(42,42).
        # A short top stub runs into an exact r14 semicircle about (20,20); the
        # semicircle meets the straight lower shaft tangentially at (20,34),
        # and the shaft ends in a 45-degree head with 8-unit arms at (42,34).
        self.add_line('stub', (28, 6), (20, 6))
        self.add_arc('turn', (20, 6), (20, 34), radius_x=14, radius_y=14, large_arc=False, sweep=False)
        self.add_line('shaft', (20, 34), (42, 34))
        self.add_contour('path', 'stub', 'turn', 'shaft')
        self.add_polyline('head', (34, 26), (42, 34), (34, 42))
        self.relate('connect', 'path', 'head')
