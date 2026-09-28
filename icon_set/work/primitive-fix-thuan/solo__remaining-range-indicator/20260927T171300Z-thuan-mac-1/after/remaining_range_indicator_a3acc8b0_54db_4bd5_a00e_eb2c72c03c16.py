"""Remaining Range Indicator, re-authored from its reference on SOLO48."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'a3acc8b0-54db-4bd5-a00e-eb2c72c03c16'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__remaining-range-indicator/20260927T171300Z-thuan-mac-1/reference/e car battery driving length 1_a3acc8b0-54db-4bd5-a00e-eb2c72c03c16.svg'
AUTHOR = 'gpt-6'

class RemainingRangeIndicator(Solo48):
    icon_id = 'remaining-range-indicator'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    categories = ("transportation", "primitives")
    aliases = ()
    keywords = ('range', 'distance', 'remaining', 'battery', 'fuel', 'dashboard', 'electric car', 'kilometres')

    def build(self) -> None:
        # Distance left from a battery can, with the source numeral above.
        self.add_polyline('can',(30,30),(30,16),(34,16),(34,8),(44,8),(44,40),(30,40),closed=True)
        self.add_line('distance',(30,30),(14,30))
        self.add_polyline('arrowhead',(20,25),(14,30),(20,35))
        self.relate('connect','distance','can','arrowhead')
        self.add_line('end-bar',(4,24),(4,36))
        self.add_line('one',(6,8),(6,16))
        self.add_arc('zero-top',(15,12),(21,12),radius_x=3)
        self.add_arc('zero-bottom',(21,12),(15,12),radius_x=3)
        self.add_contour('zero','zero-top','zero-bottom',closed=True)
