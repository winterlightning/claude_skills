"""Connector to another page (outdoors), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '04a89f3f-0b74-491b-bdd0-032abf7a2fff'
SOURCE_PATH = 'icons-json/outdoors/connector to another page_04a89f3f-0b74-491b-bdd0-032abf7a2fff.json'
AUTHOR = 'json_to_solo'

class ConnectorToAnotherPageOutdoors(Solo48):
    icon_id = 'connector-to-another-page-outdoors'
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
        self.add_line('e3', (4, 21), (4, 8))
        self.add_line('e4', (4, 8), (44, 8))
        self.add_bezier('e5', (44, 21), ((43.964, 21.101), (43.927, 21.676), (43.891, 21.768)), ((43.673, 22.072), (43.282, 21.739), (43, 22)))
        self.add_bezier('e6', (4, 22), ((4, 21.722), (4, 21.278), (4, 21)))
        self.add_contour('c0', 'e0', 'e5', 'e1', 'e2', 'e6', 'e3', 'e4', closed=True)
