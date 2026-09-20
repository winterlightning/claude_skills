"""Independent 32px profile of pencil-cup.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '104c25ae-97c3-4c5b-897d-6e2ec2b026fa'
SOURCE_PATH = 'pictographic-primitives/symbol/stationary_104c25ae-97c3-4c5b-897d-6e2ec2b026fa.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('104c25ae-97c3-4c5b-897d-6e2ec2b026fa', 'pictographic-primitives/symbol/stationary_104c25ae-97c3-4c5b-897d-6e2ec2b026fa.svg'),)
PROFILE_SOURCE_KEYS = ('solo/pencil-cup',)
SOLO_SOURCE_ICON_IDS = ('pencil-cup',)
REFERENCE_EXPORT_SHA256 = 'af0b81744b3b561ee89427b68c11d6587688141955fa1a0734e9db996a3dac72'

class Drawing(Sub32):
    icon_id = 'pencil-cup-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 16), (12, 16))
        self.add_line('p1-r1-2', (12, 16), (20, 16))
        self.add_line('p1-r1-3', (20, 16), (27, 16))
        self.add_line('p1-r1-4', (27, 16), (27, 26))
        self.add_arc('p1-r1-5', (27, 26), (23, 30), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-6', (23, 30), (9, 30))
        self.add_arc('p1-r1-7', (9, 30), (5, 26), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-8', (5, 26), (5, 16))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_line('p2-r1-1', (5, 16), (5, 8))
        self.add_line('p2-r1-2', (5, 8), (8, 2))
        self.add_line('p2-r1-3', (8, 2), (12, 8))
        self.add_line('p2-r1-4', (12, 8), (12, 16))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (20, 16), (20, 2))
        self.add_line('p3-r1-2', (20, 2), (27, 2))
        self.add_line('p3-r1-3', (27, 2), (27, 16))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-1', 'p2-r1-4')
        self.relate("connect", 'p1-r1-2', 'p2-r1-4')
        self.relate("connect", 'p1-r1-2', 'p3-r1-1')
        self.relate("connect", 'p1-r1-3', 'p3-r1-1')
        self.relate("connect", 'p1-r1-3', 'p3-r1-3')
        self.relate("connect", 'p1-r1-4', 'p3-r1-3')
        self.relate("connect", 'p1-r1-8', 'p2-r1-1')
