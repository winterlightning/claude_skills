"""Book open idea (content), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f3ae031f-18d4-5ac4-b016-51186b90e93b'
SOURCE_PATH = 'icons-json/content/book open idea_f3ae031f-18d4-5ac4-b016-51186b90e93b.json'
AUTHOR = 'json_to_solo'

class BookOpenIdea(Solo48):
    icon_id = 'book-open-idea'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'content'
    aliases = ()
    keywords = ('book', 'open', 'idea', 'content')

    def build(self):
        self.add_line('sym-e0', (24, 6), (24, 10))
        self.add_line('sym-e1', (24, 42), (24, 22))
        self.add_line('sym-e2', (24, 22), (24, 22))
        self.add_line('sym-e3', (24, 22), (22, 19))
        self.add_arc('sym-e4', (22, 19), (11, 15), radius_x=16, sweep=False)
        self.add_arc('sym-e5', (11, 15), (9, 15), radius_x=36)
        self.add_line('sym-e6-1', (9, 15), (6, 16))
        self.add_arc('sym-e6-2', (6, 16), (6, 17), radius_x=1)
        self.add_line('sym-e9', (6, 17), (6, 35))
        self.add_line('sym-e10', (6, 35), (6, 36))
        self.add_arc('sym-e11', (6, 36), (10, 38), radius_x=3, sweep=False)
        self.add_arc('sym-e12', (10, 38), (20, 39), radius_x=26)
        self.add_arc('sym-e13', (20, 39), (24, 42), radius_x=26, sweep=False)
        self.add_arc('sym-e14', (24, 42), (28, 39), radius_x=25)
        self.add_arc('sym-e15', (28, 39), (38, 38), radius_x=26)
        self.add_arc('sym-e16', (38, 38), (42, 36), radius_x=3, sweep=False)
        self.add_arc('sym-e17', (42, 36), (42, 35), radius_x=37)
        self.add_line('sym-e18', (42, 35), (42, 17))
        self.add_arc('sym-e21-1', (42, 17), (42, 16), radius_x=1)
        self.add_line('sym-e21-2', (42, 16), (39, 15))
        self.add_arc('sym-e22', (39, 15), (37, 15), radius_x=36)
        self.add_arc('sym-e23', (37, 15), (26, 19), radius_x=16, sweep=False)
        self.add_line('sym-e24', (26, 19), (24, 22))
        self.add_line('sym-e25', (15, 7), (17, 9))
        self.add_line('sym-e26', (33, 7), (31, 9))
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6-1', 'sym-e6-2', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e21-1', 'sym-e21-2', 'sym-e22', 'sym-e23', 'sym-e24')
        self.add_contour('sym-c2', 'sym-e25')
        self.add_contour('sym-c3', 'sym-e26')
