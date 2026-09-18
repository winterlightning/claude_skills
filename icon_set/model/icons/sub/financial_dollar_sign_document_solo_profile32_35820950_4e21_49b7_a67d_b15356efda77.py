"""Independent 32px profile of financial-dollar-sign-document-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '35820950-4e21-49b7-a67d-b15356efda77'
SOURCE_PATH = 'pictographic-primitives/other/dollar bill_35820950-4e21-49b7-a67d-b15356efda77.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('35820950-4e21-49b7-a67d-b15356efda77', 'pictographic-primitives/other/dollar bill_35820950-4e21-49b7-a67d-b15356efda77.svg'),)
PROFILE_SOURCE_KEYS = ('solo/financial-dollar-sign-document-solo',)
SOLO_SOURCE_ICON_IDS = ('financial-dollar-sign-document-solo',)
REFERENCE_EXPORT_SHA256 = '6d5b6d721f6bdede00fd4d9d02872bc8992658ea250d9fe293a9c8809019ba41'

class Drawing(Sub32):
    icon_id = 'financial-dollar-sign-document-solo-profile32'
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
        self.add_line('p2-r1-1', (20, 12), (16, 12))
        self.add_arc('p2-r1-2', (16, 12), (16, 17), radius_x=4, radius_y=3, large_arc=False, sweep=False)
        self.add_arc('p2-r1-3', (16, 17), (16, 23), radius_x=4, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p2-r1-4', (16, 23), (12, 23))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (16, 10), (16, 12))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (16, 23), (16, 24))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate("connect", 'p2-r1-1', 'p3-r1-1')
        self.relate("connect", 'p2-r1-2', 'p3-r1-1')
        self.relate("connect", 'p2-r1-3', 'p4-r1-1')
        self.relate("connect", 'p2-r1-4', 'p4-r1-1')
