'Column with open book.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The SQUARE visible envelope is (4, 4, 44, 44).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5dd33c32-a4a4-49c4-9f2f-9e1e0c52c018'
SOURCE_PATH = 'pictographic-primitives/culture/batch-02/mythology_5dd33c32-a4a4-49c4-9f2f-9e1e0c52c018.svg'
AUTHOR = 'gpt-6'

class ColumnWithOpenBook(Solo48):
    icon_id = 'column-with-open-book'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/culture'
    aliases = ()
    keywords = ('mythology', 'column', 'book', 'classical', 'greek', 'study', 'literature', 'architecture')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_11_6 = (11, 6)
        p_27_6 = (27, 6)
        p_27_16 = (27, 16)
        p_11_16 = (11, 16)
        p_11_25 = (11, 25)
        p_11_42 = (11, 42)
        p_22_26 = (22, 26)
        p_32_29 = (32, 29)
        p_42_26 = (42, 26)
        p_42_39 = (42, 39)
        p_32_42 = (32, 42)
        p_22_39 = (22, 39)
        self.add_line('capital-top', p_11_6, p_27_6)
        self.add_arc('capital-right', p_27_6, p_27_16, radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_arc('capital-left', p_11_16, p_11_6, radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_line('shaft', p_11_25, p_11_42)
        self.add_line('book-1', p_22_26, p_32_29)
        self.add_line('book-2', p_32_29, p_42_26)
        self.add_line('book-3', p_42_26, p_42_39)
        self.add_line('book-4', p_42_39, p_32_42)
        self.add_line('book-5', p_32_42, p_22_39)
        self.add_line('book-6', p_22_39, p_22_26)
        self.add_line('spine', p_32_29, p_32_42)
        self.add_contour('book', 'book-1', 'book-2', 'book-3', 'book-4', 'book-5', 'book-6', closed=True)
        self.add_contour('capital', 'capital-left', 'capital-top', 'capital-right', closed=False)
        self.relate('connect', 'book', 'spine')
