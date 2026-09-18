"""Independent 32px profile of state32-2402841c-2a0c-4c6d-89fa-56200e029d7d.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '2402841c-2a0c-4c6d-89fa-56200e029d7d'
SOURCE_PATH = 'icon_set/assets/combination-state32/2402841c-2a0c-4c6d-89fa-56200e029d7d.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2402841c-2a0c-4c6d-89fa-56200e029d7d', 'icon_set/assets/combination-state32/2402841c-2a0c-4c6d-89fa-56200e029d7d.svg'),)
PROFILE_SOURCE_KEYS = ()
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = 'ed87d229857de0d6048f6b4163a7359b16a7f1fa22b3360b7b7b82eb6ff56dff'

class Drawing(Sub32):
    icon_id = 'state32-2402841c-2a0c-4c6d-89fa-56200e029d7d'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (26, 5), ((23, 3), (20, 2), (17, 2)))
        self.add_bezier('p1-r1-2', (17, 2), ((9, 2), (3, 8), (3, 17)))
        self.add_bezier('p1-r1-3', (3, 17), ((3, 18), (3, 19), (3, 20)))
        self.add_bezier('p1-r1-4', (3, 20), ((5, 27), (10, 30), (16, 30)))
        self.add_bezier('p1-r1-5', (16, 30), ((21, 30), (26, 28), (29, 24)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (13, 10), (23, 16))
        self.add_line('p2-r1-2', (23, 16), (13, 22))
        self.add_line('p2-r1-3', (13, 22), (13, 10))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
