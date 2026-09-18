"""Independent 32px profile of folder.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '91daaa04-622c-5ef9-b833-ef74f90bf833'
SOURCE_PATH = 'pictographic-primitives/folders/folder_91daaa04-622c-5ef9-b833-ef74f90bf833.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('91daaa04-622c-5ef9-b833-ef74f90bf833', 'pictographic-primitives/folders/folder_91daaa04-622c-5ef9-b833-ef74f90bf833.svg'),)
PROFILE_SOURCE_KEYS = ('solo/folder',)
SOLO_SOURCE_ICON_IDS = ('folder',)
REFERENCE_EXPORT_SHA256 = '4a807b621db1fea2576499246cd0fc5fe75dbeeb7402b88aff57f6daf5450154'

class Drawing(Sub32):
    icon_id = 'folder-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'folders'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (28, 27), (3, 27))
        self.add_arc('p1-r1-2', (3, 27), (2, 26), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (2, 26), (2, 24), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_line('p1-r1-4', (2, 24), (2, 7))
        self.add_arc('p1-r1-5', (2, 7), (4, 5), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('p1-r1-6', (4, 5), (5, 5), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_line('p1-r1-7', (5, 5), (11, 5))
        self.add_line('p1-r1-8', (11, 5), (16, 8))
        self.add_line('p1-r1-9', (16, 8), (27, 8))
        self.add_bezier('p1-r1-10', (27, 8), ((27, 8), (28, 8), (28, 8)))
        self.add_bezier('p1-r1-11', (28, 8), ((28, 8), (29, 8), (29, 8)))
        self.add_bezier('p1-r1-12', (29, 8), ((29, 9), (30, 9), (30, 10)))
        self.add_line('p1-r1-13', (30, 10), (30, 10))
        self.add_line('p1-r1-14', (30, 10), (30, 26))
        self.add_arc('p1-r1-15', (30, 26), (28, 27), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', 'p1-r1-13', 'p1-r1-14', 'p1-r1-15', closed=False)
