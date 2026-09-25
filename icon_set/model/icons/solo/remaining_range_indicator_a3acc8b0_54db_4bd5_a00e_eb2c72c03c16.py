"""Remaining Range Indicator, re-authored from its reference on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a3acc8b0-54db-4bd5-a00e-eb2c72c03c16'
SOURCE_PATH = 'pictographic-primitives/transportation/e car battery driving length 1_a3acc8b0-54db-4bd5-a00e-eb2c72c03c16.svg'
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
        # Current contract centerline extremes: (6,8)-(42,40).
        # Can, directional distance shaft, and its terminal bar form a functional range diagram.
        self.add_polyline('can',(30,28),(30,16),(34,16),(34,8),(44,8),(44,16),(44,16),(44,40),(30,40),closed=True)
        self.add_line('distance',(30,28),(14,28))
        self.relate('connect','distance','can')
        self.add_polyline('arrowhead',(20,22),(14,28),(20,34))
        self.relate('connect','distance','arrowhead')
        self.add_line('end-bar',(4,20),(4,36))
