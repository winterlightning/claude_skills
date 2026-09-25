"""Independent 32px profile of state32-17182188-4f92-4523-a585-9c4533451c16.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '17182188-4f92-4523-a585-9c4533451c16'
SOURCE_PATH = 'icon_set/assets/combination-state32/17182188-4f92-4523-a585-9c4533451c16.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('17182188-4f92-4523-a585-9c4533451c16', 'icon_set/assets/combination-state32/17182188-4f92-4523-a585-9c4533451c16.svg'),)
PROFILE_SOURCE_KEYS = ()
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '2874371ce022e60a4367defce57ce4632034c6b14d371c8abbdb7a5e8f53d70e'

class Drawing(Sub32):
    icon_id = 'state32-17182188-4f92-4523-a585-9c4533451c16'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'state'
    categories = ('state',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (16, 30), ((10, 23), (4, 17), (4, 12)))
        self.add_bezier('p1-r1-2', (4, 12), ((4, 5), (10, 2), (16, 2)))
        self.add_bezier('p1-r1-3', (16, 2), ((22, 2), (28, 5), (28, 12)))
        self.add_bezier('p1-r1-4', (28, 12), ((28, 17), (22, 23), (16, 30)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (13, 9), (19, 16))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p2-r2-1', (19, 9), (13, 16))
        self.add_contour('path-2-2', 'p2-r2-1', closed=False)
