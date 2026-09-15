'Book idea: preserve curved open pages and a centred inspiration ray; omit crowded short side rays.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f3ae031f-18d4-5ac4-b016-51186b90e93b'
SOURCE_PATH = 'pictographic-primitives/content/book open idea_f3ae031f-18d4-5ac4-b016-51186b90e93b.svg'
AUTHOR = 'gpt-6'

class BookOpenIdea(Solo48):
    icon_id = 'book-open-idea'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'content'
    aliases = ()
    keywords = ('book', 'open', 'idea', 'content')

    def build(self) -> None:
        self.add_bezier('top-left',(6,19),((12,17),(19,18),(24,24)))
        self.add_bezier('top-right',(24,24),((29,18),(36,17),(42,19)))
        self.add_line('right',(42,19),(42,38))
        self.add_bezier('bottom-right',(42,38),((35,36),(28,38),(24,42)))
        self.add_bezier('bottom-left',(24,42),((20,38),(13,36),(6,38)))
        self.add_line('left',(6,38),(6,19))
        self.add_contour('book','top-left','top-right','right','bottom-right','bottom-left','left',closed=True)
        self.add_line('spine',(24,24),(24,42));self.relate('connect','book','spine')
        self.add_line('idea',(24,6),(24,10))
