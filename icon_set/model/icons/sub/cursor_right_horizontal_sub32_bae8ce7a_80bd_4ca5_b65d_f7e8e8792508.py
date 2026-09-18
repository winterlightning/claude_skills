"""Independent 32px profile of cursor-right-horizontal.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'bae8ce7a-80bd-4ca5-b65d-f7e8e8792508'
SOURCE_PATH = 'pictographic-primitives/state/cursor right horizontal_bae8ce7a-80bd-4ca5-b65d-f7e8e8792508.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('bae8ce7a-80bd-4ca5-b65d-f7e8e8792508', 'pictographic-primitives/state/cursor right horizontal_bae8ce7a-80bd-4ca5-b65d-f7e8e8792508.svg'),)
PROFILE_SOURCE_KEYS = ('solo/cursor-right-horizontal',)
SOLO_SOURCE_ICON_IDS = ('cursor-right-horizontal',)
REFERENCE_EXPORT_SHA256 = '3eb2ff3240f7b4f6bd34dc943255f3e9dfe6f737dcbd507db8752f7e117b78a4'

class Drawing(Sub32):
    icon_id = 'cursor-right-horizontal-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'state'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (26, 13), (2, 5))
        self.add_line('p1-r1-2', (2, 5), (6, 15))
        self.add_arc('p1-r1-3', (6, 15), (6, 17), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-4', (6, 17), (2, 27))
        self.add_line('p1-r1-5', (2, 27), (30, 15))
        self.add_line('p1-r1-6', (30, 15), (26, 13))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
