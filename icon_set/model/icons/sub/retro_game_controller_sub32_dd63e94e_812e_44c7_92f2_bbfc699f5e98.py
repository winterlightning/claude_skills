"""Independent 32px profile of retro-game-controller.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'dd63e94e-812e-44c7-92f2-bbfc699f5e98'
SOURCE_PATH = 'pictographic-primitives/technology/game_dd63e94e-812e-44c7-92f2-bbfc699f5e98.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('dd63e94e-812e-44c7-92f2-bbfc699f5e98', 'pictographic-primitives/technology/game_dd63e94e-812e-44c7-92f2-bbfc699f5e98.svg'),)
PROFILE_SOURCE_KEYS = ('solo/retro-game-controller',)
SOLO_SOURCE_ICON_IDS = ('retro-game-controller',)
REFERENCE_EXPORT_SHA256 = '1ca60569a79b97e54d4f99c3c09e34c4f41c334c81f75ed74689eb1e8e52c596'

class Drawing(Sub32):
    icon_id = 'retro-game-controller-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/technology'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (8, 10), ((4, 11), (2, 15), (2, 18)))
        self.add_bezier('p1-r1-2', (2, 18), ((2, 19), (2, 20), (3, 22)))
        self.add_bezier('p1-r1-3', (3, 22), ((4, 25), (8, 27), (11, 27)))
        self.add_bezier('p1-r1-4', (11, 27), ((12, 27), (13, 27), (15, 26)))
        self.add_line('p1-r1-5', (15, 26), (24, 22))
        self.add_bezier('p1-r1-6', (24, 22), ((28, 21), (30, 17), (30, 14)))
        self.add_bezier('p1-r1-7', (30, 14), ((30, 13), (30, 12), (29, 10)))
        self.add_bezier('p1-r1-8', (29, 10), ((28, 7), (24, 5), (21, 5)))
        self.add_bezier('p1-r1-9', (21, 5), ((20, 5), (19, 5), (17, 6)))
        self.add_line('p1-r1-10', (17, 6), (8, 10))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', closed=False)
        self.add_line('p2-r1-1', (8, 18), (11, 18))
        self.add_line('p2-r1-2', (11, 18), (14, 18))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (11, 15), (11, 18))
        self.add_line('p3-r1-2', (11, 18), (11, 21))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (21, 14), (21, 14))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate("connect", 'p2-r1-1', 'p3-r1-1')
        self.relate("connect", 'p2-r1-1', 'p3-r1-2')
        self.relate("connect", 'p2-r1-2', 'p3-r1-1')
        self.relate("connect", 'p2-r1-2', 'p3-r1-2')
