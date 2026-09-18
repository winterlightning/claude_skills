"""Independent 32px profile of chicken-face.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '7443f092-4834-4d07-9b5b-1b7914777905'
SOURCE_PATH = 'pictographic-primitives/animals/chicken_7443f092-4834-4d07-9b5b-1b7914777905.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('7443f092-4834-4d07-9b5b-1b7914777905', 'pictographic-primitives/animals/chicken_7443f092-4834-4d07-9b5b-1b7914777905.svg'),)
PROFILE_SOURCE_KEYS = ('solo/chicken-face',)
SOLO_SOURCE_ICON_IDS = ('chicken-face',)
REFERENCE_EXPORT_SHA256 = '9bbc5a9688cae7020358725b5ea130c8ae8e847164c2006b396f805bd598484b'

class Drawing(Sub32):
    icon_id = 'chicken-face-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'animals'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 30), (5, 20))
        self.add_bezier('p1-r1-2', (5, 20), ((5, 13), (10, 8), (16, 8)))
        self.add_bezier('p1-r1-3', (16, 8), ((22, 8), (27, 13), (27, 20)))
        self.add_line('p1-r1-4', (27, 20), (27, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_bezier('p2-r1-1', (16, 8), ((15, 8), (14, 8), (14, 7)))
        self.add_bezier('p2-r1-2', (14, 7), ((13, 7), (13, 6), (13, 5)))
        self.add_bezier('p2-r1-3', (13, 5), ((13, 3), (14, 2), (16, 2)))
        self.add_bezier('p2-r1-4', (16, 2), ((18, 2), (20, 3), (20, 5)))
        self.add_bezier('p2-r1-5', (20, 5), ((20, 6), (19, 7), (18, 7)))
        self.add_bezier('p2-r1-6', (18, 7), ((18, 8), (17, 8), (16, 8)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', closed=False)
        self.add_line('p3-r1-1', (11, 19), (11, 19))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (21, 19), (21, 19))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (13, 26), (16, 30))
        self.add_line('p5-r1-2', (16, 30), (20, 26))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', closed=False)
        self.relate("connect", 'p1-r1-2', 'p2-r1-1')
        self.relate("connect", 'p1-r1-2', 'p2-r1-6')
        self.relate("connect", 'p1-r1-3', 'p2-r1-1')
        self.relate("connect", 'p1-r1-3', 'p2-r1-6')
