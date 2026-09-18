"""Independent 32px profile of synchronize-refresh-arrow-a0553293.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'a0553293-203d-4c9b-9583-f6ead215b9d7'
SOURCE_PATH = 'pictographic-primitives/interface-essential/synchronize refresh arrow_a0553293-203d-4c9b-9583-f6ead215b9d7.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a0553293-203d-4c9b-9583-f6ead215b9d7', 'pictographic-primitives/interface-essential/synchronize refresh arrow_a0553293-203d-4c9b-9583-f6ead215b9d7.svg'), ('4d77908b-9f0a-416f-bab9-3143aecf95b6', 'pictographic-primitives/interface-essential/synchronize refresh arrow_4d77908b-9f0a-416f-bab9-3143aecf95b6.svg'))
PROFILE_SOURCE_KEYS = ('solo/synchronize-refresh-arrow-a0553293', 'solo/synchronize-refresh-arrow-interface-essential')
SOLO_SOURCE_ICON_IDS = ('synchronize-refresh-arrow-a0553293', 'synchronize-refresh-arrow-interface-essential')
REFERENCE_EXPORT_SHA256 = '9677eec079b466cfacf500d6b45a19cbff276d484544d1af04b88058fb82fcf6'

class Drawing(Sub32):
    icon_id = 'synchronize-refresh-arrow-a0553293-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (27, 16), (15, 5), radius_x=13, radius_y=11, large_arc=False, sweep=False)
        self.add_arc('p1-r1-2', (15, 5), (2, 16), radius_x=13, radius_y=11, large_arc=False, sweep=False)
        self.add_arc('p1-r1-3', (2, 16), (15, 27), radius_x=13, radius_y=11, large_arc=False, sweep=False)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (30, 13), (27, 16))
        self.add_line('p2-r1-2', (27, 16), (24, 12))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-1', 'p2-r1-2')
