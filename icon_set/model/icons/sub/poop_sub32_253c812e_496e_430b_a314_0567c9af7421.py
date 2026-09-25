"""Independent 32px profile of poop.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '253c812e-496e-430b-a314-0567c9af7421'
SOURCE_PATH = 'pictographic-primitives/state/poop_253c812e-496e-430b-a314-0567c9af7421.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('253c812e-496e-430b-a314-0567c9af7421', 'pictographic-primitives/state/poop_253c812e-496e-430b-a314-0567c9af7421.svg'), ('c36f6e2e-cf6c-482e-822f-17cf7a892183', 'pictographic-primitives/symbol/poop_c36f6e2e-cf6c-482e-822f-17cf7a892183.svg'))
PROFILE_SOURCE_KEYS = ('solo/poop', 'solo/poop-symbol')
SOLO_SOURCE_ICON_IDS = ('poop', 'poop-symbol')
REFERENCE_EXPORT_SHA256 = 'f687f6acfb67a09c66fdcb1bd9c3d863fd74051e858f5bf19128c12d73a1ed91'

class Drawing(Sub32):
    icon_id = 'poop-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'state'
    categories = ('state',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (7, 18), ((6, 18), (6, 19), (5, 19)))
        self.add_bezier('p1-r1-2', (5, 19), ((3, 20), (2, 22), (2, 25)))
        self.add_bezier('p1-r1-3', (2, 25), ((2, 25), (2, 25), (2, 25)))
        self.add_bezier('p1-r1-4', (2, 25), ((2, 25), (2, 25), (2, 25)))
        self.add_bezier('p1-r1-5', (2, 25), ((2, 28), (5, 30), (8, 30)))
        self.add_bezier('p1-r1-6', (8, 30), ((8, 30), (8, 30), (8, 30)))
        self.add_bezier('p1-r1-7', (8, 30), ((9, 30), (9, 30), (10, 30)))
        self.add_line('p1-r1-8', (10, 30), (26, 30))
        self.add_bezier('p1-r1-9', (26, 30), ((26, 30), (26, 30), (27, 30)))
        self.add_bezier('p1-r1-10', (27, 30), ((27, 30), (27, 30), (27, 30)))
        self.add_bezier('p1-r1-11', (27, 30), ((29, 29), (30, 28), (30, 27)))
        self.add_bezier('p1-r1-12', (30, 27), ((30, 27), (30, 27), (30, 26)))
        self.add_bezier('p1-r1-13', (30, 26), ((30, 26), (30, 26), (30, 26)))
        self.add_bezier('p1-r1-14', (30, 26), ((30, 26), (30, 26), (30, 26)))
        self.add_bezier('p1-r1-15', (30, 26), ((30, 25), (29, 24), (28, 23)))
        self.add_bezier('p1-r1-16', (28, 23), ((27, 23), (27, 23), (26, 23)))
        self.add_bezier('p1-r1-17', (26, 23), ((26, 23), (26, 23), (26, 23)))
        self.add_bezier('p1-r1-18', (26, 23), ((26, 23), (26, 23), (26, 23)))
        self.add_bezier('p1-r1-19', (26, 23), ((26, 22), (27, 22), (27, 21)))
        self.add_bezier('p1-r1-20', (27, 21), ((27, 21), (27, 20), (27, 20)))
        self.add_bezier('p1-r1-21', (27, 20), ((27, 19), (27, 19), (27, 18)))
        self.add_bezier('p1-r1-22', (27, 18), ((26, 17), (25, 16), (24, 16)))
        self.add_bezier('p1-r1-23', (24, 16), ((23, 16), (23, 15), (22, 15)))
        self.add_bezier('p1-r1-24', (22, 15), ((22, 15), (22, 15), (22, 15)))
        self.add_bezier('p1-r1-25', (22, 15), ((22, 15), (22, 15), (22, 15)))
        self.add_bezier('p1-r1-26', (22, 15), ((22, 15), (22, 14), (22, 14)))
        self.add_bezier('p1-r1-27', (22, 14), ((23, 13), (23, 12), (23, 12)))
        self.add_bezier('p1-r1-28', (23, 12), ((23, 11), (23, 11), (23, 11)))
        self.add_bezier('p1-r1-29', (23, 11), ((23, 9), (22, 8), (21, 6)))
        self.add_bezier('p1-r1-30', (21, 6), ((20, 6), (20, 5), (19, 5)))
        self.add_bezier('p1-r1-31', (19, 5), ((19, 4), (19, 4), (18, 4)))
        self.add_line('p1-r1-32', (18, 4), (17, 2))
        self.add_line('p1-r1-33', (17, 2), (16, 5))
        self.add_bezier('p1-r1-34', (16, 5), ((16, 7), (13, 9), (11, 10)))
        self.add_line('p1-r1-35', (11, 10), (8, 11))
        self.add_bezier('p1-r1-36', (8, 11), ((8, 11), (7, 12), (7, 12)))
        self.add_bezier('p1-r1-37', (7, 12), ((6, 13), (6, 14), (6, 15)))
        self.add_bezier('p1-r1-38', (6, 15), ((6, 16), (7, 16), (7, 18)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', 'p1-r1-13', 'p1-r1-14', 'p1-r1-15', 'p1-r1-16', 'p1-r1-17', 'p1-r1-18', 'p1-r1-19', 'p1-r1-20', 'p1-r1-21', 'p1-r1-22', 'p1-r1-23', 'p1-r1-24', 'p1-r1-25', 'p1-r1-26', 'p1-r1-27', 'p1-r1-28', 'p1-r1-29', 'p1-r1-30', 'p1-r1-31', 'p1-r1-32', 'p1-r1-33', 'p1-r1-34', 'p1-r1-35', 'p1-r1-36', 'p1-r1-37', 'p1-r1-38', closed=False)
