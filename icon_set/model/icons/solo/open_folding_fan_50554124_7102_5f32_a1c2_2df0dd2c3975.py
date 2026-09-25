'Open folding fan.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The HRECT_L visible envelope is (2, 6, 46, 42).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '50554124-7102-5f32-a1c2-2df0dd2c3975'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-06/hand fan_50554124-7102-5f32-a1c2-2df0dd2c3975.svg'
AUTHOR = 'gpt-6'

class OpenFoldingFan(Solo48):
    icon_id = 'open-folding-fan'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('open', 'folding', 'fan')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_4_21 = (4, 21)
        p_24_8 = (24, 8)
        p_44_21 = (44, 21)
        p_24_35 = (24, 35)
        p_24_40 = (24, 40)
        self.add_arc('leaf-left', p_4_21, p_24_8, radius_x=20, radius_y=13, sweep=True, large_arc=False)
        self.add_arc('leaf-right', p_24_8, p_44_21, radius_x=20, radius_y=13, sweep=True, large_arc=False)
        self.add_line('edge-right', p_44_21, p_24_35)
        self.add_line('edge-left', p_24_35, p_4_21)
        self.add_line('rib', p_24_8, p_24_35)
        self.add_line('pivot', p_24_35, p_24_40)
        self.add_contour('leaf', 'leaf-left', 'leaf-right', 'edge-right', 'edge-left', closed=True)
        self.relate('connect', 'leaf', 'rib')
        self.relate('connect', 'pivot', 'leaf')
        self.relate('connect', 'pivot', 'rib')
