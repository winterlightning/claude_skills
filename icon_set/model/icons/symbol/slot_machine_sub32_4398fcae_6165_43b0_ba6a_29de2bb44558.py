"""Independent 32px profile of slot-machine.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '4398fcae-6165-43b0-ba6a-29de2bb44558'
SOURCE_PATH = 'pictographic-primitives/state/slot machine_4398fcae-6165-43b0-ba6a-29de2bb44558.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('4398fcae-6165-43b0-ba6a-29de2bb44558', 'pictographic-primitives/state/slot machine_4398fcae-6165-43b0-ba6a-29de2bb44558.svg'),)
PROFILE_SOURCE_KEYS = ('solo/slot-machine',)
SOLO_SOURCE_ICON_IDS = ('slot-machine',)
REFERENCE_EXPORT_SHA256 = '648c7e4f98f18f1807eae9a913eabe9c163bffa6389eec999d3fc5d6621b3559'

class Drawing(Sub32):
    icon_id = 'slot-machine-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 2), (11, 2))
        self.add_line('p1-r1-2', (11, 2), (16, 2))
        self.add_line('p1-r1-3', (16, 2), (21, 2))
        self.add_line('p1-r1-4', (21, 2), (27, 2))
        self.add_arc('p1-r1-5', (27, 2), (30, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-6', (30, 5), (30, 11))
        self.add_line('p1-r1-7', (30, 11), (30, 16))
        self.add_line('p1-r1-8', (30, 16), (30, 21))
        self.add_line('p1-r1-9', (30, 21), (30, 27))
        self.add_arc('p1-r1-10', (30, 27), (27, 30), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-11', (27, 30), (21, 30))
        self.add_line('p1-r1-12', (21, 30), (16, 30))
        self.add_line('p1-r1-13', (16, 30), (11, 30))
        self.add_line('p1-r1-14', (11, 30), (5, 30))
        self.add_arc('p1-r1-15', (5, 30), (2, 27), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-16', (2, 27), (2, 21))
        self.add_line('p1-r1-17', (2, 21), (2, 16))
        self.add_line('p1-r1-18', (2, 16), (2, 11))
        self.add_line('p1-r1-19', (2, 11), (2, 5))
        self.add_arc('p1-r1-20', (2, 5), (5, 2), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', 'p1-r1-13', 'p1-r1-14', 'p1-r1-15', 'p1-r1-16', 'p1-r1-17', 'p1-r1-18', 'p1-r1-19', 'p1-r1-20', closed=False)
        self.add_line('p2-r1-1', (2, 11), (16, 11))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (16, 11), (30, 11))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (16, 11), (16, 30))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate('connect', 'p1-r1-6', 'p3-r1-1')
        self.relate('connect', 'p1-r1-7', 'p3-r1-1')
        self.relate('connect', 'p1-r1-12', 'p4-r1-1')
        self.relate('connect', 'p1-r1-13', 'p4-r1-1')
        self.relate('connect', 'p1-r1-18', 'p2-r1-1')
        self.relate('connect', 'p1-r1-19', 'p2-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p4-r1-1')
        self.relate('connect', 'p3-r1-1', 'p4-r1-1')
