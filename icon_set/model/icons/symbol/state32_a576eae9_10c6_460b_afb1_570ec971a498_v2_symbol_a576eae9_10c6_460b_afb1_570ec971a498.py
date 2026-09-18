"""Independent 32px profile of state32-a576eae9-10c6-460b-afb1-570ec971a498.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'a576eae9-10c6-460b-afb1-570ec971a498'
SOURCE_PATH = 'icon_set/assets/combination-state32/a576eae9-10c6-460b-afb1-570ec971a498.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a576eae9-10c6-460b-afb1-570ec971a498', 'icon_set/assets/combination-state32/a576eae9-10c6-460b-afb1-570ec971a498.svg'),)
PROFILE_SOURCE_KEYS = ()
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '33fcea0d9806ceb9df8d71f829abd70c1c4248d9140fb9ee078ea57e79bf9041'

class DrawingVariant2ContainerSymbol(Sub32):
    icon_id = 'state32-a576eae9-10c6-460b-afb1-570ec971a498-v2-symbol'
    related_origin_icon_id = 'state32-a576eae9-10c6-460b-afb1-570ec971a498-v2'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/state32-a576eae9-10c6-460b-afb1-570ec971a498-v2'
    counterpart_icon_id = 'state32-a576eae9-10c6-460b-afb1-570ec971a498-v2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (29, 10), ((26, 5), (21, 2), (16, 2)))
        self.add_bezier('p1-r1-2', (16, 2), ((10, 2), (4, 6), (3, 13)))
        self.add_bezier('p1-r1-3', (3, 13), ((2, 14), (2, 16), (2, 17)))
        self.add_bezier('p1-r1-4', (2, 17), ((2, 25), (9, 30), (16, 30)))
        self.add_bezier('p1-r1-5', (16, 30), ((22, 30), (27, 27), (30, 20)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p1-r2-1', (22, 10), (30, 10))
        self.add_line('p1-r2-2', (30, 10), (30, 2))
        self.add_contour('path-1-2', 'p1-r2-1', 'p1-r2-2', closed=False)
        self.relate('connect', 'path-1-1', 'path-1-2')
