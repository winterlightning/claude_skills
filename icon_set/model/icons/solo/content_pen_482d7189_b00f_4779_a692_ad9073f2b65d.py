"""Content pen (content), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '482d7189-b00f-4779-a692-ad9073f2b65d'
SOURCE_PATH = 'icons-json/content/content pen_482d7189-b00f-4779-a692-ad9073f2b65d.json'
AUTHOR = 'json_to_solo'

class ContentPen(Solo48):
    icon_id = 'content-pen'
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
        self.add_bezier('e3', (9, 34), ((9.36, 33.092), (10.313, 31.687), (11, 31)))
        self.add_bezier('e4', (36, 6), ((37.546, 7.399), (39.382, 8.847), (40.748, 10.426)), ((40.966, 10.676), (42, 11.964), (42, 12.161)), ((42, 12.164), (42, 12.167), (42, 12.169)), ((42, 12.382), (40.904, 13.724), (40.625, 14.01)), ((39.046, 15.614), (37.41, 17.168), (35.823, 18.755)), ((31.257, 23.321), (26.635, 27.845), (22.045, 32.386)), ((20.146, 34.26), (17.414, 38.125), (15, 39)))
        self.add_contour('c0', 'e0', 'e3', 'e1', 'e4', 'e2', closed=True)
