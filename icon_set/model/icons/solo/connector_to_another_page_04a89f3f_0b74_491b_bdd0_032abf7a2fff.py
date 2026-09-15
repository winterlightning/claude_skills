"""Connector to another page (outdoors), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '04a89f3f-0b74-491b-bdd0-032abf7a2fff'
SOURCE_PATH = 'icons-json/outdoors/connector to another page_04a89f3f-0b74-491b-bdd0-032abf7a2fff.json'
AUTHOR = 'gpt-6'

class ConnectorToAnotherPage(Solo48):
    icon_id = 'connector-to-another-page'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    aliases = ()
    keywords = ('connector', 'to', 'another', 'page', 'outdoors')

    def build(self):
        self.add_line('e0', (44, 8), (44, 21))
        self.add_line('e1', (43, 22), (24, 40))
        self.add_line('e2', (24, 40), (4, 22))
        self.add_line('e4', (4, 8), (44, 8))
        self.add_arc('e5', (44, 21), (43, 22), radius_x=1, radius_y=1, large_arc=False, sweep=True)
        self.add_line('e6', (4, 22), (4, 8))
        self.add_contour('c0', 'e0', 'e5', 'e1', 'e2', 'e6', 'e4', closed=True)
