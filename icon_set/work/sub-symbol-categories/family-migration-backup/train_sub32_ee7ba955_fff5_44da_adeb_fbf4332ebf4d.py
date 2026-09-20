"""Independent 32px profile of train.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'ee7ba955-fff5-44da-adeb-fbf4332ebf4d'
SOURCE_PATH = 'pictographic-primitives/symbol/train_ee7ba955-fff5-44da-adeb-fbf4332ebf4d.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('ee7ba955-fff5-44da-adeb-fbf4332ebf4d', 'pictographic-primitives/symbol/train_ee7ba955-fff5-44da-adeb-fbf4332ebf4d.svg'),)
PROFILE_SOURCE_KEYS = ('solo/train',)
SOLO_SOURCE_ICON_IDS = ('train',)
REFERENCE_EXPORT_SHA256 = 'a27a93a64d876740c89b5ea68e1bd3164f5592742e03be5297246407659d3588'

class Drawing(Sub32):
    icon_id = 'train-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (27, 8), (5, 8))
        self.add_line('p1-r1-2', (5, 8), (5, 6))
        self.add_arc('p1-r1-3', (5, 6), (9, 2), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-4', (9, 2), (23, 2))
        self.add_arc('p1-r1-5', (23, 2), (27, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-6', (27, 6), (27, 20))
        self.add_arc('p1-r1-7', (27, 20), (24, 22), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-8', (24, 22), (22, 23))
        self.add_line('p1-r1-9', (22, 23), (10, 23))
        self.add_line('p1-r1-10', (10, 23), (8, 22))
        self.add_arc('p1-r1-11', (8, 22), (5, 20), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-12', (5, 20), (5, 8))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', closed=False)
        self.add_line('p2-r1-1', (22, 23), (26, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (10, 23), (6, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate("connect", 'p1-r1-8', 'p2-r1-1')
        self.relate("connect", 'p1-r1-9', 'p2-r1-1')
        self.relate("connect", 'p1-r1-9', 'p3-r1-1')
        self.relate("connect", 'p1-r1-10', 'p3-r1-1')
