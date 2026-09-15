"""Remove the central fan rib; keep the mirrored pair of remaining ribs. Independent feedback revision; parent preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e42cbce0-9cff-57ad-9095-13c8d5b279a0'
SOURCE_PATH = 'pictographic-primitives/culture/batch-03/fan_e42cbce0-9cff-57ad-9095-13c8d5b279a0.svg'
AUTHOR = 'gpt-6'

class FoldingHandFan(Solo48):
    icon_id = 'folding-hand-fan'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'culture/objects'
    aliases = ()
    keywords = ('fan', 'folding fan', 'hand fan', 'japanese', 'asian', 'accessory', 'cooling', 'traditional')

    def build(self) -> None:
        """Symbol plan: Remove the central fan rib; keep the mirrored pair of remaining ribs. Reference: inspected current parent; no useful exact Lucide match selected."""
        p_4_19 = (4, 19)
        p_13_11 = (13, 11)
        p_24_8 = (24, 8)
        p_35_11 = (35, 11)
        p_44_19 = (44, 19)
        p_24_40 = (24, 40)
        self.add_arc('edge-left-outer', p_4_19, p_13_11, radius_x=26, radius_y=24, sweep=True, large_arc=False)
        self.add_arc('edge-left-inner', p_13_11, p_24_8, radius_x=26, radius_y=24, sweep=True, large_arc=False)
        self.add_arc('edge-right-inner', p_24_8, p_35_11, radius_x=26, radius_y=24, sweep=True, large_arc=False)
        self.add_arc('edge-right-outer', p_35_11, p_44_19, radius_x=26, radius_y=24, sweep=True, large_arc=False)
        self.add_line('right-rib', p_44_19, p_24_40)
        self.add_line('left-rib', p_24_40, p_4_19)
        self.add_line('rib-left', p_13_11, p_24_40)
        self.add_line('rib-right', p_35_11, p_24_40)
        self.add_contour('fan', 'edge-left-outer', 'edge-left-inner', 'edge-right-inner', 'edge-right-outer', 'right-rib', 'left-rib', closed=True)
        self.relate('connect', 'fan', 'rib-left')
        self.relate('connect', 'fan', 'rib-right')
        self.relate('connect', 'rib-left', 'rib-right')
