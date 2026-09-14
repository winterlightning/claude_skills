'Classical head with book.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The SQUARE visible envelope is (4, 4, 44, 44).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8cdb2a8f-2d94-4ed2-9762-9b3c6ee9478d'
SOURCE_PATH = 'pictographic-primitives/culture/batch-02/greek mythology_8cdb2a8f-2d94-4ed2-9762-9b3c6ee9478d.svg'
AUTHOR = 'gpt-6'

class ClassicalHeadWithBook(Solo48):
    icon_id = 'classical-head-with-book'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/culture'
    aliases = ()
    keywords = ('mythology', 'greek', 'classical', 'book', 'reading', 'philosophy', 'study', 'literature')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_11_13 = (11, 13)
        p_31_13 = (31, 13)
        p_27_18 = (27, 18)
        p_6_21 = (6, 21)
        p_11_21 = (11, 21)
        p_11_26 = (11, 26)
        p_13_26 = (13, 26)
        p_13_29 = (13, 29)
        p_11_34 = (11, 34)
        p_6_42 = (6, 42)
        p_22_26 = (22, 26)
        p_32_29 = (32, 29)
        p_42_26 = (42, 26)
        p_42_39 = (42, 39)
        p_32_42 = (32, 42)
        p_22_39 = (22, 39)
        self.add_arc('crown', p_11_13, p_31_13, radius_x=10, radius_y=7, sweep=True, large_arc=False)
        self.add_arc('back-head', p_31_13, p_27_18, radius_x=11, radius_y=11, sweep=True, large_arc=False)
        self.add_line('face-1', p_11_13, p_6_21)
        self.add_line('face-2', p_6_21, p_11_21)
        self.add_line('face-3', p_11_21, p_11_26)
        self.add_line('face-4', p_11_26, p_13_26)
        self.add_line('face-5', p_13_26, p_13_29)
        self.add_arc('neck', p_13_29, p_11_34, radius_x=2, radius_y=5, sweep=True, large_arc=False)
        self.add_arc('shoulder', p_11_34, p_6_42, radius_x=10, radius_y=10, sweep=True, large_arc=False)
        self.add_line('book-1', p_22_26, p_32_29)
        self.add_line('book-2', p_32_29, p_42_26)
        self.add_line('book-3', p_42_26, p_42_39)
        self.add_line('book-4', p_42_39, p_32_42)
        self.add_line('book-5', p_32_42, p_22_39)
        self.add_line('book-6', p_22_39, p_22_26)
        self.add_line('spine', p_32_29, p_32_42)
        self.add_contour('front', 'face-1', 'face-2', 'face-3', 'face-4', 'face-5', 'neck', 'shoulder', closed=False)
        self.add_contour('book', 'book-1', 'book-2', 'book-3', 'book-4', 'book-5', 'book-6', closed=True)
        self.relate('connect', 'crown', 'front')
        self.relate('connect', 'crown', 'back-head')
        self.relate('connect', 'book', 'spine')
