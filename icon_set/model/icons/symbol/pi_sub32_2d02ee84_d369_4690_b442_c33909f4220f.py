"""Independent 32px profile of pi.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '2d02ee84-d369-4690-b442-c33909f4220f'
SOURCE_PATH = 'pictographic-primitives/symbol/pi_2d02ee84-d369-4690-b442-c33909f4220f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2d02ee84-d369-4690-b442-c33909f4220f', 'pictographic-primitives/symbol/pi_2d02ee84-d369-4690-b442-c33909f4220f.svg'),)
PROFILE_SOURCE_KEYS = ('solo/pi',)
SOLO_SOURCE_ICON_IDS = ('pi',)
REFERENCE_EXPORT_SHA256 = '5adecee376ff1a0583c0e766e88ee6851ab7071ab9a9fa2e1a8998ab89532eff'

class Drawing(Sub32):
    icon_id = 'pi-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 5), (10, 5))
        self.add_line('p1-r1-2', (10, 5), (23, 5))
        self.add_line('p1-r1-3', (23, 5), (30, 5))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (10, 5), (6, 27))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (23, 5), (22, 20))
        self.add_bezier('p3-r1-2', (22, 20), ((22, 20), (22, 20), (22, 21)))
        self.add_bezier('p3-r1-3', (22, 21), ((22, 25), (23, 27), (26, 27)))
        self.add_bezier('p3-r1-4', (26, 27), ((27, 27), (28, 26), (29, 25)))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p3-r1-1')
        self.relate('connect', 'p1-r1-3', 'p3-r1-1')
