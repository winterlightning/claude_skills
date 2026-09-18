"""Independent 32px profile of whistle-sports.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'c3a5ced3-e720-4af3-8b39-b0f56b9fee0f'
SOURCE_PATH = 'pictographic-primitives/sports/whistle_c3a5ced3-e720-4af3-8b39-b0f56b9fee0f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('c3a5ced3-e720-4af3-8b39-b0f56b9fee0f', 'pictographic-primitives/sports/whistle_c3a5ced3-e720-4af3-8b39-b0f56b9fee0f.svg'),)
PROFILE_SOURCE_KEYS = ('solo/whistle-sports',)
SOLO_SOURCE_ICON_IDS = ('whistle-sports',)
REFERENCE_EXPORT_SHA256 = '3485568cf1ccc62e92067b2ddff04c50dd59a355e4366a8332b6c82eda554e3e'

class Drawing(Sub32):
    icon_id = 'whistle-sports-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'sports'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (28, 2), (30, 7))
        self.add_line('p1-r1-2', (30, 7), (21, 14))
        self.add_bezier('p1-r1-3', (21, 14), ((22, 16), (23, 18), (23, 20)))
        self.add_bezier('p1-r1-4', (23, 20), ((23, 20), (23, 20), (23, 21)))
        self.add_bezier('p1-r1-5', (23, 21), ((22, 26), (18, 30), (13, 30)))
        self.add_bezier('p1-r1-6', (13, 30), ((13, 30), (13, 30), (12, 30)))
        self.add_bezier('p1-r1-7', (12, 30), ((7, 30), (2, 25), (2, 20)))
        self.add_bezier('p1-r1-8', (2, 20), ((2, 20), (2, 19), (2, 19)))
        self.add_bezier('p1-r1-9', (2, 19), ((2, 16), (4, 13), (6, 11)))
        self.add_bezier('p1-r1-10', (6, 11), ((7, 11), (7, 11), (7, 11)))
        self.add_line('p1-r1-11', (7, 11), (28, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', closed=False)
