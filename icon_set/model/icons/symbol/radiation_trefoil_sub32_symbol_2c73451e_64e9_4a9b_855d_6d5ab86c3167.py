"""Independent 32px profile of radiation-trefoil.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '2c73451e-64e9-4a9b-855d-6d5ab86c3167'
SOURCE_PATH = 'pictographic-primitives/symbol/nuclear energy_2c73451e-64e9-4a9b-855d-6d5ab86c3167.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2c73451e-64e9-4a9b-855d-6d5ab86c3167', 'pictographic-primitives/symbol/nuclear energy_2c73451e-64e9-4a9b-855d-6d5ab86c3167.svg'), ('db4b8c72-f358-486f-9136-75181808b594', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/radioactive_db4b8c72-f358-486f-9136-75181808b594.svg'))
PROFILE_SOURCE_KEYS = ('solo/radiation-trefoil', 'solo/radiation-trefoil-with-center-stroke')
SOLO_SOURCE_ICON_IDS = ('radiation-trefoil', 'radiation-trefoil-with-center-stroke')
REFERENCE_EXPORT_SHA256 = '03ce75d6b3cec85b8419b496dfcfa9a6c5846028180055c5fbc33b0e971713c8'

class DrawingContainerSymbol(Sub32):
    icon_id = 'radiation-trefoil-sub32-symbol'
    related_origin_icon_id = 'radiation-trefoil-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/radiation-trefoil-sub32'
    counterpart_icon_id = 'radiation-trefoil-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (24, 3), ((26, 5), (28, 6), (29, 8)))
        self.add_bezier('p1-r1-2', (29, 8), ((29, 10), (30, 12), (30, 15)))
        self.add_line('p1-r1-3', (30, 15), (23, 15))
        self.add_arc('p1-r1-4', (23, 15), (20, 9), radius_x=7, radius_y=7, large_arc=False, sweep=False)
        self.add_line('p1-r1-5', (20, 9), (24, 3))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_bezier('p2-r1-1', (2, 15), ((2, 12), (3, 10), (3, 8)))
        self.add_bezier('p2-r1-2', (3, 8), ((4, 6), (6, 5), (8, 3)))
        self.add_line('p2-r1-3', (8, 3), (12, 9))
        self.add_arc('p2-r1-4', (12, 9), (9, 15), radius_x=7, radius_y=7, large_arc=False, sweep=False)
        self.add_line('p2-r1-5', (9, 15), (2, 15))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.add_arc('p3-r1-1', (24, 26), (8, 26), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_line('p3-r1-2', (8, 26), (12, 20))
        self.add_arc('p3-r1-3', (12, 20), (20, 20), radius_x=7, radius_y=7, large_arc=False, sweep=False)
        self.add_line('p3-r1-4', (20, 20), (24, 26))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_line('p4-r1-1', (16, 15), (16, 15))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
