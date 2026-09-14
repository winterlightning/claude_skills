"""Chip (state), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd62fa8d6-31ca-4052-9e36-0909d6c1a80e'
SOURCE_PATH = 'icons-json/state/chip_d62fa8d6-31ca-4052-9e36-0909d6c1a80e.json'
AUTHOR = 'json_to_solo'

class ChipState(Solo48):
    icon_id = 'chip-state'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('chip', 'state')

    def build(self):
        self.add_line('sym-e0', (36, 30), (36, 18))
        self.add_line('sym-e1', (36, 18), (42, 18))
        self.add_line('sym-e2', (12, 30), (12, 18))
        self.add_line('sym-e3', (12, 18), (6, 18))
        self.add_line('sym-e4', (31, 6), (31, 12))
        self.add_line('sym-e5', (31, 12), (24, 12))
        self.add_line('sym-e6', (24, 12), (17, 12))
        self.add_line('sym-e7', (17, 12), (17, 6))
        self.add_line('sym-e8', (36, 18), (36, 15))
        self.add_arc('sym-e9', (36, 15), (34, 12), radius_x=4, sweep=False)
        self.add_line('sym-e10', (34, 12), (31, 12))
        self.add_line('sym-e11', (12, 18), (12, 15))
        self.add_arc('sym-e12', (12, 15), (14, 12), radius_x=4)
        self.add_line('sym-e13', (14, 12), (17, 12))
        self.add_line('sym-e14', (42, 30), (36, 30))
        self.add_line('sym-e15', (36, 30), (36, 33))
        self.add_arc('sym-e16', (36, 33), (34, 36), radius_x=4)
        self.add_line('sym-e17', (34, 36), (31, 36))
        self.add_line('sym-e18', (31, 36), (31, 42))
        self.add_line('sym-e19', (24, 36), (31, 36))
        self.add_line('sym-e20', (6, 30), (12, 30))
        self.add_line('sym-e21', (12, 30), (12, 33))
        self.add_arc('sym-e22', (12, 33), (14, 36), radius_x=4, sweep=False)
        self.add_line('sym-e23', (14, 36), (17, 36))
        self.add_line('sym-e24', (17, 36), (17, 42))
        self.add_line('sym-e25', (24, 36), (17, 36))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3')
        self.add_contour('sym-c2', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7')
        self.add_contour('sym-c3', 'sym-e8', 'sym-e9', 'sym-e10')
        self.add_contour('sym-c4', 'sym-e11', 'sym-e12', 'sym-e13')
        self.add_contour('sym-c5', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18')
        self.add_contour('sym-c6', 'sym-e19')
        self.add_contour('sym-c7', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24')
        self.add_contour('sym-c8', 'sym-e25')
        self.relate('connect', 'sym-c0', 'sym-c5')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c7')
        self.relate('connect', 'sym-c1', 'sym-c4')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c2', 'sym-c4')
        self.relate('connect', 'sym-c5', 'sym-c6')
        self.relate('connect', 'sym-c6', 'sym-c8')
        self.relate('connect', 'sym-c7', 'sym-c8')
        self.relate('connect', 'sym-c0', 'sym-c5')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c4')
        self.relate('connect', 'sym-c1', 'sym-c7')
        self.relate('connect', 'sym-c0', 'sym-c5')
        self.relate('connect', 'sym-c1', 'sym-c7')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c4')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c2', 'sym-c4')
        self.relate('connect', 'sym-c5', 'sym-c6')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c2', 'sym-c4')
        self.relate('connect', 'sym-c7', 'sym-c8')
        self.relate('connect', 'sym-c5', 'sym-c6')
        self.relate('connect', 'sym-c7', 'sym-c8')
