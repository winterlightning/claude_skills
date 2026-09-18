"""Independent 32px profile of book-close-1.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '3591871b-5aae-4c39-9571-b421f21c9a22'
SOURCE_PATH = 'pictographic-primitives/content/book close 1_3591871b-5aae-4c39-9571-b421f21c9a22.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('3591871b-5aae-4c39-9571-b421f21c9a22', 'pictographic-primitives/content/book close 1_3591871b-5aae-4c39-9571-b421f21c9a22.svg'),)
PROFILE_SOURCE_KEYS = ('solo/book-close-1',)
SOLO_SOURCE_ICON_IDS = ('book-close-1',)
REFERENCE_EXPORT_SHA256 = 'da04cf885b588700eb7fe32ffd72f7d489223e86f01904d9c2881b245b04d36f'

class Drawing(Sub32):
    icon_id = 'book-close-1-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'content'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (8, 2), (12, 2))
        self.add_line('p1-r1-2', (12, 2), (24, 2))
        self.add_arc('p1-r1-3', (24, 2), (27, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-4', (27, 5), (27, 23))
        self.add_line('p1-r1-5', (27, 23), (27, 27))
        self.add_arc('p1-r1-6', (27, 27), (24, 30), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-7', (24, 30), (12, 30))
        self.add_line('p1-r1-8', (12, 30), (8, 30))
        self.add_arc('p1-r1-9', (8, 30), (5, 27), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-10', (5, 27), (5, 5))
        self.add_arc('p1-r1-11', (5, 5), (8, 2), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', closed=False)
        self.add_line('p2-r1-1', (12, 2), (12, 23))
        self.add_line('p2-r1-2', (12, 23), (12, 30))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_bezier('p3-r1-1', (12, 23), ((15, 24), (17, 25), (20, 25)))
        self.add_bezier('p3-r1-2', (20, 25), ((22, 25), (24, 24), (27, 23)))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-2', 'p2-r1-1')
        self.relate("connect", 'p1-r1-4', 'p3-r1-2')
        self.relate("connect", 'p1-r1-5', 'p3-r1-2')
        self.relate("connect", 'p1-r1-7', 'p2-r1-2')
        self.relate("connect", 'p1-r1-8', 'p2-r1-2')
        self.relate("connect", 'p2-r1-1', 'p3-r1-1')
        self.relate("connect", 'p2-r1-2', 'p3-r1-1')
