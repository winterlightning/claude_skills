"""Independent 32px profile of sanitary-pad.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '31816e20-325b-4b31-8b23-a9a4d37a4bdf'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/sanitary pad_31816e20-325b-4b31-8b23-a9a4d37a4bdf.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('31816e20-325b-4b31-8b23-a9a4d37a4bdf', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/sanitary pad_31816e20-325b-4b31-8b23-a9a4d37a4bdf.svg'),)
PROFILE_SOURCE_KEYS = ('solo/sanitary-pad',)
SOLO_SOURCE_ICON_IDS = ('sanitary-pad',)
REFERENCE_EXPORT_SHA256 = '79c3591b93e3adc5975a8d718aa71c740229ec09b2b7291c925226fff666ab9b'

class Drawing(Sub32):
    icon_id = 'sanitary-pad-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'health'
    categories = ('health', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (7, 9), (11, 4))
        self.add_bezier('p1-r1-2', (11, 4), ((13, 3), (16, 2), (18, 2)))
        self.add_bezier('p1-r1-3', (18, 2), ((22, 2), (25, 4), (28, 7)))
        self.add_bezier('p1-r1-4', (28, 7), ((29, 9), (30, 11), (30, 14)))
        self.add_bezier('p1-r1-5', (30, 14), ((30, 17), (28, 21), (25, 23)))
        self.add_line('p1-r1-6', (25, 23), (21, 28))
        self.add_bezier('p1-r1-7', (21, 28), ((19, 29), (16, 30), (14, 30)))
        self.add_bezier('p1-r1-8', (14, 30), ((10, 30), (7, 28), (4, 25)))
        self.add_bezier('p1-r1-9', (4, 25), ((3, 23), (2, 21), (2, 18)))
        self.add_bezier('p1-r1-10', (2, 18), ((2, 15), (4, 11), (7, 9)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', closed=False)
        self.add_line('p2-r1-1', (12, 14), (15, 11))
        self.add_bezier('p2-r1-2', (15, 11), ((16, 11), (17, 11), (18, 11)))
        self.add_bezier('p2-r1-3', (18, 11), ((19, 11), (20, 11), (21, 12)))
        self.add_bezier('p2-r1-4', (21, 12), ((21, 13), (21, 14), (21, 14)))
        self.add_bezier('p2-r1-5', (21, 14), ((21, 16), (21, 17), (20, 18)))
        self.add_line('p2-r1-6', (20, 18), (17, 21))
        self.add_bezier('p2-r1-7', (17, 21), ((16, 21), (15, 21), (14, 21)))
        self.add_bezier('p2-r1-8', (14, 21), ((13, 21), (12, 21), (11, 20)))
        self.add_bezier('p2-r1-9', (11, 20), ((11, 19), (11, 18), (11, 18)))
        self.add_bezier('p2-r1-10', (11, 18), ((11, 16), (11, 15), (12, 14)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', 'p2-r1-8', 'p2-r1-9', 'p2-r1-10', closed=False)
