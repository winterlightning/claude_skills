"""Independent 32px profile of beamed-eighth-notes.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '16a68778-68d4-5f6b-9ce5-e5182435ed96'
SOURCE_PATH = 'pictographic-primitives/music/music note_16a68778-68d4-5f6b-9ce5-e5182435ed96.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('16a68778-68d4-5f6b-9ce5-e5182435ed96', 'pictographic-primitives/music/music note_16a68778-68d4-5f6b-9ce5-e5182435ed96.svg'),)
PROFILE_SOURCE_KEYS = ('solo/beamed-eighth-notes',)
SOLO_SOURCE_ICON_IDS = ('beamed-eighth-notes',)
REFERENCE_EXPORT_SHA256 = '7f43070370e7f320a749982831a9f4b8f0dd7e582d78830eea1900a89aef3c66'

class Drawing(Sub32):
    icon_id = 'beamed-eighth-notes-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/music'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (2, 25), (7, 21), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (7, 21), (11, 25), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (11, 25), (7, 30), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (7, 30), (2, 25), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (11, 25), (11, 7))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_arc('p3-r1-1', (21, 21), (25, 16), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('p3-r1-2', (25, 16), (30, 21), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('p3-r1-3', (30, 21), (25, 25), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('p3-r1-4', (25, 25), (21, 21), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_line('p4-r1-1', (30, 21), (30, 2))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (11, 7), (30, 2))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate("connect", 'p1-r1-2', 'p2-r1-1')
        self.relate("connect", 'p1-r1-3', 'p2-r1-1')
        self.relate("connect", 'p2-r1-1', 'p5-r1-1')
        self.relate("connect", 'p3-r1-2', 'p4-r1-1')
        self.relate("connect", 'p3-r1-3', 'p4-r1-1')
        self.relate("connect", 'p4-r1-1', 'p5-r1-1')
