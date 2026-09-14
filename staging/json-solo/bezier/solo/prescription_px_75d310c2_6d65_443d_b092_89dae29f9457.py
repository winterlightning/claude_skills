"""Prescription px (health), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '75d310c2-6d65-443d-b092-89dae29f9457'
SOURCE_PATH = 'icons-json/health/prescription px_75d310c2-6d65-443d-b092-89dae29f9457.json'
AUTHOR = 'json_to_solo'

class PrescriptionPx75d310c2(Solo48):
    icon_id = 'prescription-px-75d310c2'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('prescription', 'px', 'health')

    def build(self):
        self.add_line('e0', (8, 37), (8, 4))
        self.add_line('e1', (8, 4), (21, 4))
        self.add_line('e2', (21, 21), (8, 21))
        self.add_line('e3', (21, 44), (31, 35))
        self.add_line('e4', (31, 35), (40, 44))
        self.add_line('e5', (40, 26), (31, 35))
        self.add_line('e6', (31, 35), (17, 21))
        self.add_bezier('e7', (21, 4), ((21.834, 4), (22.392, 4.264), (23.183, 4.527)), ((25.12, 5.155), (26.771, 6.255), (27.958, 8.055)), ((30.846, 12.436), (28.8, 18.609), (24.244, 20.445)), ((23.124, 20.9), (22.204, 21), (21, 21)))
        self.add_contour('c0', 'e0', 'e1', 'e7', 'e2')
        self.add_contour('c1', 'e3', 'e4')
        self.add_contour('c2', 'e5', 'e6')
        self.relate('connect', 'c1', 'c2')
