"""Independent 32px profile of circle-half-symbol.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '031da5e5-a8c4-45af-9b74-e8c1dae95201'
SOURCE_PATH = 'pictographic-primitives/symbol/circle half_031da5e5-a8c4-45af-9b74-e8c1dae95201.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('031da5e5-a8c4-45af-9b74-e8c1dae95201', 'pictographic-primitives/symbol/circle half_031da5e5-a8c4-45af-9b74-e8c1dae95201.svg'),)
PROFILE_SOURCE_KEYS = ('solo/circle-half-symbol',)
SOLO_SOURCE_ICON_IDS = ('circle-half-symbol',)
REFERENCE_EXPORT_SHA256 = '9a30803427845e3ff74742cfd3daef328feb41fd02bc202cb1fcfe6b48bc2c33'

class Drawing(Sub32):
    icon_id = 'circle-half-symbol-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (27, 2), ((27, 2), (27, 2), (26, 2)))
        self.add_bezier('p1-r1-2', (26, 2), ((15, 2), (5, 8), (5, 15)))
        self.add_bezier('p1-r1-3', (5, 15), ((5, 16), (5, 16), (5, 16)))
        self.add_bezier('p1-r1-4', (5, 16), ((5, 19), (6, 22), (9, 24)))
        self.add_bezier('p1-r1-5', (9, 24), ((13, 27), (19, 30), (26, 30)))
        self.add_bezier('p1-r1-6', (26, 30), ((26, 30), (26, 30), (27, 30)))
        self.add_bezier('p1-r1-7', (27, 30), ((27, 30), (27, 30), (27, 30)))
        self.add_line('p1-r1-8', (27, 30), (27, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
