"""Classical column beside an open book. SQUARE (2,2)-(46,46). Lucide book-open: two pages with spine. Capital retains inward volute curls; repeated spiral turns, fluting and text removed."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5dd33c32-a4a4-49c4-9f2f-9e1e0c52c018'
SOURCE_PATH = 'pictographic-primitives/culture/batch-02/mythology_5dd33c32-a4a4-49c4-9f2f-9e1e0c52c018.svg'


class ColumnWithOpenBook(Solo48):
    icon_id = 'column-with-open-book'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/culture"
    aliases = ()
    keywords = ('mythology', 'column', 'book', 'classical', 'greek', 'study', 'literature', 'architecture')

    def build(self) -> None:
        self.add_line('capital-top', (8,2), (28,2))
        self.add_arc('capital-right', (28,2), (28,14), radius_x=6)
        self.add_arc('capital-left', (8,14), (8,2), radius_x=6)
        self.add_arc('volute-left', (8,8), (8,14), radius_x=3)
        self.add_arc('volute-right', (28,14), (28,8), radius_x=3)
        self.add_contour('capital', 'volute-left','capital-left','capital-top','capital-right','volute-right')
        self.add_line('shaft', (8,22), (8,46))
        self.add_line('shaft-right', (16,22), (16,38))
        
        self.add_polyline('book', (22,26), (34,30), (46,26), (46,42), (34,46), (22,42), closed=True)
        self.add_line('spine', (34,30), (34,46))
        self.relate('connect', 'book', 'spine')
