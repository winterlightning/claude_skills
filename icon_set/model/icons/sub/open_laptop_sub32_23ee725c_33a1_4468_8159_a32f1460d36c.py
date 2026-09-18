"""Independent 32px profile of open-laptop.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '23ee725c-33a1-4468-8159-a32f1460d36c'
SOURCE_PATH = 'pictographic-primitives/computers/batch-01/laptop 1_23ee725c-33a1-4468-8159-a32f1460d36c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('23ee725c-33a1-4468-8159-a32f1460d36c', 'pictographic-primitives/computers/batch-01/laptop 1_23ee725c-33a1-4468-8159-a32f1460d36c.svg'), ('9c785f9a-558d-4793-8f09-218c477d8c84', 'pictographic-primitives/computers/batch-01/laptop 1_9c785f9a-558d-4793-8f09-218c477d8c84.svg'), ('0eca8bb8-75fe-4501-aa58-53ce337798cc', 'pictographic-primitives/computers/batch-01/laptop_0eca8bb8-75fe-4501-aa58-53ce337798cc.svg'), ('4679969c-dfb9-4a03-ab57-4d2eded56e5a', 'pictographic-primitives/computers/batch-01/laptop_4679969c-dfb9-4a03-ab57-4d2eded56e5a.svg'), ('7a7343f1-5eae-443d-b8b7-d063758ee85e', 'pictographic-primitives/computers/batch-01/laptop_7a7343f1-5eae-443d-b8b7-d063758ee85e.svg'), ('96bd0a70-5265-56a5-8f8c-7df6339b6c49', 'pictographic-primitives/computers/batch-01/laptop_96bd0a70-5265-56a5-8f8c-7df6339b6c49.svg'))
PROFILE_SOURCE_KEYS = ('solo/open-laptop',)
SOLO_SOURCE_ICON_IDS = ('open-laptop',)
REFERENCE_EXPORT_SHA256 = '0323f1e773042f851a32389933df851e2b550da0f626642f2fb36f5d7c5454a8'

class Drawing(Sub32):
    icon_id = 'open-laptop-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/device'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (6, 5), (26, 5))
        self.add_arc('p1-r1-2', (26, 5), (29, 8), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (29, 8), (29, 20))
        self.add_line('p1-r1-4', (29, 20), (30, 27))
        self.add_line('p1-r1-5', (30, 27), (2, 27))
        self.add_line('p1-r1-6', (2, 27), (3, 20))
        self.add_line('p1-r1-7', (3, 20), (3, 8))
        self.add_arc('p1-r1-8', (3, 8), (6, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_line('p2-r1-1', (3, 20), (29, 20))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.relate("connect", 'p1-r1-3', 'p2-r1-1')
        self.relate("connect", 'p1-r1-4', 'p2-r1-1')
        self.relate("connect", 'p1-r1-6', 'p2-r1-1')
        self.relate("connect", 'p1-r1-7', 'p2-r1-1')
