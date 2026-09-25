'Trilobite fossil.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The VRECT_L visible envelope is (6, 2, 42, 46).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7ba30cb2-a7ee-5783-ac87-e8a711683857'
SOURCE_PATH = 'pictographic-primitives/culture/batch-07/trilobite fossil shell_7ba30cb2-a7ee-5783-ac87-e8a711683857.svg'
AUTHOR = 'gpt-6'

class TrilobiteFossil(Solo48):
    icon_id = 'trilobite-fossil'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'culture'
    aliases = ()
    keywords = ('trilobite', 'fossil', 'prehistoric', 'palaeontology', 'shell', 'arthropod', 'ancient', 'museum')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_8_21 = (8, 21)
        p_24_4 = (24, 4)
        p_40_21 = (40, 21)
        p_35_21 = (35, 21)
        p_13_21 = (13, 21)
        p_32_29 = (32, 29)
        p_29_37 = (29, 37)
        p_24_44 = (24, 44)
        p_19_37 = (19, 37)
        p_16_29 = (16, 29)
        p_10_33 = (10, 33)
        p_38_33 = (38, 33)
        self.add_arc('head-left', p_8_21, p_24_4, radius_x=16, radius_y=17, sweep=True, large_arc=False)
        self.add_arc('head-right', p_24_4, p_40_21, radius_x=16, radius_y=17, sweep=True, large_arc=False)
        self.add_line('head-base-right', p_40_21, p_35_21)
        self.add_line('head-base-middle', p_35_21, p_13_21)
        self.add_line('head-base-left', p_13_21, p_8_21)
        self.add_line('body-r1', p_35_21, p_32_29)
        self.add_line('body-r2', p_32_29, p_29_37)
        self.add_arc('tail-right', p_29_37, p_24_44, radius_x=5, radius_y=7, sweep=True, large_arc=False)
        self.add_arc('tail-left', p_24_44, p_19_37, radius_x=5, radius_y=7, sweep=True, large_arc=False)
        self.add_line('body-l2', p_19_37, p_16_29)
        self.add_line('body-l1', p_16_29, p_13_21)
        self.add_line('segment-top', p_16_29, p_32_29)
        self.add_line('segment-bottom', p_19_37, p_29_37)
        self.add_line('leg-left', p_16_29, p_10_33)
        self.add_line('leg-right', p_32_29, p_38_33)
        self.add_contour('head', 'head-left', 'head-right', 'head-base-right', 'head-base-middle', 'head-base-left', closed=True)
        self.add_contour('body', 'body-r1', 'body-r2', 'tail-right', 'tail-left', 'body-l2', 'body-l1', closed=False)
        self.relate('connect', 'head', 'body')
        self.relate('connect', 'body', 'segment-top')
        self.relate('connect', 'body', 'segment-bottom')
        self.relate('connect', 'body', 'leg-left')
        self.relate('connect', 'segment-top', 'leg-left')
        self.relate('connect', 'body', 'leg-right')
        self.relate('connect', 'segment-top', 'leg-right')
