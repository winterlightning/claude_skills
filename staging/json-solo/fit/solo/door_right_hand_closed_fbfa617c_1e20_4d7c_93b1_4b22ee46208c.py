"""Door right hand closed (building), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fbfa617c-1e20-4d7c-93b1-4b22ee46208c'
SOURCE_PATH = 'icons-json/building/door right hand closed_fbfa617c-1e20-4d7c-93b1-4b22ee46208c.json'
AUTHOR = 'json_to_solo'

class DoorRightHandClosedBuilding(Solo48):
    icon_id = 'door-right-hand-closed-building'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'building'
    aliases = ()
    keywords = ('door', 'right', 'hand', 'closed', 'building')

    def build(self):
        self.add_line('sym-e0', (11, 42), (37, 42))
        self.add_line('sym-e1', (37, 42), (42, 42))
        self.add_line('sym-e2', (24, 6), (35, 6))
        self.add_arc('sym-e3', (35, 6), (37, 8), radius_x=2)
        self.add_line('sym-e4', (37, 8), (37, 42))
        self.add_line('sym-e5', (6, 42), (11, 42))
        self.add_line('sym-e6', (11, 42), (11, 8))
        self.add_arc('sym-e7', (11, 8), (13, 6), radius_x=2)
        self.add_line('sym-e8', (13, 6), (24, 6))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4')
        self.add_contour('sym-c2', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
