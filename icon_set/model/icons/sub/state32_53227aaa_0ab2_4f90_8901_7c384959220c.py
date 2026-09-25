"""Independent 32px profile of state32-53227aaa-0ab2-4f90-8901-7c384959220c.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '53227aaa-0ab2-4f90-8901-7c384959220c'
SOURCE_PATH = 'icon_set/assets/combination-state32/53227aaa-0ab2-4f90-8901-7c384959220c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('53227aaa-0ab2-4f90-8901-7c384959220c', 'icon_set/assets/combination-state32/53227aaa-0ab2-4f90-8901-7c384959220c.svg'),)
PROFILE_SOURCE_KEYS = ()
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = 'c165fda8a6f5c7d6af284220ae9778c5a7debc836512891b9a312574057ff2af'

class Drawing(Sub32):
    icon_id = 'state32-53227aaa-0ab2-4f90-8901-7c384959220c'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'state'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (7, 30), (17, 30))
        self.add_bezier('p1-r1-2', (17, 30), ((26, 30), (30, 25), (30, 20)))
        self.add_bezier('p1-r1-3', (30, 20), ((30, 14), (26, 9), (17, 9)))
        self.add_line('p1-r1-4', (17, 9), (2, 9))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p1-r2-1', (9, 2), (2, 9))
        self.add_line('p1-r2-2', (2, 9), (9, 16))
        self.add_contour('path-1-2', 'p1-r2-1', 'p1-r2-2', closed=False)
        self.relate("connect", 'p1-r1-4', 'p1-r2-1')
        self.relate("connect", 'p1-r1-4', 'p1-r2-2')
