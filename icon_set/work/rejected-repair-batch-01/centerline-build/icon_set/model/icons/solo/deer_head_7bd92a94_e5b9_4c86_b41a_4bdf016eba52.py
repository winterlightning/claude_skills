'Deer head.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The SQUARE visible envelope is (4, 4, 44, 44).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7bd92a94-e5b9-4c86-b41a-4bdf016eba52'
SOURCE_PATH = 'pictographic-primitives/animals/deer_7bd92a94-e5b9-4c86-b41a-4bdf016eba52.svg'
AUTHOR = 'gpt-6'

class DeerHead(Solo48):
    icon_id = 'deer-head'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ()
    keywords = ('deer', 'head', 'antlers', 'stag', 'face', 'muzzle', 'wildlife', 'buck')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_17_22 = (17, 22)
        p_31_22 = (31, 22)
        p_29_37 = (29, 37)
        p_19_37 = (19, 37)
        p_6_13 = (6, 13)
        p_6_6 = (6, 6)
        p_17_8 = (17, 8)
        p_42_13 = (42, 13)
        p_42_6 = (42, 6)
        p_31_8 = (31, 8)
        self.add_line('crown', p_17_22, p_31_22)
        self.add_line('cheek-right', p_31_22, p_29_37)
        self.add_arc('chin', p_29_37, p_19_37, radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_line('cheek-left', p_19_37, p_17_22)
        self.add_line('left-antler-1', p_17_22, p_6_13)
        self.add_line('left-antler-2', p_6_13, p_6_6)
        self.add_line('left-tine', p_6_13, p_17_8)
        self.add_line('right-antler-1', p_31_22, p_42_13)
        self.add_line('right-antler-2', p_42_13, p_42_6)
        self.add_line('right-tine', p_42_13, p_31_8)
        self.add_contour('head', 'crown', 'cheek-right', 'chin', 'cheek-left', closed=True)
        self.add_contour('left-antler', 'left-antler-1', 'left-antler-2', closed=False)
        self.add_contour('right-antler', 'right-antler-1', 'right-antler-2', closed=False)
        self.relate('connect', 'head', 'left-antler')
        self.relate('connect', 'left-antler', 'left-tine')
        self.relate('connect', 'head', 'right-antler')
        self.relate('connect', 'right-antler', 'right-tine')
