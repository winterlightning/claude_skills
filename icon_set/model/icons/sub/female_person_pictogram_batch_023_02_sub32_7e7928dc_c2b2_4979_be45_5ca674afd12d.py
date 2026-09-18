"""Independent 32px profile of female-person-pictogram-batch-023-02.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '7e7928dc-c2b2-4979-be45-5ca674afd12d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/full body women_7e7928dc-c2b2-4979-be45-5ca674afd12d.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('7e7928dc-c2b2-4979-be45-5ca674afd12d', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/full body women_7e7928dc-c2b2-4979-be45-5ca674afd12d.svg'),)
PROFILE_SOURCE_KEYS = ('solo/female-person-pictogram-batch-023-02',)
SOLO_SOURCE_ICON_IDS = ('female-person-pictogram-batch-023-02',)
REFERENCE_EXPORT_SHA256 = '0cb5eafdb20fa971dfcf916cd41d1d1dc4fe8b02ff8bb49de5d0d802608a02f6'

class Drawing(Sub32):
    icon_id = 'female-person-pictogram-batch-023-02-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (12, 6), (20, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (20, 6), (12, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (12, 16), (20, 16))
        self.add_line('p2-r1-2', (20, 16), (27, 24))
        self.add_line('p2-r1-3', (27, 24), (20, 24))
        self.add_line('p2-r1-4', (20, 24), (20, 30))
        self.add_line('p2-r1-5', (20, 30), (12, 30))
        self.add_line('p2-r1-6', (12, 30), (12, 24))
        self.add_line('p2-r1-7', (12, 24), (5, 24))
        self.add_line('p2-r1-8', (5, 24), (12, 16))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', 'p2-r1-8', closed=False)
