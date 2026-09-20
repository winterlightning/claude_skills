"""Independent 32px profile of dna-artificial-intelligence.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'c3ad20f0-3e47-4b9f-8ec6-40806e89dc7f'
SOURCE_PATH = 'pictographic-primitives/artificial-intelligence/dna_c3ad20f0-3e47-4b9f-8ec6-40806e89dc7f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('c3ad20f0-3e47-4b9f-8ec6-40806e89dc7f', 'pictographic-primitives/artificial-intelligence/dna_c3ad20f0-3e47-4b9f-8ec6-40806e89dc7f.svg'),)
PROFILE_SOURCE_KEYS = ('solo/dna-artificial-intelligence',)
SOLO_SOURCE_ICON_IDS = ('dna-artificial-intelligence',)
REFERENCE_EXPORT_SHA256 = '183e50db85fbd5abb575ab3af8146af4e1f46271022ec00bb129e30f77b41fdd'

class Drawing(Sub32):
    icon_id = 'dna-artificial-intelligence-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'artificial-intelligence'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (21, 2), (20, 10), radius_x=8, radius_y=8, large_arc=False, sweep=False)
        self.add_line('p1-r1-2', (20, 10), (21, 11))
        self.add_line('p1-r1-3', (21, 11), (18, 11))
        self.add_arc('p1-r1-4', (18, 11), (11, 17), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_line('p1-r1-5', (11, 17), (11, 24))
        self.add_arc('p1-r1-6', (11, 24), (10, 30), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_arc('p2-r1-1', (30, 8), (25, 11), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_line('p2-r1-2', (25, 11), (21, 11))
        self.add_arc('p2-r1-3', (21, 11), (19, 19), radius_x=9, radius_y=9, large_arc=False, sweep=True)
        self.add_arc('p2-r1-4', (19, 19), (18, 20), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p2-r1-5', (18, 20), (15, 21))
        self.add_arc('p2-r1-6', (15, 21), (5, 20), radius_x=30, radius_y=30, large_arc=False, sweep=False)
        self.add_arc('p2-r1-7', (5, 20), (2, 21), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', closed=False)
        self.relate("connect", 'p1-r1-2', 'p2-r1-2')
        self.relate("connect", 'p1-r1-2', 'p2-r1-3')
        self.relate("connect", 'p1-r1-3', 'p2-r1-2')
        self.relate("connect", 'p1-r1-3', 'p2-r1-3')
