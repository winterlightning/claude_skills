'Open book: equal pages share the spine; shorter text marks preserve clear margins on both sides.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '710c81fd-6fdd-45a1-b7ed-cc8825ddf0d9'
SOURCE_PATH = 'icons-json/content/book open_710c81fd-6fdd-45a1-b7ed-cc8825ddf0d9.json'
AUTHOR = 'gpt-6'

class BookOpen710c81fd(Solo48):
    icon_id = 'book-open-710c81fd'
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
