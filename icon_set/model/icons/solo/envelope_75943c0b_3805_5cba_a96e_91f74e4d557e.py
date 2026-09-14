"""Envelope (emails), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '75943c0b-3805-5cba-a96e-91f74e4d557e'
SOURCE_PATH = 'icons-json/emails/envelope_75943c0b-3805-5cba-a96e-91f74e4d557e.json'
AUTHOR = 'json_to_solo'

class Envelope(Solo48):
    icon_id = 'envelope'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'emails'
    aliases = ()
    keywords = ('envelope', 'emails')

    def build(self):
        self.add_line('sym-e0', (43, 40), (36, 40))
        self.add_line('sym-e1', (36, 40), (7, 40))
        self.add_line('sym-e2', (7, 40), (5, 40))
        self.add_line('sym-e3', (44, 8), (39, 8))
        self.add_line('sym-e4', (39, 8), (6, 8))
        self.add_line('sym-e5', (6, 8), (4, 8))
        self.add_arc('sym-e6', (24, 28), (22, 27), radius_x=3, sweep=False)
        self.add_line('sym-e7', (22, 27), (4, 9))
        self.add_line('sym-e8', (4, 9), (4, 14))
        self.add_line('sym-e9', (4, 14), (4, 37))
        self.add_arc('sym-e10', (4, 37), (4, 38), radius_x=3)
        self.add_arc('sym-e11', (4, 38), (4, 39), radius_x=1)
        self.add_line('sym-e12', (4, 39), (19, 24))
        self.add_arc('sym-e13', (24, 28), (26, 27), radius_x=3)
        self.add_line('sym-e14', (26, 27), (44, 9))
        self.add_line('sym-e15', (44, 9), (44, 14))
        self.add_line('sym-e16', (44, 14), (44, 37))
        self.add_arc('sym-e17', (44, 37), (44, 38), radius_x=3, sweep=False)
        self.add_arc('sym-e18', (44, 38), (44, 39), radius_x=1, sweep=False)
        self.add_line('sym-e19', (44, 39), (29, 24))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2')
        self.add_contour('sym-c1', 'sym-e3', 'sym-e4', 'sym-e5')
        self.add_contour('sym-c2', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12')
        self.add_contour('sym-c3', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c2')
