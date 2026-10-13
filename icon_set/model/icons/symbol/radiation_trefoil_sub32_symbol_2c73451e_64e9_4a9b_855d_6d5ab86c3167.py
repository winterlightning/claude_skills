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
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Radiation: three blades (outer arc, straight sides and inner edge) around an empty centre, 4 units between blades.
        self.add_bezier('b0-out', (20, 5), ((18.929, 4.231), (17.469, 4.0), (16, 4)), ((14.531, 4.0), (13.071, 4.231), (12, 5)))
        self.add_polyline('b0-rest', (12, 5), (14, 12), (18, 12), (20, 5))
        self.relate('connect', 'b0-out', 'b0-rest')
        self.add_bezier('b1-out', (2, 21), ((2.921, 23.803), (4.435, 26.426), (7, 28)))
        self.add_polyline('b1-rest', (7, 28), (12, 22), (10, 19), (2, 21))
        self.relate('connect', 'b1-out', 'b1-rest')
        self.add_bezier('b2-out', (25, 28), ((27.565, 26.426), (29.079, 23.803), (30, 21)))
        self.add_polyline('b2-rest', (30, 21), (22, 19), (20, 22), (25, 28))
        self.relate('connect', 'b2-out', 'b2-rest')
