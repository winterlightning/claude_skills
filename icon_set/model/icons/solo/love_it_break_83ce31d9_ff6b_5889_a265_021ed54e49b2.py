"""Love it break (social), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '83ce31d9-ff6b-5889-a265-021ed54e49b2'
SOURCE_PATH = 'icons-json/social/love it break_83ce31d9-ff6b-5889-a265-021ed54e49b2.json'
AUTHOR = 'json_to_solo'

class LoveItBreak(Solo48):
    icon_id = 'love-it-break'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'social'
    aliases = ()
    keywords = ('love', 'it', 'break', 'social')

    def build(self):
        self.add_line('e0', (9, 27), (24, 40))
        self.add_line('e1', (24, 40), (38, 28))
        self.add_line('e2', (26, 12), (21, 17))
        self.add_line('e3', (21, 17), (28, 23))
        self.add_line('e4', (28, 23), (22, 28))
        self.add_arc('e5-1', (25, 13), (15, 8), radius_x=13, sweep=False)
        self.add_line('e5-2', (15, 8), (8, 10))
        self.add_arc('e5-3', (8, 10), (5, 13), radius_x=10, sweep=False)
        self.add_line('e5-4', (5, 13), (4, 17))
        self.add_arc('e5-5', (4, 17), (9, 27), radius_x=13, sweep=False)
        self.add_arc('e6-1', (38, 28), (44, 18), radius_x=14, sweep=False)
        self.add_arc('e6-2', (44, 18), (34, 8), radius_x=10, sweep=False)
        self.add_arc('e6-3', (34, 8), (26, 12), radius_x=10, sweep=False)
        self.add_arc('e7', (22, 28), (24, 33), radius_x=6, sweep=False)
        self.add_contour('c0', 'e5-1', 'e5-2', 'e5-3', 'e5-4', 'e5-5', 'e0', 'e1', 'e6-1', 'e6-2', 'e6-3', 'e2', 'e3', 'e4', 'e7')
