"""Independent 32px profile of rounded-cloud-722d5456.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '722d5456-d7c9-4f1d-8e45-c7093737ba2e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/container/cloud 1_722d5456-d7c9-4f1d-8e45-c7093737ba2e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('722d5456-d7c9-4f1d-8e45-c7093737ba2e', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/container/cloud 1_722d5456-d7c9-4f1d-8e45-c7093737ba2e.svg'),)
PROFILE_SOURCE_KEYS = ('solo/rounded-cloud-722d5456',)
SOLO_SOURCE_ICON_IDS = ('rounded-cloud-722d5456',)
REFERENCE_EXPORT_SHA256 = 'd15543f91f91e8ba99cf5ec7aae7bc42f7e8867c447ba4962d2c472ef74f2392'

class Drawing(Sub32):
    icon_id = 'rounded-cloud-722d5456-sub32'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'container'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (8, 15), (16, 6), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (16, 6), (24, 15), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (24, 15), (30, 20), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (30, 20), (24, 26), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (24, 26), (8, 26))
        self.add_arc('p1-r1-6', (8, 26), (2, 20), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('p1-r1-7', (2, 20), (8, 15), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
