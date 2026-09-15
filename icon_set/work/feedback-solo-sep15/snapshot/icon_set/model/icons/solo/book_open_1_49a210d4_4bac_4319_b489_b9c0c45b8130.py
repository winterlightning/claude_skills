'Open book: equal pages share the spine; shorter text marks preserve clear margins on both sides.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '49a210d4-4bac-4319-b489-b9c0c45b8130'
SOURCE_PATH = 'pictographic-primitives/content/book open 1_49a210d4-4bac-4319-b489-b9c0c45b8130.svg'
AUTHOR = 'gpt-6'

class BookOpen1Content(Solo48):
    icon_id = 'book-open-1-content'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'content'
    aliases = ()
    keywords = ('book', 'open', 'content')

    def build(self) -> None:
        self.add_polyline('cover',(4,8),(24,13),(44,8),(44,35),(24,40),(4,35),closed=True)
        self.add_line('spine',(24,13),(24,40));self.relate('connect','spine','cover')
        self.add_line('left-text',(12,23),(16,24))
        self.add_line('right-text',(32,24),(36,23))
