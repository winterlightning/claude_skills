"""Independent 32px profile of man-with-short-hair-and-open-shoulders.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
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
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'avatars'
    categories = ('avatars', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Man with short hair: squared head with a rounded chin, open shoulders 8 units below.
        self.add_line('h-1', (12, 2), (20, 2))
        self.add_arc('h-2', (20, 2), (23, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('h-3', (23, 5), (23, 7))
        self.add_arc('h-4', (23, 7), (9, 7), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_line('h-5', (9, 7), (9, 5))
        self.add_arc('h-6', (9, 5), (12, 2), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('head', 'h-1', 'h-2', 'h-3', 'h-4', 'h-5', 'h-6', closed=True)
        self.add_arc('s-1', (4, 30), (12, 22), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_line('s-2', (12, 22), (20, 22))
        self.add_arc('s-3', (20, 22), (28, 30), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_contour('shoulders', 's-1', 's-2', 's-3')
