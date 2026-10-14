"""Independent 32px profile of dna-artificial-intelligence.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'c3ad20f0-3e47-4b9f-8ec6-40806e89dc7f'
SOURCE_PATH = 'pictographic-primitives/artificial-intelligence/dna_c3ad20f0-3e47-4b9f-8ec6-40806e89dc7f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('c3ad20f0-3e47-4b9f-8ec6-40806e89dc7f', 'pictographic-primitives/artificial-intelligence/dna_c3ad20f0-3e47-4b9f-8ec6-40806e89dc7f.svg'),)
PROFILE_SOURCE_KEYS = ('solo/dna-artificial-intelligence',)
SOLO_SOURCE_ICON_IDS = ('dna-artificial-intelligence',)
REFERENCE_EXPORT_SHA256 = '183e50db85fbd5abb575ab3af8146af4e1f46271022ec00bb129e30f77b41fdd'

class Drawing(Sub32):
    icon_id = 'dna-artificial-intelligence-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'artificial-intelligence'
    categories = ('artificial-intelligence', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (4, 2), ((4, 6), (28, 10), (28, 16)))
        self.add_bezier('p1-r1-2', (28, 16), ((28, 22), (4, 26), (4, 30)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_bezier('p2-r1-1', (28, 2), ((28, 6), (4, 10), (4, 16)))
        self.add_bezier('p2-r1-2', (4, 16), ((4, 22), (28, 26), (28, 30)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (4, 16), (28, 16))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p3-r1-1')
        self.relate('connect', 'p1-r1-2', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-2', 'p3-r1-1')
        self.relate('connect', 'path-1-1', 'path-2-1')
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-2')
