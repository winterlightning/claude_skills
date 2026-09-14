"""Psychiatry (health), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f0d4e8d8-2e3e-47b4-82f6-85f8457f25af'
SOURCE_PATH = 'icons-json/health/psychiatry_f0d4e8d8-2e3e-47b4-82f6-85f8457f25af.json'
AUTHOR = 'json_to_solo'

class PsychiatryHealth(Solo48):
    icon_id = 'psychiatry-health'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('psychiatry', 'health')

    def build(self):
        self.add_line('sym-e0', (20, 8), (24, 8))
        self.add_line('sym-e1', (24, 8), (28, 8))
        self.add_line('sym-e2', (24, 40), (24, 25))
        self.add_line('sym-e3', (24, 25), (24, 8))
        self.add_line('sym-e4', (28, 40), (24, 40))
        self.add_line('sym-e5', (24, 40), (20, 40))
        self.add_bezier('sym-e6', (44, 8), ((43.3, 8), (42.7, 8), (42, 8)))
        self.add_bezier('sym-e7', (42, 8), ((40.091, 8), (38, 9.038), (38, 11)))
        self.add_line('sym-e8', (38, 11), (38, 17))
        self.add_bezier('sym-e9', (38, 17), ((38, 18.398), (36.845, 19.846), (36, 21)))
        self.add_bezier('sym-e10', (36, 21), ((33.136, 24.891), (28.445, 25.084), (24, 25)))
        self.add_bezier('sym-e11', (24, 25), ((19.555, 25.084), (14.864, 24.891), (12, 21)))
        self.add_bezier('sym-e12', (12, 21), ((11.155, 19.846), (10, 18.398), (10, 17)))
        self.add_line('sym-e13', (10, 17), (10, 11))
        self.add_bezier('sym-e14', (10, 11), ((10, 9.038), (7.909, 8), (6, 8)))
        self.add_bezier('sym-e15', (6, 8), ((5.3, 8), (4.7, 8), (4, 8)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3')
        self.add_contour('sym-c2', 'sym-e4', 'sym-e5')
        self.add_contour('sym-c3', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
