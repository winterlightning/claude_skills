"""Independent 32px profile of seven-lobed-cannabis-leaf.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '487f3a05-de28-44cf-9e49-3130e24b6363'
SOURCE_PATH = 'pictographic-primitives/cannabis/cannabis_487f3a05-de28-44cf-9e49-3130e24b6363.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('487f3a05-de28-44cf-9e49-3130e24b6363', 'pictographic-primitives/cannabis/cannabis_487f3a05-de28-44cf-9e49-3130e24b6363.svg'), ('8a80ee4f-5c0f-47e3-8f69-d4a34318a6b1', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/cannabis/cannabis_8a80ee4f-5c0f-47e3-8f69-d4a34318a6b1.svg'))
PROFILE_SOURCE_KEYS = ('solo/seven-lobed-cannabis-leaf',)
SOLO_SOURCE_ICON_IDS = ('seven-lobed-cannabis-leaf',)
REFERENCE_EXPORT_SHA256 = 'c0ab8426035055cba698a29a2eb98b6141b6d9b6ff7640a3d0db352b7737ce7b'

class Drawing(Sub32):
    icon_id = 'seven-lobed-cannabis-leaf-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'cannabis'
    categories = ('primitives', 'cannabis')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (16, 2), ((18, 6), (19, 8), (19, 11)))
        self.add_bezier('p1-r1-2', (19, 11), ((19, 11), (19, 12), (19, 13)))
        self.add_bezier('p1-r1-3', (19, 13), ((22, 10), (25, 7), (28, 7)))
        self.add_bezier('p1-r1-4', (28, 7), ((28, 12), (25, 14), (22, 16)))
        self.add_bezier('p1-r1-5', (22, 16), ((23, 16), (23, 16), (23, 16)))
        self.add_bezier('p1-r1-6', (23, 16), ((26, 16), (29, 18), (30, 19)))
        self.add_bezier('p1-r1-7', (30, 19), ((29, 22), (27, 23), (25, 23)))
        self.add_bezier('p1-r1-8', (25, 23), ((24, 23), (23, 22), (22, 22)))
        self.add_bezier('p1-r1-9', (22, 22), ((24, 25), (24, 28), (24, 29)))
        self.add_bezier('p1-r1-10', (24, 29), ((21, 29), (18, 28), (16, 26)))
        self.add_bezier('p1-r1-11', (16, 26), ((14, 28), (11, 29), (8, 29)))
        self.add_bezier('p1-r1-12', (8, 29), ((8, 28), (8, 25), (10, 22)))
        self.add_bezier('p1-r1-13', (10, 22), ((9, 22), (8, 23), (7, 23)))
        self.add_bezier('p1-r1-14', (7, 23), ((5, 23), (3, 22), (2, 19)))
        self.add_bezier('p1-r1-15', (2, 19), ((3, 18), (6, 16), (9, 16)))
        self.add_bezier('p1-r1-16', (9, 16), ((9, 16), (9, 16), (10, 16)))
        self.add_bezier('p1-r1-17', (10, 16), ((7, 14), (4, 12), (4, 7)))
        self.add_bezier('p1-r1-18', (4, 7), ((7, 7), (10, 10), (13, 13)))
        self.add_bezier('p1-r1-19', (13, 13), ((13, 12), (13, 11), (13, 11)))
        self.add_bezier('p1-r1-20', (13, 11), ((13, 8), (14, 6), (16, 2)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', 'p1-r1-13', 'p1-r1-14', 'p1-r1-15', 'p1-r1-16', 'p1-r1-17', 'p1-r1-18', 'p1-r1-19', 'p1-r1-20', closed=False)
        self.add_line('p2-r1-1', (16, 26), (16, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.relate('connect', 'p1-r1-10', 'p2-r1-1')
        self.relate('connect', 'p1-r1-11', 'p2-r1-1')
