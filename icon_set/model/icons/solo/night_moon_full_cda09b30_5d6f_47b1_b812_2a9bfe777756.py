"""Night moon full (weather), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cda09b30-5d6f-47b1-b812-2a9bfe777756'
SOURCE_PATH = 'icons-json/weather/night moon full_cda09b30-5d6f-47b1-b812-2a9bfe777756.json'
AUTHOR = 'json_to_solo'

class NightMoonFull(Solo48):
    icon_id = 'night-moon-full'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'weather'
    aliases = ()
    keywords = ('night', 'moon', 'full', 'weather')

    def build(self):
        self.add_arc('e0-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e0-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_contour('e0', 'e0-top', 'e0-bottom', closed=True)
