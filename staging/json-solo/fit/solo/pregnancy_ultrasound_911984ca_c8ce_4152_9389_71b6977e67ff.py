"""Pregnancy ultrasound (health), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '911984ca-c8ce-4152-9389-71b6977e67ff'
SOURCE_PATH = 'icons-json/health/pregnancy ultrasound_911984ca-c8ce-4152-9389-71b6977e67ff.json'
AUTHOR = 'json_to_solo'

class PregnancyUltrasoundHealth(Solo48):
    icon_id = 'pregnancy-ultrasound-health'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('pregnancy', 'ultrasound', 'health')

    def build(self):
        self.add_line('e0', (44, 29), (31, 8))
        self.add_line('e1', (18, 8), (4, 29))
        self.add_arc('e2-1', (31, 8), (19, 8), radius_x=12)
        self.add_line('e2-2', (19, 8), (18, 8))
        self.add_line('e3-1', (4, 29), (4, 31))
        self.add_arc('e3-2', (4, 31), (13, 37), radius_x=43, sweep=False)
        self.add_arc('e3-3', (13, 37), (24, 40), radius_x=22, sweep=False)
        self.add_line('e3-4', (24, 40), (31, 39))
        self.add_arc('e3-5', (31, 39), (37, 36), radius_x=33, sweep=False)
        self.add_arc('e3-6', (37, 36), (44, 31), radius_x=36, sweep=False)
        self.add_line('e3-7', (44, 31), (44, 29))
        self.add_contour('c0', 'e0', 'e2-1', 'e2-2', 'e1', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e3-5', 'e3-6', 'e3-7', closed=True)
