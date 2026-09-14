'Cat paw print.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The SQUARE visible envelope is (4, 4, 44, 44).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = None
SOURCE_PATH = 'icon_set/model/icons/solo/cat_paw_print.py'
AUTHOR = 'gpt-6'

class CatPawPrint(Solo48):
    icon_id = 'cat-paw-print'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ('feline paw print',)
    keywords = ('cat', 'paw', 'pet', 'kitten', 'footprint', 'animal')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_6_21 = (6, 21)
        p_16_6 = (16, 6)
        p_32_6 = (32, 6)
        p_42_21 = (42, 21)
        p_14_34 = (14, 34)
        p_34_34 = (34, 34)
        self.add_line('toe-0', p_6_21, p_6_21)
        self.add_line('toe-1', p_16_6, p_16_6)
        self.add_line('toe-2', p_32_6, p_32_6)
        self.add_line('toe-3', p_42_21, p_42_21)
        self.add_arc('pad-top', p_14_34, p_34_34, radius_x=10, radius_y=10, sweep=True, large_arc=False)
        self.add_arc('pad-base', p_34_34, p_14_34, radius_x=10, radius_y=8, sweep=True, large_arc=False)
        self.add_contour('pad', 'pad-top', 'pad-base', closed=True)
