"""Independent 32px profile of british-pound-invoice-document-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'd540aa9a-0088-4ba3-b31e-9f6965432001'
SOURCE_PATH = 'pictographic-primitives/other/pound bill_d540aa9a-0088-4ba3-b31e-9f6965432001.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('d540aa9a-0088-4ba3-b31e-9f6965432001', 'pictographic-primitives/other/pound bill_d540aa9a-0088-4ba3-b31e-9f6965432001.svg'),)
PROFILE_SOURCE_KEYS = ('solo/british-pound-invoice-document-solo',)
SOLO_SOURCE_ICON_IDS = ('british-pound-invoice-document-solo',)
REFERENCE_EXPORT_SHA256 = 'a88b439195a4f7689ddfeb8aa6c25e178b5856f4fa7fed53300c21d04acb9e32'

class Drawing(Sub32):
    icon_id = 'british-pound-invoice-document-solo-profile32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/finance'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 2), (19, 2))
        self.add_line('p1-r1-2', (19, 2), (27, 10))
        self.add_line('p1-r1-3', (27, 10), (27, 30))
        self.add_line('p1-r1-4', (27, 30), (5, 30))
        self.add_line('p1-r1-5', (5, 30), (5, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_arc('p2-r1-1', (20, 15), (14, 15), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('p2-r1-2', (14, 15), (14, 23))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (12, 23), (20, 23))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (12, 17), (15, 17))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
