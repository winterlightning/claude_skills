"""Independent 32px profile of chinese-character-wen.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '0bb42ca6-0129-4662-8afe-17019b0e641a'
SOURCE_PATH = 'pictographic-primitives/symbol/chinese language symbol_0bb42ca6-0129-4662-8afe-17019b0e641a.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('0bb42ca6-0129-4662-8afe-17019b0e641a', 'pictographic-primitives/symbol/chinese language symbol_0bb42ca6-0129-4662-8afe-17019b0e641a.svg'),)
PROFILE_SOURCE_KEYS = ('solo/chinese-character-wen',)
SOLO_SOURCE_ICON_IDS = ('chinese-character-wen',)
REFERENCE_EXPORT_SHA256 = '4eaae6e7386e7c678f0efd0efbdd4d4a98f84eb96b4bf99b1178c6e59242671f'

class Drawing(Sub32):
    icon_id = 'chinese-character-wen-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbols/standalone'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 8), (8, 8))
        self.add_line('p1-r1-2', (8, 8), (16, 8))
        self.add_line('p1-r1-3', (16, 8), (24, 8))
        self.add_line('p1-r1-4', (24, 8), (30, 8))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (16, 2), (16, 8))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_arc('p3-r1-1', (8, 8), (16, 21), radius_x=31, radius_y=31, large_arc=False, sweep=False)
        self.add_arc('p3-r1-2', (16, 21), (30, 30), radius_x=31, radius_y=31, large_arc=False, sweep=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_arc('p4-r1-1', (24, 8), (16, 21), radius_x=31, radius_y=31, large_arc=False, sweep=True)
        self.add_arc('p4-r1-2', (16, 21), (2, 30), radius_x=31, radius_y=31, large_arc=False, sweep=True)
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.relate("connect", 'p1-r1-1', 'p3-r1-1')
        self.relate("connect", 'p1-r1-2', 'p2-r1-1')
        self.relate("connect", 'p1-r1-2', 'p3-r1-1')
        self.relate("connect", 'p1-r1-3', 'p2-r1-1')
        self.relate("connect", 'p1-r1-3', 'p4-r1-1')
        self.relate("connect", 'p1-r1-4', 'p4-r1-1')
        self.relate("connect", 'p3-r1-1', 'p4-r1-1')
        self.relate("connect", 'p3-r1-1', 'p4-r1-2')
        self.relate("connect", 'p3-r1-2', 'p4-r1-1')
        self.relate("connect", 'p3-r1-2', 'p4-r1-2')
