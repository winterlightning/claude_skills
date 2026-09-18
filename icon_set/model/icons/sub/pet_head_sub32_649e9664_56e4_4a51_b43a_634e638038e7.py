"""Independent 32px profile of pet-head.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '649e9664-56e4-4a51-b43a-634e638038e7'
SOURCE_PATH = 'pictographic-primitives/symbol/pet head_649e9664-56e4-4a51-b43a-634e638038e7.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('649e9664-56e4-4a51-b43a-634e638038e7', 'pictographic-primitives/symbol/pet head_649e9664-56e4-4a51-b43a-634e638038e7.svg'),)
PROFILE_SOURCE_KEYS = ('solo/pet-head',)
SOLO_SOURCE_ICON_IDS = ('pet-head',)
REFERENCE_EXPORT_SHA256 = '8bb3ceb9ae8d85e969d74979fd0e772cd4c403faa7da43c62bdc07698df8640b'

class Drawing(Sub32):
    icon_id = 'pet-head-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (20, 8), (22, 7))
        self.add_arc('p1-r1-2', (22, 7), (26, 5), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (26, 5), (30, 9), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (30, 9), (26, 13), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('p1-r1-5', (26, 13), (25, 23), radius_x=9, radius_y=9, large_arc=False, sweep=True)
        self.add_arc('p1-r1-6', (25, 23), (22, 26), radius_x=12, radius_y=12, large_arc=False, sweep=True)
        self.add_arc('p1-r1-7', (22, 26), (16, 27), radius_x=12, radius_y=12, large_arc=False, sweep=True)
        self.add_line('p1-r1-8', (16, 27), (12, 26))
        self.add_arc('p1-r1-9', (12, 26), (8, 24), radius_x=12, radius_y=12, large_arc=False, sweep=True)
        self.add_arc('p1-r1-10', (8, 24), (6, 13), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('p1-r1-11', (6, 13), (2, 9), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('p1-r1-12', (2, 9), (6, 5), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-13', (6, 5), (12, 8), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_arc('p1-r1-14', (12, 8), (20, 8), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', 'p1-r1-13', 'p1-r1-14', closed=False)
