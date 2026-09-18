"""Independent 32px profile of aerosol-spray-can-batch-019-01.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '31ccd5ef-ee58-44ad-8884-4d5e8485d81f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/spray can_31ccd5ef-ee58-44ad-8884-4d5e8485d81f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('31ccd5ef-ee58-44ad-8884-4d5e8485d81f', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/spray can_31ccd5ef-ee58-44ad-8884-4d5e8485d81f.svg'),)
PROFILE_SOURCE_KEYS = ('solo/aerosol-spray-can-batch-019-01',)
SOLO_SOURCE_ICON_IDS = ('aerosol-spray-can-batch-019-01',)
REFERENCE_EXPORT_SHA256 = '39fa470eb754bd0af248cc1a09283a709fb12819622e60a31985c19a26bc5fde'

class Drawing(Sub32):
    icon_id = 'aerosol-spray-can-batch-019-01-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (8, 10), (17, 10))
        self.add_arc('p1-r1-2', (17, 10), (20, 13), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (20, 13), (20, 27))
        self.add_arc('p1-r1-4', (20, 27), (17, 30), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (17, 30), (8, 30))
        self.add_arc('p1-r1-6', (8, 30), (5, 27), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-7', (5, 27), (5, 13))
        self.add_arc('p1-r1-8', (5, 13), (8, 10), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_line('p2-r1-1', (9, 10), (9, 2))
        self.add_line('p2-r1-2', (9, 2), (16, 2))
        self.add_line('p2-r1-3', (16, 2), (16, 10))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_line('p3-r1-1', (23, 5), (27, 2))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (26, 10), (27, 13))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
