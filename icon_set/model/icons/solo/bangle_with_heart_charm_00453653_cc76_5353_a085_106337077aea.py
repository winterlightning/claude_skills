'Bangle with heart charm.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The VRECT_L visible envelope is (6, 2, 42, 46).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '00453653-cc76-5353-a085-106337077aea'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-04/bracelet with heart_00453653-cc76-5353-a085-106337077aea.svg'
AUTHOR = 'gpt-6'

class BangleWithHeartCharm(Solo48):
    icon_id = 'bangle-with-heart-charm'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('bracelet', 'bangle', 'heart', 'charm', 'jewellery', 'jewelry', 'love', 'accessory')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_14_33 = (14, 33)
        p_8_21 = (8, 21)
        p_40_21 = (40, 21)
        p_34_33 = (34, 33)
        p_24_30 = (24, 30)
        p_24_44 = (24, 44)
        self.add_arc('band-left', p_14_33, p_8_21, radius_x=16, radius_y=17, sweep=True, large_arc=False)
        self.add_arc('band-top', p_8_21, p_40_21, radius_x=16, radius_y=17, sweep=True, large_arc=False)
        self.add_arc('band-right', p_40_21, p_34_33, radius_x=16, radius_y=17, sweep=True, large_arc=False)
        self.add_arc('charm-l', p_24_30, p_14_33, radius_x=5, radius_y=5, sweep=False, large_arc=False)
        self.add_line('charm-ls', p_14_33, p_24_44)
        self.add_line('charm-rs', p_24_44, p_34_33)
        self.add_arc('charm-r', p_34_33, p_24_30, radius_x=5, radius_y=5, sweep=False, large_arc=False)
        self.add_contour('band', 'band-left', 'band-top', 'band-right', closed=False)
        self.add_contour('charm', 'charm-l', 'charm-ls', 'charm-rs', 'charm-r', closed=True)
        self.relate('connect', 'band', 'charm')
