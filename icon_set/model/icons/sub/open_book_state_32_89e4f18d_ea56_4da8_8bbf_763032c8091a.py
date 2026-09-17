"""Open Book: An open book shows two broad blank pages joined by a central vertical spine. Their upper and lower edges bow gently, meeting in central notches above and below.

Construction: Two curved page tops and bottoms meet at one central spine; no page marks added. Lucide book-open informs shared spine.
Keyshape: HRECT_XL; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '89e4f18d-ea56-4da8-8bbf-763032c8091a'
SOURCE_PATH = 'pictographic-primitives/state/book pages_89e4f18d-ea56-4da8-8bbf-763032c8091a.svg'
AUTHOR = 'gpt-6'


class OpenBookState32(Sub32):
    icon_id = 'open-book-state-32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives/shape'
    aliases = ()
    keywords = ('open', 'book', 'shows', 'broad', 'blank', 'pages', 'joined', 'central')

    def build(self):
        self.add_arc('top-left',(2,4),(16,8),radius_x=14,radius_y=4)
        self.add_arc('top-right',(16,8),(30,4),radius_x=14,radius_y=4)
        self.add_line('right',(30,4),(30,24))
        self.add_arc('bottom-right',(30,24),(16,28),radius_x=14,radius_y=4,sweep=False)
        self.add_arc('bottom-left',(16,28),(2,24),radius_x=14,radius_y=4,sweep=False)
        self.add_line('left',(2,24),(2,4))
        self.add_contour('pages','top-left','top-right','right','bottom-right','bottom-left','left',closed=True)
        self.add_line('spine',(16,8),(16,28))
        self.relate('connect','pages','spine')
