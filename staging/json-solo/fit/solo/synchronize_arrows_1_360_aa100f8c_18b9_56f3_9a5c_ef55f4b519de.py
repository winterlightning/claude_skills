"""Synchronize arrows 1 360 (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'aa100f8c-18b9-56f3-9a5c-ef55f4b519de'
SOURCE_PATH = 'icons-json/arrows/synchronize arrows 1 360_aa100f8c-18b9-56f3-9a5c-ef55f4b519de.json'
AUTHOR = 'json_to_solo'

class SynchronizeArrows1360Arrows(Solo48):
    icon_id = 'synchronize-arrows-1-360-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('synchronize', 'arrows')

    def build(self):
        self.add_line('e0', (17, 35), (11, 36))
        self.add_line('e1', (11, 36), (13, 42))
        self.add_line('e2', (35, 6), (37, 13))
        self.add_line('e3', (37, 13), (30, 13))
        self.add_arc('e4-1', (41, 19), (42, 24), radius_x=14)
        self.add_arc('e4-2', (42, 24), (11, 36), radius_x=18)
        self.add_arc('e5-1', (7, 29), (6, 24), radius_x=14)
        self.add_arc('e5-2', (6, 24), (37, 13), radius_x=18)
        self.add_contour('c0', 'e4-1', 'e4-2')
        self.add_contour('c1', 'e0', 'e1')
        self.add_contour('c2', 'e2', 'e3')
        self.add_contour('c3', 'e5-1', 'e5-2')
