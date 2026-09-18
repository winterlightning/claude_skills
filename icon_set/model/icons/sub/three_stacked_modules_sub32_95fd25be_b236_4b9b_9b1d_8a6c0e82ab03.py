"""Independent 32px profile of three-stacked-modules.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '95fd25be-b236-4b9b-9b1d-8a6c0e82ab03'
SOURCE_PATH = 'pictographic-primitives/programing/module three_95fd25be-b236-4b9b-9b1d-8a6c0e82ab03.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('95fd25be-b236-4b9b-9b1d-8a6c0e82ab03', 'pictographic-primitives/programing/module three_95fd25be-b236-4b9b-9b1d-8a6c0e82ab03.svg'), ('f9fae231-69ce-40f3-ac89-7b4fb7c79dfe', 'pictographic-primitives/programing/module three_f9fae231-69ce-40f3-ac89-7b4fb7c79dfe.svg'))
PROFILE_SOURCE_KEYS = ('solo/three-stacked-modules',)
SOLO_SOURCE_ICON_IDS = ('three-stacked-modules',)
REFERENCE_EXPORT_SHA256 = 'd2571284419ee4ff1bbc5566eece5a2a9217a5fdfe927300e17ef8de9d684884'

class Drawing(Sub32):
    icon_id = 'three-stacked-modules-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/programming'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (11, 2), (21, 2))
        self.add_line('p1-r1-2', (21, 2), (21, 13))
        self.add_line('p1-r1-3', (21, 13), (11, 13))
        self.add_line('p1-r1-4', (11, 13), (11, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (2, 19), (13, 19))
        self.add_line('p2-r1-2', (13, 19), (13, 30))
        self.add_line('p2-r1-3', (13, 30), (2, 30))
        self.add_line('p2-r1-4', (2, 30), (2, 19))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (19, 19), (30, 19))
        self.add_line('p3-r1-2', (30, 19), (30, 30))
        self.add_line('p3-r1-3', (30, 30), (19, 30))
        self.add_line('p3-r1-4', (19, 30), (19, 19))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
