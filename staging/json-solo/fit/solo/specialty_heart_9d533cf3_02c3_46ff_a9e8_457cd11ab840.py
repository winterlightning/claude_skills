"""Specialty heart (health), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9d533cf3-02c3-46ff-a9e8-457cd11ab840'
SOURCE_PATH = 'icons-json/health/specialty heart_9d533cf3-02c3-46ff-a9e8-457cd11ab840.json'
AUTHOR = 'json_to_solo'

class SpecialtyHeartHealth(Solo48):
    icon_id = 'specialty-heart-health'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('specialty', 'heart', 'health')

    def build(self):
        self.add_line('sym-e0', (17, 36), (24, 42))
        self.add_line('sym-e1', (24, 42), (31, 36))
        self.add_arc('sym-e2', (31, 36), (42, 17), radius_x=30, sweep=False)
        self.add_line('sym-e3', (42, 17), (42, 16))
        self.add_arc('sym-e5', (42, 16), (32, 6), radius_x=10, sweep=False)
        self.add_line('sym-e8', (32, 6), (26, 8))
        self.add_arc('sym-e9', (26, 8), (25, 10), radius_x=9, sweep=False)
        self.add_line('sym-e10', (25, 10), (24, 11))
        self.add_arc('sym-e11', (24, 11), (24, 10), radius_x=30)
        self.add_arc('sym-e12', (24, 10), (24, 11), radius_x=14, sweep=False)
        self.add_line('sym-e13', (24, 11), (23, 10))
        self.add_line('sym-e14', (23, 10), (22, 8))
        self.add_line('sym-e15', (22, 8), (16, 6))
        self.add_arc('sym-e18', (16, 6), (6, 16), radius_x=10, sweep=False)
        self.add_line('sym-e20', (6, 16), (6, 17))
        self.add_arc('sym-e21', (6, 17), (17, 36), radius_x=30, sweep=False)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e5', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e18', 'sym-e20', 'sym-e21', closed=True)
