"""Independent 32px profile of disabled-battery-content.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '49cd19ff-6293-48fa-8d62-d508a17a80ae'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/49cd19ff-6293-48fa-8d62-d508a17a80ae.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('49cd19ff-6293-48fa-8d62-d508a17a80ae', 'icon_set/dist/gallery/combination-originals/49cd19ff-6293-48fa-8d62-d508a17a80ae.svg'),)
PROFILE_SOURCE_KEYS = ('solo/disabled-battery-content', 'solo/disabled-battery-content-v2')
SOLO_SOURCE_ICON_IDS = ('disabled-battery-content', 'disabled-battery-content-v2')
REFERENCE_EXPORT_SHA256 = 'a98a496e1c6721f13ec21b2a77a27cc660b7362d8c92d84883761d5006df722d'

class Drawing(Sub32):
    icon_id = 'disabled-battery-content-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    categories = ('symbol', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Disabled battery: rounded body with a bracket terminal, slashed corner to corner.
        self.add_line('b-1', (5, 4), (19, 4))
        self.add_arc('b-2', (19, 4), (22, 7), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('b-3', (22, 7), (22, 25))
        self.add_arc('b-4', (22, 25), (19, 28), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('b-5', (19, 28), (5, 28))
        self.add_arc('b-6', (5, 28), (2, 25), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('b-7', (2, 25), (2, 7))
        self.add_arc('b-8', (2, 7), (5, 4), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('body', 'b-1', 'b-2', 'b-3', 'b-4', 'b-5', 'b-6', 'b-7', 'b-8', closed=True)
        self.add_polyline('terminal', (22, 12), (30, 12), (30, 20), (22, 20))
        self.add_line('slash', (4, 26), (20, 6))
        self.relate('connect', 'body', 'terminal')
        self.relate('connect', 'body', 'slash')
