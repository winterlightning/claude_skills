"""Left (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9faff82a-8ae6-50ea-a8eb-8b1cf1da62fa'
SOURCE_PATH = 'icons-json/arrows/left_9faff82a-8ae6-50ea-a8eb-8b1cf1da62fa.json'
AUTHOR = 'json_to_solo'

class Left(Solo48):
    icon_id = 'left'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('left', 'arrows')

    def build(self):
        self.add_line('e0', (25, 6), (6, 24))
        self.add_line('e1', (6, 24), (25, 42))
        self.add_line('e2', (42, 6), (23, 24))
        self.add_line('e3', (23, 24), (42, 42))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2', 'e3')
