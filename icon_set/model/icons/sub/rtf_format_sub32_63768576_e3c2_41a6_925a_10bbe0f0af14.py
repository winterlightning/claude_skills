"""Independent 32px profile of rtf-format.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '63768576-e3c2-41a6-925a-10bbe0f0af14'
SOURCE_PATH = 'pictographic-primitives/state/rtf format_63768576-e3c2-41a6-925a-10bbe0f0af14.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('63768576-e3c2-41a6-925a-10bbe0f0af14', 'pictographic-primitives/state/rtf format_63768576-e3c2-41a6-925a-10bbe0f0af14.svg'),)
PROFILE_SOURCE_KEYS = ('solo/rtf-format',)
SOLO_SOURCE_ICON_IDS = ('rtf-format',)
REFERENCE_EXPORT_SHA256 = '8b8894e93c5ffd08941da3c860035b2d19a104b99c99902b0cae6acd230efb20'

class Drawing(Sub32):
    icon_id = 'rtf-format-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'state'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (27, 8), (26, 7))
        self.add_line('p1-r1-2', (26, 7), (22, 3))
        self.add_line('p1-r1-3', (22, 3), (22, 2))
        self.add_line('p1-r1-4', (22, 2), (8, 2))
        self.add_line('p1-r1-5', (8, 2), (6, 3))
        self.add_line('p1-r1-6', (6, 3), (5, 6))
        self.add_line('p1-r1-7', (5, 6), (5, 26))
        self.add_line('p1-r1-8', (5, 26), (6, 29))
        self.add_line('p1-r1-9', (6, 29), (7, 30))
        self.add_line('p1-r1-10', (7, 30), (24, 30))
        self.add_arc('p1-r1-11', (24, 30), (27, 27), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('p1-r1-12', (27, 27), (27, 8))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', closed=False)
        self.add_line('p2-r1-1', (12, 16), (20, 16))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (19, 23), (13, 23))
        self.add_arc('p3-r1-2', (13, 23), (12, 22), radius_x=1, radius_y=1, large_arc=False, sweep=True)
        self.add_line('p3-r1-3', (12, 22), (12, 10))
        self.add_arc('p3-r1-4', (12, 10), (13, 9), radius_x=1, radius_y=1, large_arc=False, sweep=True)
        self.add_line('p3-r1-5', (13, 9), (19, 9))
        self.add_arc('p3-r1-6', (19, 9), (20, 10), radius_x=1, radius_y=1, large_arc=False, sweep=True)
        self.add_line('p3-r1-7', (20, 10), (20, 22))
        self.add_arc('p3-r1-8', (20, 22), (19, 23), radius_x=1, radius_y=1, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', 'p3-r1-7', 'p3-r1-8', closed=False)
