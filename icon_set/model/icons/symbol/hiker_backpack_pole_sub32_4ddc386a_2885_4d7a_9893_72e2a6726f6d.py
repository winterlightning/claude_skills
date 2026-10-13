"""Independent 32px profile of hiker-backpack-pole.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '4ddc386a-2885-4d7a-9893-72e2a6726f6d'
SOURCE_PATH = 'pictographic-primitives/symbol/trekking_4ddc386a-2885-4d7a-9893-72e2a6726f6d.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('4ddc386a-2885-4d7a-9893-72e2a6726f6d', 'pictographic-primitives/symbol/trekking_4ddc386a-2885-4d7a-9893-72e2a6726f6d.svg'),)
PROFILE_SOURCE_KEYS = ('solo/hiker-backpack-pole',)
SOLO_SOURCE_ICON_IDS = ('hiker-backpack-pole',)
REFERENCE_EXPORT_SHA256 = 'f5dbe1213c58d96d396da87a0e90064090b1e39c292972e38ea5205db355a408'

class Drawing(Sub32):
    icon_id = 'hiker-backpack-pole-sub32'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Hiker: head dot, backpack against the back, arm out to a walking pole, legs apart.
        self.add_arc('head-1', (14, 4), (18, 4), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('head-2', (18, 4), (14, 4), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('head', 'head-1', 'head-2', closed=True)
        self.add_polyline('pack', (14, 14), (6, 14), (6, 22), (14, 22), (14, 14))
        self.add_line('arm', (14, 14), (26, 16))
        self.add_line('pole', (26, 6), (26, 30))
        self.add_line('leg-back', (14, 22), (12, 30))
        self.add_line('leg-front', (14, 22), (18, 30))
        self.relate('connect', 'pack', 'arm')
        self.relate('connect', 'arm', 'pole')
        self.relate('connect', 'pack', 'leg-back')
        self.relate('connect', 'pack', 'leg-front')
        self.relate('connect', 'leg-back', 'leg-front')
