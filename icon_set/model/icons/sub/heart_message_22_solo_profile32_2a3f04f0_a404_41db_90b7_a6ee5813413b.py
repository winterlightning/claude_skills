"""Independent 32px profile of heart-message-22-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '2a3f04f0-a404-41db-90b7-a6ee5813413b'
SOURCE_PATH = 'pictographic-primitives/symbol/messages bubble round heart_2a3f04f0-a404-41db-90b7-a6ee5813413b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2a3f04f0-a404-41db-90b7-a6ee5813413b', 'pictographic-primitives/symbol/messages bubble round heart_2a3f04f0-a404-41db-90b7-a6ee5813413b.svg'), ('147e6d81-0d21-49c9-8726-0fadea0fff54', 'pictographic-primitives/symbol/messages bubble with heart_147e6d81-0d21-49c9-8726-0fadea0fff54.svg'))
PROFILE_SOURCE_KEYS = ('solo/heart-message-22-solo', 'solo/heart-message-77-solo')
SOLO_SOURCE_ICON_IDS = ('heart-message-22-solo', 'heart-message-77-solo')
REFERENCE_EXPORT_SHA256 = '685847693ea0fd50c447b5ddb25d955415e53ba9e7894c68b3383fbb4da32c75'

class Drawing(Sub32):
    icon_id = 'heart-message-22-solo-profile32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (7, 2), (25, 2))
        self.add_arc('p1-r1-2', (25, 2), (30, 7), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (30, 7), (30, 19))
        self.add_arc('p1-r1-4', (30, 19), (25, 24), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (25, 24), (16, 24))
        self.add_line('p1-r1-6', (16, 24), (8, 30))
        self.add_line('p1-r1-7', (8, 30), (8, 24))
        self.add_line('p1-r1-8', (8, 24), (7, 24))
        self.add_arc('p1-r1-9', (7, 24), (2, 19), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p1-r1-10', (2, 19), (2, 7))
        self.add_arc('p1-r1-11', (2, 7), (7, 2), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', closed=False)
        self.add_bezier('p2-r1-1', (16, 17), ((13, 14), (9, 14), (9, 11)))
        self.add_bezier('p2-r1-2', (9, 11), ((9, 10), (10, 9), (12, 9)))
        self.add_bezier('p2-r1-3', (12, 9), ((13, 9), (15, 10), (16, 11)))
        self.add_bezier('p2-r1-4', (16, 11), ((17, 10), (19, 9), (20, 9)))
        self.add_bezier('p2-r1-5', (20, 9), ((22, 9), (23, 10), (23, 11)))
        self.add_bezier('p2-r1-6', (23, 11), ((23, 14), (19, 14), (16, 17)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', closed=False)
