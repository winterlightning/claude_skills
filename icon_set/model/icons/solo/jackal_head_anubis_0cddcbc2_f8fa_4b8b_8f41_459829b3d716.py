'Jackal head anubis.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The VRECT_L visible envelope is (6, 2, 42, 46).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0cddcbc2-f8fa-4b8b-8f41-459829b3d716'
SOURCE_PATH = 'pictographic-primitives/culture/batch-04/sphinx_0cddcbc2-f8fa-4b8b-8f41-459829b3d716.svg'
AUTHOR = 'gpt-6'

class JackalHeadAnubis(Solo48):
    icon_id = 'jackal-head-anubis'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'culture'
    categories = ('culture', 'primitives')
    aliases = ()
    keywords = ('anubis', 'jackal', 'egyptian', 'god', 'mask', 'mythology', 'pharaoh', 'ancient')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_11_25 = (11, 25)
        p_11_4 = (11, 4)
        p_19_18 = (19, 18)
        p_29_18 = (29, 18)
        p_37_4 = (37, 4)
        p_37_25 = (37, 25)
        p_28_35 = (28, 35)
        p_28_38 = (28, 38)
        p_20_38 = (20, 38)
        p_20_35 = (20, 35)
        p_8_44 = (8, 44)
        p_14_44 = (14, 44)
        p_40_44 = (40, 44)
        p_34_44 = (34, 44)
        self.add_line('ears-left-1', p_11_25, p_11_4)
        self.add_line('ears-left-2', p_11_4, p_19_18)
        self.add_arc('brow', p_19_18, p_29_18, radius_x=10, radius_y=11, sweep=True, large_arc=False)
        self.add_line('ears-right-1', p_29_18, p_37_4)
        self.add_line('ears-right-2', p_37_4, p_37_25)
        self.add_arc('cheek-right', p_37_25, p_28_35, radius_x=9, radius_y=10, sweep=True, large_arc=False)
        self.add_line('muzzle-right', p_28_35, p_28_38)
        self.add_arc('chin', p_28_38, p_20_38, radius_x=4, radius_y=5, sweep=True, large_arc=False)
        self.add_line('muzzle-left', p_20_38, p_20_35)
        self.add_arc('cheek-left', p_20_35, p_11_25, radius_x=9, radius_y=10, sweep=True, large_arc=False)
        self.add_line('left-lappet-1', p_11_25, p_8_44)
        self.add_line('left-lappet-2', p_8_44, p_14_44)
        self.add_line('right-lappet-1', p_37_25, p_40_44)
        self.add_line('right-lappet-2', p_40_44, p_34_44)
        self.add_contour('head', 'ears-left-1', 'ears-left-2', 'brow', 'ears-right-1', 'ears-right-2', 'cheek-right', 'muzzle-right', 'chin', 'muzzle-left', 'cheek-left', closed=True)
        self.add_contour('left-lappet', 'left-lappet-1', 'left-lappet-2', closed=False)
        self.add_contour('right-lappet', 'right-lappet-1', 'right-lappet-2', closed=False)
        self.relate('connect', 'head', 'left-lappet')
        self.relate('connect', 'head', 'right-lappet')
