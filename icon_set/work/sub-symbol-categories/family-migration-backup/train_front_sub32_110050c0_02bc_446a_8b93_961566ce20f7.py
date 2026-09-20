"""Independent 32px profile of train-front.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '110050c0-02bc-446a-8b93-961566ce20f7'
SOURCE_PATH = 'pictographic-primitives/symbol/train_110050c0-02bc-446a-8b93-961566ce20f7.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('110050c0-02bc-446a-8b93-961566ce20f7', 'pictographic-primitives/symbol/train_110050c0-02bc-446a-8b93-961566ce20f7.svg'),)
PROFILE_SOURCE_KEYS = ('solo/train-front',)
SOLO_SOURCE_ICON_IDS = ('train-front',)
REFERENCE_EXPORT_SHA256 = '2afc659038f76772eae96815ee221d14117eb12aeb8123bea5e27fd1680503a1'

class Drawing(Sub32):
    icon_id = 'train-front-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (11, 2), (21, 2))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (10, 10), (22, 10))
        self.add_arc('p2-r1-2', (22, 10), (27, 14), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p2-r1-3', (27, 14), (27, 18))
        self.add_line('p2-r1-4', (27, 18), (27, 21))
        self.add_arc('p2-r1-5', (27, 21), (22, 25), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p2-r1-6', (22, 25), (21, 25))
        self.add_line('p2-r1-7', (21, 25), (11, 25))
        self.add_line('p2-r1-8', (11, 25), (10, 25))
        self.add_arc('p2-r1-9', (10, 25), (5, 21), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p2-r1-10', (5, 21), (5, 18))
        self.add_line('p2-r1-11', (5, 18), (5, 14))
        self.add_arc('p2-r1-12', (5, 14), (10, 10), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', 'p2-r1-8', 'p2-r1-9', 'p2-r1-10', 'p2-r1-11', 'p2-r1-12', closed=False)
        self.add_line('p3-r1-1', (5, 18), (27, 18))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (11, 25), (2, 30))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (21, 25), (30, 30))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate("connect", 'p2-r1-3', 'p3-r1-1')
        self.relate("connect", 'p2-r1-4', 'p3-r1-1')
        self.relate("connect", 'p2-r1-6', 'p5-r1-1')
        self.relate("connect", 'p2-r1-7', 'p4-r1-1')
        self.relate("connect", 'p2-r1-7', 'p5-r1-1')
        self.relate("connect", 'p2-r1-8', 'p4-r1-1')
        self.relate("connect", 'p2-r1-10', 'p3-r1-1')
        self.relate("connect", 'p2-r1-11', 'p3-r1-1')
