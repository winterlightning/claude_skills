"""Independent 32px profile of man-with-short-hair-and-open-shoulders.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'ccad9539-3f9e-4f75-8205-11baacf5298e'
SOURCE_PATH = 'pictographic-primitives/avatars/man_ccad9539-3f9e-4f75-8205-11baacf5298e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('ccad9539-3f9e-4f75-8205-11baacf5298e', 'pictographic-primitives/avatars/man_ccad9539-3f9e-4f75-8205-11baacf5298e.svg'),)
PROFILE_SOURCE_KEYS = ('solo/man-with-short-hair-and-open-shoulders',)
SOLO_SOURCE_ICON_IDS = ('man-with-short-hair-and-open-shoulders',)
REFERENCE_EXPORT_SHA256 = 'b0af71412baa0ec888521a4ca5dc35bb432718c3793e82cc9342a6ef69085e5a'

class Drawing(Sub32):
    icon_id = 'man-with-short-hair-and-open-shoulders-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'avatars'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (12, 2), (20, 2))
        self.add_arc('p1-r1-2', (20, 2), (23, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (23, 5), (23, 9))
        self.add_arc('p1-r1-4', (23, 9), (9, 9), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (9, 9), (9, 5))
        self.add_arc('p1-r1-6', (9, 5), (12, 2), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_line('p2-r1-1', (5, 30), (5, 27))
        self.add_arc('p2-r1-2', (5, 27), (13, 19), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_line('p2-r1-3', (13, 19), (19, 19))
        self.add_arc('p2-r1-4', (19, 19), (27, 27), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_line('p2-r1-5', (27, 27), (27, 30))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
