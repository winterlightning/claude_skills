"""Independent 32px profile of cloud.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '1a5b10c5-e3d9-4568-9b2c-8d04c5b409cd'
SOURCE_PATH = 'pictographic-primitives/internet/cloud_1a5b10c5-e3d9-4568-9b2c-8d04c5b409cd.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('1a5b10c5-e3d9-4568-9b2c-8d04c5b409cd', 'pictographic-primitives/internet/cloud_1a5b10c5-e3d9-4568-9b2c-8d04c5b409cd.svg'),)
PROFILE_SOURCE_KEYS = ('solo/cloud',)
SOLO_SOURCE_ICON_IDS = ('cloud',)
REFERENCE_EXPORT_SHA256 = '92d6f7aa5f112153455bbef090004fb08fac8d48ea6f7685b095906911cde5f6'

class Drawing(Sub32):
    icon_id = 'cloud-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'internet'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (9, 27), ((5, 27), (2, 24), (2, 20)))
        self.add_bezier('p1-r1-2', (2, 20), ((2, 15), (4, 12), (8, 12)))
        self.add_bezier('p1-r1-3', (8, 12), ((8, 7), (11, 5), (16, 5)))
        self.add_bezier('p1-r1-4', (16, 5), ((21, 5), (24, 7), (24, 12)))
        self.add_bezier('p1-r1-5', (24, 12), ((28, 12), (30, 15), (30, 20)))
        self.add_bezier('p1-r1-6', (30, 20), ((30, 24), (27, 27), (23, 27)))
        self.add_line('p1-r1-7', (23, 27), (9, 27))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
