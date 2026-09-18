"""Independent 32px profile of soap.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '4ee9ecc8-c1c5-4fbd-86bf-4c3aaf9a18f4'
SOURCE_PATH = 'pictographic-primitives/symbol/soap_4ee9ecc8-c1c5-4fbd-86bf-4c3aaf9a18f4.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('4ee9ecc8-c1c5-4fbd-86bf-4c3aaf9a18f4', 'pictographic-primitives/symbol/soap_4ee9ecc8-c1c5-4fbd-86bf-4c3aaf9a18f4.svg'),)
PROFILE_SOURCE_KEYS = ('solo/soap',)
SOLO_SOURCE_ICON_IDS = ('soap',)
REFERENCE_EXPORT_SHA256 = '359ecc91d653bc7a4f8ae3bf5f6bffd1fe0b31fe274abbe6daeb34ca448f9742'

class Drawing(Sub32):
    icon_id = 'soap-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (2, 10), (16, 5), radius_x=14, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (16, 5), (30, 10), radius_x=14, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (30, 10), (16, 16), radius_x=14, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (16, 16), (2, 10), radius_x=14, radius_y=6, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (2, 10), (2, 22))
        self.add_arc('p2-r1-2', (2, 22), (16, 27), radius_x=14, radius_y=6, large_arc=False, sweep=False)
        self.add_arc('p2-r1-3', (16, 27), (30, 22), radius_x=14, radius_y=6, large_arc=False, sweep=False)
        self.add_line('p2-r1-4', (30, 22), (30, 10))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-2', 'p2-r1-4')
        self.relate("connect", 'p1-r1-3', 'p2-r1-4')
        self.relate("connect", 'p1-r1-4', 'p2-r1-1')
