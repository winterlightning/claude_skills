"""Air pollution fire (_uncategorized_01), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bab5b5ab-20b1-4dd5-9adc-c0506955e155'
SOURCE_PATH = 'icons-json/_uncategorized_01/air pollution fire_bab5b5ab-20b1-4dd5-9adc-c0506955e155.json'
AUTHOR = 'json_to_solo'

class AirPollutionFireUncategorized01(Solo48):
    icon_id = 'air-pollution-fire-uncategorized-01'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_01'
    aliases = ()
    keywords = ('air', 'pollution', 'fire', '_uncategorized_01')

    def build(self):
        self.add_line('e0', (40, 4), (8, 44))
        self.add_contour('c0', 'e0')
