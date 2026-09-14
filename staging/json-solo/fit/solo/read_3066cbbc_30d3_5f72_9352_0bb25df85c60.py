"""Read (emails), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3066cbbc-30d3-5f72-9352-0bb25df85c60'
SOURCE_PATH = 'icons-json/emails/read_3066cbbc-30d3-5f72-9352-0bb25df85c60.json'
AUTHOR = 'json_to_solo'

class ReadEmails(Solo48):
    icon_id = 'read-emails'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'emails'
    aliases = ()
    keywords = ('read', 'emails')

    def build(self):
        self.add_line('e0', (33, 28), (31, 30))
        self.add_line('e1-1', (34, 39), (26, 42))
        self.add_line('e1-2', (26, 42), (24, 42))
        self.add_arc('e1-3', (24, 42), (6, 24), radius_x=18)
        self.add_arc('e1-4', (6, 24), (24, 6), radius_x=18)
        self.add_line('e1-5', (24, 6), (30, 7))
        self.add_arc('e1-6', (30, 7), (39, 14), radius_x=19)
        self.add_arc('e1-7', (39, 14), (42, 23), radius_x=18)
        self.add_line('e1-8', (42, 23), (42, 25))
        self.add_arc('e1-9', (42, 25), (41, 30), radius_x=15)
        self.add_arc('e1-10', (41, 30), (39, 33), radius_x=8)
        self.add_arc('e1-11', (39, 33), (33, 28), radius_x=4)
        self.add_arc('e2-1', (31, 30), (19, 32), radius_x=9)
        self.add_arc('e2-2', (19, 32), (15, 21), radius_x=9)
        self.add_arc('e2-3', (15, 21), (27, 15), radius_x=9)
        self.add_arc('e2-4', (27, 15), (33, 28), radius_x=11)
        self.add_contour('c0', 'e1-1', 'e1-2', 'e1-3', 'e1-4', 'e1-5', 'e1-6', 'e1-7', 'e1-8', 'e1-9', 'e1-10', 'e1-11')
        self.add_contour('c1', 'e2-1', 'e2-2', 'e2-3', 'e2-4', 'e0', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c1', 'c0')
