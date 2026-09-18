"""Independent 32px profile of dice-b1fb9650.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'b1fb9650-ac29-44c4-bc7c-62fe2b8946d1'
SOURCE_PATH = 'pictographic-primitives/entertainment/dice_b1fb9650-ac29-44c4-bc7c-62fe2b8946d1.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('b1fb9650-ac29-44c4-bc7c-62fe2b8946d1', 'pictographic-primitives/entertainment/dice_b1fb9650-ac29-44c4-bc7c-62fe2b8946d1.svg'),)
PROFILE_SOURCE_KEYS = ('solo/dice-b1fb9650',)
SOLO_SOURCE_ICON_IDS = ('dice-b1fb9650',)
REFERENCE_EXPORT_SHA256 = '8e274c6056ac24e5e012a92e517d2b8191a6472c32441a34b3831b27e05411dc'

class Drawing(Sub32):
    icon_id = 'dice-b1fb9650-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'entertainment'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (16, 16), (16, 16))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (2, 16), (2, 6))
        self.add_arc('p2-r1-2', (2, 6), (6, 2), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p2-r1-3', (6, 2), (16, 2))
        self.add_line('p2-r1-4', (16, 2), (26, 2))
        self.add_arc('p2-r1-5', (26, 2), (30, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p2-r1-6', (30, 6), (30, 16))
        self.add_line('p2-r1-7', (30, 16), (30, 26))
        self.add_arc('p2-r1-8', (30, 26), (26, 30), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p2-r1-9', (26, 30), (16, 30))
        self.add_line('p2-r1-10', (16, 30), (6, 30))
        self.add_arc('p2-r1-11', (6, 30), (2, 26), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p2-r1-12', (2, 26), (2, 16))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', 'p2-r1-8', 'p2-r1-9', 'p2-r1-10', 'p2-r1-11', 'p2-r1-12', closed=False)
