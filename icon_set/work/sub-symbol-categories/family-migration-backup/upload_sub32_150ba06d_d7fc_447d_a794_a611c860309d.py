"""Independent 32px profile of upload.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '150ba06d-d7fc-447d-a794-a611c860309d'
SOURCE_PATH = 'pictographic-primitives/emails/upload_150ba06d-d7fc-447d-a794-a611c860309d.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('150ba06d-d7fc-447d-a794-a611c860309d', 'pictographic-primitives/emails/upload_150ba06d-d7fc-447d-a794-a611c860309d.svg'),)
PROFILE_SOURCE_KEYS = ('solo/upload',)
SOLO_SOURCE_ICON_IDS = ('upload',)
REFERENCE_EXPORT_SHA256 = '90ddb7d31b33bdb60915cc36290d5526a36036d6d83792c01d872136b5d8568f'

class Drawing(Sub32):
    icon_id = 'upload-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'emails'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (9, 9), (16, 2))
        self.add_line('p1-r1-2', (16, 2), (23, 9))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (16, 2), (16, 20))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (5, 23), (5, 26))
        self.add_arc('p3-r1-2', (5, 26), (9, 30), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('p3-r1-3', (9, 30), (23, 30))
        self.add_arc('p3-r1-4', (23, 30), (27, 26), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('p3-r1-5', (27, 26), (27, 23))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-2', 'p2-r1-1')
