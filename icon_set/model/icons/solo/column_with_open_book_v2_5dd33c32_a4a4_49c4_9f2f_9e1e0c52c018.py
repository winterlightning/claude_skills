# Variant of column-with-open-book; parent file remains unchanged.
"""Classical column and open book, with simplified capital and wider separation. SQUARE visible bounds (4,4)-(44,44). Lucide book-open informed the shared spine."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5dd33c32-a4a4-49c4-9f2f-9e1e0c52c018'
SOURCE_PATH = 'pictographic-primitives/culture/batch-02/mythology_5dd33c32-a4a4-49c4-9f2f-9e1e0c52c018.svg'
AUTHOR = 'gpt-6'

class ColumnWithOpenBookVariant2(Solo48):
    icon_id = 'column-with-open-book-v2'
    variant_of = 'column-with-open-book'
    variant_label = 'Roomier spacing — review 02'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/culture'
    aliases = ()
    keywords = ('mythology', 'column', 'book', 'classical', 'greek', 'study', 'literature', 'architecture')

    def build(self) -> None:
        self.add_arc('capital-left',(10,14),(10,6),radius_x=4)
        self.add_line('capital-top',(10,6),(18,6))
        self.add_arc('capital-right',(18,6),(18,14),radius_x=4)
        self.add_contour('capital','capital-left','capital-top','capital-right')
        self.add_line('shaft',(10,23),(10,42))
        self.add_line('shaft-right',(18,23),(18,42))
        self.add_polyline('book',(26,26),(34,30),(42,26),(42,38),(34,42),(26,38),closed=True)
        self.add_line('spine',(34,30),(34,42))
        self.relate('connect','book','spine')
