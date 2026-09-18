"""Independent 32px profile of state32-387118e1-371f-4a7a-a550-753be354d5fc.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '387118e1-371f-4a7a-a550-753be354d5fc'
SOURCE_PATH = 'icon_set/assets/combination-state32/387118e1-371f-4a7a-a550-753be354d5fc.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('387118e1-371f-4a7a-a550-753be354d5fc', 'icon_set/assets/combination-state32/387118e1-371f-4a7a-a550-753be354d5fc.svg'),)
PROFILE_SOURCE_KEYS = ()
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '1ce9d5b8fd02e1b325d629bdf19fa3058770873523372db8b775324cbc16118f'

class Drawing(Sub32):
    icon_id = 'state32-387118e1-371f-4a7a-a550-753be354d5fc'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (16, 2), (16, 16))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_bezier('p1-r2-1', (8, 7), ((4, 10), (2, 14), (2, 18)))
        self.add_bezier('p1-r2-2', (2, 18), ((2, 24), (8, 30), (16, 30)))
        self.add_bezier('p1-r2-3', (16, 30), ((24, 30), (30, 24), (30, 18)))
        self.add_bezier('p1-r2-4', (30, 18), ((30, 14), (28, 10), (24, 7)))
        self.add_contour('path-1-2', 'p1-r2-1', 'p1-r2-2', 'p1-r2-3', 'p1-r2-4', closed=False)
