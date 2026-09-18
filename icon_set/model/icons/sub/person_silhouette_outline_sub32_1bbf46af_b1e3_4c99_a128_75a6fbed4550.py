"""Independent 32px profile of person-silhouette-outline.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '1bbf46af-b1e3-4c99-a128-75a6fbed4550'
SOURCE_PATH = 'pictographic-primitives/symbol/person 1_1bbf46af-b1e3-4c99-a128-75a6fbed4550.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('1bbf46af-b1e3-4c99-a128-75a6fbed4550', 'pictographic-primitives/symbol/person 1_1bbf46af-b1e3-4c99-a128-75a6fbed4550.svg'),)
PROFILE_SOURCE_KEYS = ('solo/person-silhouette-outline',)
SOLO_SOURCE_ICON_IDS = ('person-silhouette-outline',)
REFERENCE_EXPORT_SHA256 = '363fd4190f6356d0533e8fcb2220e7ccf9a38780475423a99a86daf57f8ca5d2'

class Drawing(Sub32):
    icon_id = 'person-silhouette-outline-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 30), (5, 26))
        self.add_arc('p1-r1-2', (5, 26), (8, 23), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (8, 23), (10, 20), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('p1-r1-4', (10, 20), (10, 19))
        self.add_arc('p1-r1-5', (10, 19), (8, 13), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_line('p1-r1-6', (8, 13), (8, 10))
        self.add_arc('p1-r1-7', (8, 10), (24, 10), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_line('p1-r1-8', (24, 10), (24, 13))
        self.add_arc('p1-r1-9', (24, 13), (22, 19), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_line('p1-r1-10', (22, 19), (22, 20))
        self.add_arc('p1-r1-11', (22, 20), (24, 23), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_arc('p1-r1-12', (24, 23), (27, 26), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-13', (27, 26), (27, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', 'p1-r1-13', closed=False)
