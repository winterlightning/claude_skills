"""Slot machine (state), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4398fcae-6165-43b0-ba6a-29de2bb44558'
SOURCE_PATH = 'icons-json/state/slot machine_4398fcae-6165-43b0-ba6a-29de2bb44558.json'
AUTHOR = 'json_to_solo'

class SlotMachineState(Solo48):
    icon_id = 'slot-machine-state'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('slot', 'machine', 'state')

    def build(self):
        self.add_line('sym-e0', (6, 16), (24, 16))
        self.add_line('sym-e1', (24, 16), (42, 16))
        self.add_line('sym-e2', (42, 16), (42, 26))
        self.add_line('sym-e3', (42, 26), (24, 26))
        self.add_line('sym-e4', (24, 26), (24, 16))
        self.add_line('sym-e5', (24, 26), (6, 26))
        self.add_line('sym-e6', (6, 26), (6, 40))
        self.add_arc('sym-e8', (6, 40), (8, 42), radius_x=4, sweep=False)
        self.add_line('sym-e9', (8, 42), (24, 42))
        self.add_line('sym-e10', (24, 42), (40, 42))
        self.add_line('sym-e11', (40, 42), (42, 40))
        self.add_line('sym-e13', (42, 40), (42, 26))
        self.add_line('sym-e14', (40, 6), (24, 6))
        self.add_line('sym-e15', (24, 6), (8, 6))
        self.add_line('sym-e16', (8, 6), (6, 8))
        self.add_line('sym-e17', (6, 8), (6, 16))
        self.add_line('sym-e18', (6, 16), (6, 26))
        self.add_line('sym-e19', (42, 16), (42, 8))
        self.add_line('sym-e20', (42, 8), (40, 6))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4')
        self.add_contour('sym-c1', 'sym-e5', 'sym-e6', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e13')
        self.add_contour('sym-c2', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18')
        self.add_contour('sym-c3', 'sym-e19', 'sym-e20')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2', 'sym-c3')
