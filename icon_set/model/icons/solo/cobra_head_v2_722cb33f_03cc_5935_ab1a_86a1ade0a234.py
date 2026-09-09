"""Side-facing cobra head with flared hood and a single eye. VRECT_XL (5,2)-(43,46). Removed coil and tail clutter. No useful exact Lucide match; intentional profile asymmetry."""
# Variant of cobra-head; parent file remains unchanged.
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '722cb33f-03cc-5935-ab1a-86a1ade0a234'
SOURCE_PATH = 'pictographic-primitives/animals/cobra head side_722cb33f-03cc-5935-ab1a-86a1ade0a234.svg'
AUTHOR = 'gpt-6'

class CobraHeadVariant2(Solo48):
    icon_id = 'cobra-head-v2'
    variant_of = 'cobra-head'
    variant_label = 'Simple cobra head and hood'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('cobra', 'snake', 'hood', 'reptile', 'serpent', 'venom', 'head', 'profile')

    def build(self) -> None:
        # Right-facing cobra head and flared hood; no coil or tail clutter.
        # VRECT_XL extremes (5,2)-(43,46).
        self.add_line('neck-back',(16,46),(16,38))
        self.add_arc('hood-bottom',(16,38),(5,23),radius_x=11,radius_y=15)
        self.add_arc('hood-top',(5,23),(24,2),radius_x=19,radius_y=21)
        self.add_arc('crown',(24,2),(43,12),radius_x=19,radius_y=10)
        self.add_arc('snout',(43,12),(35,20),radius_x=8)
        self.add_line('jaw',(35,20),(29,20))
        self.add_arc('throat',(29,20),(23,26),radius_x=6,sweep=False)
        self.add_line('neck-front',(23,26),(29,46))
        self.add_line('base',(29,46),(16,46))
        self.add_contour('outline','neck-back','hood-bottom','hood-top','crown','snout','jaw','throat','neck-front','base',closed=True)
        self.add_dot('eye',(31,11))
