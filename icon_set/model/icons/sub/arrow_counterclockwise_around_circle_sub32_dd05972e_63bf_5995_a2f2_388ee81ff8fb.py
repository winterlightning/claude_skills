"""Independent 32px profile of arrow-counterclockwise-around-circle.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'dd05972e-63bf-5995-a2f2-388ee81ff8fb'
SOURCE_PATH = 'pictographic-primitives/arrows/rotate back_dd05972e-63bf-5995-a2f2-388ee81ff8fb.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('dd05972e-63bf-5995-a2f2-388ee81ff8fb', 'pictographic-primitives/arrows/rotate back_dd05972e-63bf-5995-a2f2-388ee81ff8fb.svg'), ('0b53a87a-e04b-4e3c-adfd-dcf1fbf284e1', 'pictographic-primitives/arrows/rotate_0b53a87a-e04b-4e3c-adfd-dcf1fbf284e1.svg'), ('f16056b7-da9d-4235-8ea0-1437b5422e2d', 'pictographic-primitives/arrows/rotate_f16056b7-da9d-4235-8ea0-1437b5422e2d.svg'))
PROFILE_SOURCE_KEYS = ('solo/arrow-counterclockwise-around-circle',)
SOLO_SOURCE_ICON_IDS = ('arrow-counterclockwise-around-circle',)
REFERENCE_EXPORT_SHA256 = '633f158385c05f040c0b56e524b71d8345ad9deb2eb53ea8284260b9a175c5c9'

class Drawing(Sub32):
    icon_id = 'arrow-counterclockwise-around-circle-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'arrows'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (2, 16), ((2, 24), (9, 29), (17, 29)))
        self.add_bezier('p1-r1-2', (17, 29), ((21, 29), (26, 27), (29, 22)))
        self.add_bezier('p1-r1-3', (29, 22), ((29, 20), (30, 18), (30, 17)))
        self.add_bezier('p1-r1-4', (30, 17), ((30, 9), (23, 2), (15, 2)))
        self.add_bezier('p1-r1-5', (15, 2), ((13, 2), (10, 3), (8, 5)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (13, 5), (8, 5))
        self.add_line('p2-r1-2', (8, 5), (8, 10))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.relate("connect", 'p1-r1-5', 'p2-r1-1')
        self.relate("connect", 'p1-r1-5', 'p2-r1-2')
