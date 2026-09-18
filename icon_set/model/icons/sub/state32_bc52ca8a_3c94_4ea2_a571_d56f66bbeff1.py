"""Independent 32px profile of state32-bc52ca8a-3c94-4ea2-a571-d56f66bbeff1.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'bc52ca8a-3c94-4ea2-a571-d56f66bbeff1'
SOURCE_PATH = 'icon_set/assets/combination-state32/bc52ca8a-3c94-4ea2-a571-d56f66bbeff1.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('bc52ca8a-3c94-4ea2-a571-d56f66bbeff1', 'icon_set/assets/combination-state32/bc52ca8a-3c94-4ea2-a571-d56f66bbeff1.svg'),)
PROFILE_SOURCE_KEYS = ()
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '64e5af275b86510b164ece5e9923eb51bcd1cb14059bdf4e2d2adf32e71947a3'

class Drawing(Sub32):
    icon_id = 'state32-bc52ca8a-3c94-4ea2-a571-d56f66bbeff1'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (12, 22), (12, 10))
        self.add_line('p1-r1-2', (12, 10), (16, 10))
        self.add_bezier('p1-r1-3', (16, 10), ((19, 10), (20, 11), (20, 13)))
        self.add_bezier('p1-r1-4', (20, 13), ((20, 14), (19, 16), (16, 16)))
        self.add_line('p1-r1-5', (16, 16), (12, 16))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_bezier('p2-r1-1', (16, 16), ((19, 16), (20, 18), (20, 19)))
        self.add_bezier('p2-r1-2', (20, 19), ((20, 21), (19, 22), (16, 22)))
        self.add_line('p2-r1-3', (16, 22), (12, 22))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_arc('p3-r1-1', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=True, sweep=False)
        self.add_arc('p3-r1-2', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=True, sweep=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-3')
        self.relate("connect", 'p1-r1-4', 'p2-r1-1')
        self.relate("connect", 'p1-r1-5', 'p2-r1-1')
