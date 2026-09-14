"""Oval (design), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '201b2f9d-9a10-514a-a362-42276721a1e0'
SOURCE_PATH = 'icons-json/design/oval_201b2f9d-9a10-514a-a362-42276721a1e0.json'
AUTHOR = 'json_to_solo'

class Oval201b2f9d(Solo48):
    icon_id = 'oval-201b2f9d'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('oval', 'design')

    def build(self):
        self.add_arc('sym-e1', (24, 40), (25, 40), radius_x=1)
        self.add_arc('sym-e2', (25, 40), (30, 39), radius_x=23, sweep=False)
        self.add_arc('sym-e3', (30, 39), (44, 24), radius_x=16, sweep=False)
        self.add_arc('sym-e6', (44, 24), (30, 9), radius_x=16, sweep=False)
        self.add_arc('sym-e7', (30, 9), (25, 8), radius_x=23, sweep=False)
        self.add_arc('sym-e8', (25, 8), (24, 8), radius_x=1)
        self.add_arc('sym-e11', (24, 8), (23, 8), radius_x=1)
        self.add_arc('sym-e12', (23, 8), (18, 9), radius_x=23, sweep=False)
        self.add_arc('sym-e13', (18, 9), (4, 24), radius_x=16, sweep=False)
        self.add_arc('sym-e16', (4, 24), (18, 39), radius_x=16, sweep=False)
        self.add_arc('sym-e17', (18, 39), (23, 40), radius_x=23, sweep=False)
        self.add_arc('sym-e18', (23, 40), (24, 40), radius_x=1)
        self.add_contour('sym-c0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e16', 'sym-e17', 'sym-e18', closed=True)
