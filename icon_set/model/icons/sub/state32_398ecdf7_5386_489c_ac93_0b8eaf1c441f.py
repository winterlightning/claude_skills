"""Independent 32px profile of state32-398ecdf7-5386-489c-ac93-0b8eaf1c441f.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '398ecdf7-5386-489c-ac93-0b8eaf1c441f'
SOURCE_PATH = 'icon_set/assets/combination-state32/398ecdf7-5386-489c-ac93-0b8eaf1c441f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('398ecdf7-5386-489c-ac93-0b8eaf1c441f', 'icon_set/assets/combination-state32/398ecdf7-5386-489c-ac93-0b8eaf1c441f.svg'),)
PROFILE_SOURCE_KEYS = ()
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '5b9dd1bd4bdd581e7a5f3dc3d057c62db3f2caa59e21b93ec6ae7e8b5799a90b'

class Drawing(Sub32):
    icon_id = 'state32-398ecdf7-5386-489c-ac93-0b8eaf1c441f'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'state'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (20, 21), ((20, 14), (16, 12), (12, 12)))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p1-r2-1', (15, 10), (12, 12))
        self.add_line('p1-r2-2', (12, 12), (15, 15))
        self.add_contour('path-1-2', 'p1-r2-1', 'p1-r2-2', closed=False)
        self.add_arc('p2-r1-1', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=True, sweep=False)
        self.add_arc('p2-r1-2', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=True, sweep=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.relate("connect", 'p1-r1-1', 'p1-r2-1')
        self.relate("connect", 'p1-r1-1', 'p1-r2-2')
