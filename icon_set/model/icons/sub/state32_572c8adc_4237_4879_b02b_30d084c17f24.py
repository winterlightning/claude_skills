"""Independent 32px profile of state32-572c8adc-4237-4879-b02b-30d084c17f24.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '572c8adc-4237-4879-b02b-30d084c17f24'
SOURCE_PATH = 'icon_set/assets/combination-state32/572c8adc-4237-4879-b02b-30d084c17f24.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('572c8adc-4237-4879-b02b-30d084c17f24', 'icon_set/assets/combination-state32/572c8adc-4237-4879-b02b-30d084c17f24.svg'),)
PROFILE_SOURCE_KEYS = ()
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = 'ee682c9282d4b5f7fcd1eb9ba61fd2e532c9fb0cb84210412e1169551cd74356'

class Drawing(Sub32):
    icon_id = 'state32-572c8adc-4237-4879-b02b-30d084c17f24'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (10, 10), (22, 10))
        self.add_bezier('p1-r1-2', (22, 10), ((22, 10), (22, 10), (22, 10)))
        self.add_line('p1-r1-3', (22, 10), (22, 22))
        self.add_bezier('p1-r1-4', (22, 22), ((22, 22), (22, 22), (22, 22)))
        self.add_line('p1-r1-5', (22, 22), (10, 22))
        self.add_bezier('p1-r1-6', (10, 22), ((10, 22), (10, 22), (10, 22)))
        self.add_line('p1-r1-7', (10, 22), (10, 10))
        self.add_bezier('p1-r1-8', (10, 10), ((10, 10), (10, 10), (10, 10)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_arc('p2-r1-1', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=True, sweep=False)
        self.add_arc('p2-r1-2', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=True, sweep=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
