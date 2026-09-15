"""Personal hotspot (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c4cba21b-2373-4c7e-bc83-c6a4dfef5c0f'
SOURCE_PATH = 'pictographic-primitives/symbol/personal hotspot_c4cba21b-2373-4c7e-bc83-c6a4dfef5c0f.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class PersonalHotspotSymbol(Solo48):
    icon_id = 'personal-hotspot-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('personal', 'hotspot', 'symbol')

    def build(self):
        # Plan: remove subpixel cubic detours while preserving real contour nodes.
        # Reference: supplied subject and its existing stroke graph.
        self.add_line('e0', (20, 4), (31, 4))
        self.add_line('e1', (18, 44), (27, 44))
        self.add_line('e2', (28, 17), (23, 17))
        self.add_bezier('e3', (29, 30), ((28.259, 30.518), (27.537, 31.418), (26.669, 31.655)), ((25.221, 32.064), (23.192, 31.773), (21.718, 31.745)), ((19.882, 31.718), (17.971, 31.845), (16.194, 31.255)), ((12.059, 29.864), (9.078, 26.027), (8.278, 21.482)), ((8.16, 20.818), (8, 20.091), (8, 19.418)), ((8, 19.343), (8, 19.272), (8, 19.2)), ((8, 18.982), (8.008, 18.764), (8.008, 18.545)), ((8.008, 13.318), (10.872, 8.245), (15.133, 5.782)), ((16.615, 4.918), (18.425, 4.455), (20, 4)))
        self.add_bezier('e4', (27, 44), ((27.093, 44), (26.712, 43.991), (26.804, 43.991)), ((33.903, 43.991), (39.992, 37.455), (39.992, 29.764)), ((39.992, 29.638), (40, 29.513), (40, 29.388)), ((39.992, 29.3), (39.992, 29.218), (39.983, 29.136)), ((39.983, 22.073), (34.408, 17), (28, 17)))
        self.add_bezier('e5', (23, 17), ((21.467, 17), (20.364, 17.227), (19, 18)))
        self.add_contour('c0', 'e3', 'e0', closed=False)
        self.add_contour('c1', 'e1', 'e4', 'e2', 'e5', closed=False)
