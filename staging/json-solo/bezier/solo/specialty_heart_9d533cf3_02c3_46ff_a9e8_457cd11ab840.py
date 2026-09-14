"""Specialty heart (health), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('sym-e2', (31, 36), ((36.097, 31.541), (42, 24.094), (42, 17)))
        self.add_bezier('sym-e3', (42, 17), ((42, 16.755), (42, 16.245), (42, 16)))
        self.add_bezier('sym-e4', (42, 16), ((42, 15.926), (42, 16.074), (42, 16)))
        self.add_bezier('sym-e5', (42, 16), ((42, 10.927), (37.163, 6), (32, 6)))
        self.add_bezier('sym-e6', (32, 6), ((31.795, 6), (32.205, 6), (32, 6)))
        self.add_bezier('sym-e7', (32, 6), ((31.935, 6), (32.065, 6), (32, 6)))
        self.add_bezier('sym-e8', (32, 6), ((29.979, 6), (27.497, 6.683), (26, 8)))
        self.add_bezier('sym-e9', (26, 8), ((25.575, 8.376), (25.352, 9.55), (25, 10)))
        self.add_bezier('sym-e10', (25, 10), ((24.73, 10.344), (24.27, 10.656), (24, 11)))
        self.add_bezier('sym-e11', (24, 11), ((23.975, 10.972), (24.025, 10.028), (24, 10)))
        self.add_bezier('sym-e12', (24, 10), ((23.975, 10.028), (24.025, 10.972), (24, 11)))
        self.add_bezier('sym-e13', (24, 11), ((23.73, 10.656), (23.27, 10.344), (23, 10)))
        self.add_bezier('sym-e14', (23, 10), ((22.648, 9.55), (22.425, 8.376), (22, 8)))
        self.add_bezier('sym-e15', (22, 8), ((20.503, 6.683), (18.021, 6), (16, 6)))
        self.add_bezier('sym-e16', (16, 6), ((15.935, 6), (16.065, 6), (16, 6)))
        self.add_bezier('sym-e17', (16, 6), ((15.795, 6), (16.205, 6), (16, 6)))
        self.add_bezier('sym-e18', (16, 6), ((10.837, 6), (6, 10.927), (6, 16)))
        self.add_bezier('sym-e19', (6, 16), ((6, 16.074), (6, 15.926), (6, 16)))
        self.add_bezier('sym-e20', (6, 16), ((6, 16.245), (6, 16.755), (6, 17)))
        self.add_bezier('sym-e21', (6, 17), ((6, 24.094), (11.903, 31.541), (17, 36)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', closed=True)
