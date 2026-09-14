'Moose head.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The SQUARE visible envelope is (4, 4, 44, 44).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3c797901-4d4a-4250-bcdf-fd815047ab51'
SOURCE_PATH = 'pictographic-primitives/culture/batch-05/moose_3c797901-4d4a-4250-bcdf-fd815047ab51.svg'
AUTHOR = 'gpt-6'

class MooseHead(Solo48):
    icon_id = 'moose-head'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/culture'
    aliases = ()
    keywords = ('moose', 'elk', 'antlers', 'animal', 'wildlife', 'nordic', 'head', 'hunting')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_6_6 = (6, 6)
        p_6_13 = (6, 13)
        p_11_17 = (11, 17)
        p_14_17 = (14, 17)
        p_21_17 = (21, 17)
        p_27_17 = (27, 17)
        p_34_17 = (34, 17)
        p_37_17 = (37, 17)
        p_42_13 = (42, 13)
        p_42_6 = (42, 6)
        p_14_8 = (14, 8)
        p_34_8 = (34, 8)
        p_35_26 = (35, 26)
        p_29_35 = (29, 35)
        p_26_34 = (26, 34)
        p_26_42 = (26, 42)
        p_13_32 = (13, 32)
        self.add_line('antler-left-upright', p_6_6, p_6_13)
        self.add_arc('antler-left-bend', p_6_13, p_11_17, radius_x=5, radius_y=5, sweep=False, large_arc=False)
        self.add_line('antler-beam-1', p_11_17, p_14_17)
        self.add_line('antler-beam-2', p_14_17, p_21_17)
        self.add_line('antler-beam-3', p_21_17, p_27_17)
        self.add_line('antler-beam-4', p_27_17, p_34_17)
        self.add_line('antler-beam-5', p_34_17, p_37_17)
        self.add_arc('antler-right-bend', p_37_17, p_42_13, radius_x=5, radius_y=5, sweep=False, large_arc=False)
        self.add_line('antler-right-upright', p_42_13, p_42_6)
        self.add_line('tine-left', p_14_17, p_14_8)
        self.add_line('tine-right', p_34_17, p_34_8)
        self.add_line('forehead', p_27_17, p_35_26)
        self.add_arc('nose', p_35_26, p_29_35, radius_x=7, radius_y=7, sweep=True, large_arc=False)
        self.add_line('muzzle-under', p_29_35, p_26_34)
        self.add_line('neck', p_26_34, p_26_42)
        self.add_arc('throat', p_26_42, p_13_32, radius_x=13, radius_y=10, sweep=True, large_arc=False)
        self.add_line('head-back', p_13_32, p_21_17)
        self.add_contour('antlers', 'antler-left-upright', 'antler-left-bend', 'antler-beam-1', 'antler-beam-2', 'antler-beam-3', 'antler-beam-4', 'antler-beam-5', 'antler-right-bend', 'antler-right-upright', closed=False)
        self.add_contour('head', 'forehead', 'nose', 'muzzle-under', 'neck', 'throat', 'head-back', closed=False)
        self.relate('connect', 'antlers', 'head')
        self.relate('connect', 'antlers', 'tine-left')
        self.relate('connect', 'antlers', 'tine-right')
