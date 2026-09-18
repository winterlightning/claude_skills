"""Independent 32px profile of cocktail.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '4e9eff0a-91b1-4736-8893-c4364a52e7a0'
SOURCE_PATH = 'pictographic-primitives/symbol/cocktail_4e9eff0a-91b1-4736-8893-c4364a52e7a0.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('4e9eff0a-91b1-4736-8893-c4364a52e7a0', 'pictographic-primitives/symbol/cocktail_4e9eff0a-91b1-4736-8893-c4364a52e7a0.svg'),)
PROFILE_SOURCE_KEYS = ('solo/cocktail',)
SOLO_SOURCE_ICON_IDS = ('cocktail',)
REFERENCE_EXPORT_SHA256 = '9883f93d0f62243ac9aceafa509a670e1c04739bd9589a6cefc9687aaedf5efd'

class Drawing(Sub32):
    icon_id = 'cocktail-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 10), (21, 10))
        self.add_line('p1-r1-2', (21, 10), (27, 10))
        self.add_arc('p1-r1-3', (27, 10), (16, 22), radius_x=11, radius_y=11, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (16, 22), (5, 10), radius_x=11, radius_y=11, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (16, 16), (21, 10))
        self.add_line('p2-r1-2', (21, 10), (24, 3))
        self.add_line('p2-r1-3', (24, 3), (27, 2))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_line('p3-r1-1', (16, 22), (16, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (10, 30), (22, 30))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-1', 'p2-r1-2')
        self.relate("connect", 'p1-r1-2', 'p2-r1-1')
        self.relate("connect", 'p1-r1-2', 'p2-r1-2')
        self.relate("connect", 'p1-r1-3', 'p3-r1-1')
        self.relate("connect", 'p1-r1-4', 'p3-r1-1')
