"""Photo time lapse (photography), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e24a3ba0-192d-4a3a-8c1f-b6fa91c84ee7'
SOURCE_PATH = 'icons-json/photography/photo time lapse_e24a3ba0-192d-4a3a-8c1f-b6fa91c84ee7.json'
AUTHOR = 'json_to_solo'

class PhotoTimeLapsePhotography(Solo48):
    icon_id = 'photo-time-lapse-photography'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'photography'
    aliases = ()
    keywords = ('photo', 'time', 'lapse', 'photography')

    def build(self):
        self.add_line('e0', (24, 14), (24, 24))
        self.add_line('e1', (24, 25), (32, 32))
        self.add_arc('e2-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e2-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_arc('e3', (24, 24), (24, 25), radius_x=24, sweep=False)
        self.add_contour('c0', 'e0', 'e3', 'e1')
        self.add_contour('e2', 'e2-top', 'e2-bottom', closed=True)
