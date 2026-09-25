"""Independent 32px profile of messages-bubble-square-three-dots.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'fa82fe91-b9d8-4c1d-b3ed-a7c76cdfd5e8'
SOURCE_PATH = 'pictographic-primitives/symbol/messages bubble square three dots_fa82fe91-b9d8-4c1d-b3ed-a7c76cdfd5e8.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('fa82fe91-b9d8-4c1d-b3ed-a7c76cdfd5e8', 'pictographic-primitives/symbol/messages bubble square three dots_fa82fe91-b9d8-4c1d-b3ed-a7c76cdfd5e8.svg'),)
PROFILE_SOURCE_KEYS = ('solo/messages-bubble-square-three-dots',)
SOLO_SOURCE_ICON_IDS = ('messages-bubble-square-three-dots',)
REFERENCE_EXPORT_SHA256 = 'f64602d1564bdbd194755fd955be7335aefb95dc702fb0dcda98d6a490468183'

class Drawing(Sub32):
    icon_id = 'messages-bubble-square-three-dots-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (7, 25), (4, 25))
        self.add_bezier('p1-r1-2', (4, 25), ((4, 24), (3, 24), (3, 23)))
        self.add_bezier('p1-r1-3', (3, 23), ((2, 23), (2, 22), (2, 21)))
        self.add_line('p1-r1-4', (2, 21), (2, 5))
        self.add_arc('p1-r1-5', (2, 5), (4, 2), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-6', (4, 2), (28, 2))
        self.add_arc('p1-r1-7', (28, 2), (30, 5), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-8', (30, 5), (30, 21))
        self.add_bezier('p1-r1-9', (30, 21), ((30, 22), (29, 23), (29, 23)))
        self.add_bezier('p1-r1-10', (29, 23), ((28, 24), (28, 24), (27, 25)))
        self.add_line('p1-r1-11', (27, 25), (14, 25))
        self.add_line('p1-r1-12', (14, 25), (7, 30))
        self.add_line('p1-r1-13', (7, 30), (7, 25))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', 'p1-r1-13', closed=False)
        self.add_line('p2-r1-1', (9, 14), (9, 14))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (16, 14), (16, 14))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (23, 14), (23, 14))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
