"""Content pen (content), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '482d7189-b00f-4779-a692-ad9073f2b65d'
SOURCE_PATH = 'icons-json/content/content pen_482d7189-b00f-4779-a692-ad9073f2b65d.json'
AUTHOR = 'json_to_solo'

class ContentPenContent(Solo48):
    icon_id = 'content-pen-content'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'content'
    aliases = ()
    keywords = ('content', 'pen')

    def build(self):
        self.add_line('e0', (6, 42), (9, 34))
        self.add_line('e1', (11, 31), (36, 6))
        self.add_line('e2', (15, 39), (6, 42))
        self.add_line('e3', (9, 34), (11, 31))
        self.add_arc('e4-1', (36, 6), (42, 12), radius_x=29)
        self.add_line('e4-2', (42, 12), (15, 39))
        self.add_contour('c0', 'e0', 'e3', 'e1', 'e4-1', 'e4-2', 'e2', closed=True)
