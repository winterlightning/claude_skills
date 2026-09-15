'Sitting penguin.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The VRECT_L visible envelope is (6, 2, 42, 46).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6673357d-4cc5-548b-a630-59b4a3dcce8b'
SOURCE_PATH = 'pictographic-primitives/animals/tux_6673357d-4cc5-548b-a630-59b4a3dcce8b.svg'
AUTHOR = 'gpt-6'

class SittingPenguin(Solo48):
    icon_id = 'sitting-penguin'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ()
    keywords = ('penguin', 'sitting', 'tux', 'linux', 'mascot', 'bird', 'flippers', 'antarctic')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_11_14 = (11, 14)
        p_37_14 = (37, 14)
        p_37_20 = (37, 20)
        p_34_33 = (34, 33)
        p_14_33 = (14, 33)
        p_11_20 = (11, 20)
        p_20_39 = (20, 39)
        p_14_44 = (14, 44)
        p_8_39 = (8, 39)
        p_40_39 = (40, 39)
        p_34_44 = (34, 44)
        p_28_39 = (28, 39)
        p_20_14 = (20, 14)
        p_28_14 = (28, 14)
        p_24_23 = (24, 23)
        self.add_arc('crown', p_11_14, p_37_14, radius_x=13, radius_y=10, sweep=True, large_arc=False)
        self.add_line('neck-right', p_37_14, p_37_20)
        self.add_arc('body-right', p_37_20, p_34_33, radius_x=25, radius_y=27, sweep=False, large_arc=False)
        self.add_arc('body-left', p_14_33, p_11_20, radius_x=25, radius_y=27, sweep=False, large_arc=False)
        self.add_line('neck-left', p_11_20, p_11_14)
        self.add_arc('left-foot-top-right', p_14_33, p_20_39, radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_arc('left-foot-bottom-right', p_20_39, p_14_44, radius_x=6, radius_y=5, sweep=True, large_arc=False)
        self.add_arc('left-foot-bottom-left', p_14_44, p_8_39, radius_x=6, radius_y=5, sweep=True, large_arc=False)
        self.add_arc('left-foot-top-left', p_8_39, p_14_33, radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_arc('right-foot-top-right', p_34_33, p_40_39, radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_arc('right-foot-bottom-right', p_40_39, p_34_44, radius_x=6, radius_y=5, sweep=True, large_arc=False)
        self.add_arc('right-foot-bottom-left', p_34_44, p_28_39, radius_x=6, radius_y=5, sweep=True, large_arc=False)
        self.add_arc('right-foot-top-left', p_28_39, p_34_33, radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_line('belly', p_20_39, p_28_39)
        self.add_line('eye-left', p_20_14, p_20_14)
        self.add_line('eye-right', p_28_14, p_28_14)
        self.add_line('beak', p_24_23, p_24_23)
        self.add_contour('body', 'body-left', 'neck-left', 'crown', 'neck-right', 'body-right', closed=False)
        self.add_contour('left-foot', 'left-foot-top-right', 'left-foot-bottom-right', 'left-foot-bottom-left', 'left-foot-top-left', closed=True)
        self.add_contour('right-foot', 'right-foot-top-right', 'right-foot-bottom-right', 'right-foot-bottom-left', 'right-foot-top-left', closed=True)
        self.relate('connect', 'body', 'left-foot')
        self.relate('connect', 'body', 'right-foot')
        self.relate('connect', 'belly', 'left-foot')
        self.relate('connect', 'belly', 'right-foot')
