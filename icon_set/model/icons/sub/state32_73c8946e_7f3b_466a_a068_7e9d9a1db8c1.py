"""Independent 32px profile of state32-73c8946e-7f3b-466a-a068-7e9d9a1db8c1.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '73c8946e-7f3b-466a-a068-7e9d9a1db8c1'
SOURCE_PATH = 'icon_set/assets/combination-state32/73c8946e-7f3b-466a-a068-7e9d9a1db8c1.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('73c8946e-7f3b-466a-a068-7e9d9a1db8c1', 'icon_set/assets/combination-state32/73c8946e-7f3b-466a-a068-7e9d9a1db8c1.svg'),)
PROFILE_SOURCE_KEYS = ()
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '3b15c607eed3aac7f081a2ec3033195a03f97fc896918797b677f6ed75f64cf8'

class Drawing(Sub32):
    icon_id = 'state32-73c8946e-7f3b-466a-a068-7e9d9a1db8c1'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'state'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 2), (27, 2))
        self.add_bezier('p1-r1-2', (27, 2), ((29, 2), (30, 3), (30, 5)))
        self.add_line('p1-r1-3', (30, 5), (30, 22))
        self.add_bezier('p1-r1-4', (30, 22), ((30, 24), (29, 25), (27, 25)))
        self.add_line('p1-r1-5', (27, 25), (22, 25))
        self.add_line('p1-r1-6', (22, 25), (22, 30))
        self.add_line('p1-r1-7', (22, 30), (15, 25))
        self.add_line('p1-r1-8', (15, 25), (5, 25))
        self.add_bezier('p1-r1-9', (5, 25), ((3, 25), (2, 24), (2, 22)))
        self.add_line('p1-r1-10', (2, 22), (2, 5))
        self.add_bezier('p1-r1-11', (2, 5), ((2, 3), (3, 2), (5, 2)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', closed=False)
        self.add_line('p2-r1-1', (12, 15), (14, 17))
        self.add_line('p2-r1-2', (14, 17), (20, 11))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
