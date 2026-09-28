'Book idea: preserve curved open pages and a centred inspiration ray; omit crowded short side rays.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "f3ae031f-18d4-5ac4-b016-51186b90e93b"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__book-open-idea/20260926T085631Z-thuan-mac/reference/book open idea_f3ae031f-18d4-5ac4-b016-51186b90e93b.svg"
AUTHOR = "claude-opus-5-5"

class BookOpenIdea(Solo48):
    icon_id = 'book-open-idea'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'content'
    categories = ('primitives', 'content')
    aliases = ()
    keywords = ('book', 'open', 'idea', 'content')

    def build(self) -> None:
        # Symbol plan (SQUARE 6..42), mirrored about x24: open book with its top
        # edges from (6,21)/(42,21) dipping to the spine at (24,24), pages to y38,
        # bottom edges dipping to (24,42). Three light rays above: a vertical
        # centre ray (24,6)-(24,10) and two 45-degree rays (10,7)-(13,10) and
        # (38,7)-(35,10) pointing at the book, each at least 8 from the others
        # and from the book.
        self.add_bezier('top-left', (6, 21), ((12, 19), (19, 19), (24, 24)))
        self.add_bezier('top-right', (24, 24), ((29, 19), (36, 19), (42, 21)))
        self.add_line('right', (42, 21), (42, 38))
        self.add_bezier('bottom-right', (42, 38), ((35, 36), (28, 38), (24, 42)))
        self.add_bezier('bottom-left', (24, 42), ((20, 38), (13, 36), (6, 38)))
        self.add_line('left', (6, 38), (6, 21))
        self.add_contour('book', 'top-left', 'top-right', 'right', 'bottom-right', 'bottom-left', 'left', closed=True)
        self.add_line('spine', (24, 24), (24, 42)); self.relate('connect', 'book', 'spine')
        self.add_line('idea', (24, 6), (24, 10))
        self.add_line('ray-left', (10, 7), (13, 10))
        self.add_line('ray-right', (38, 7), (35, 10))
