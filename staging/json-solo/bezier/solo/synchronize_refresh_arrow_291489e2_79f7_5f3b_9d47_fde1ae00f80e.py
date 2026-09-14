"""Synchronize refresh arrow (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '291489e2-79f7-5f3b-9d47-fde1ae00f80e'
SOURCE_PATH = 'icons-json/interface-essential/synchronize refresh arrow_291489e2-79f7-5f3b-9d47-fde1ae00f80e.json'
AUTHOR = 'json_to_solo'

class SynchronizeRefreshArrow291489e2(Solo48):
    icon_id = 'synchronize-refresh-arrow-291489e2'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('synchronize', 'refresh', 'arrow', 'interface-essential')

    def build(self):
        self.add_line('e0', (9, 26), (4, 21))
        self.add_line('e1', (9, 26), (14, 21))
        self.add_bezier('e2', (25, 40), ((25.991, 40), (26.882, 39.983), (27.873, 39.983)), ((28.727, 39.983), (29.673, 39.731), (30.5, 39.554)), ((36.764, 38.206), (42.055, 33.432), (43.527, 27.629)), ((43.745, 26.771), (43.982, 25.869), (43.982, 24.985)), ((43.982, 24.724), (44, 24.455), (44, 24.194)), ((44, 24.189), (44, 24.185), (44, 24.181)), ((44, 23.907), (43.982, 23.625), (43.982, 23.352)), ((43.982, 14.956), (35.418, 8.017), (26.591, 8.017)), ((26.464, 8.008), (26.327, 8.008), (26.2, 8)), ((26.199, 8), (26.198, 8), (26.197, 8)), ((26.125, 8), (26.053, 8.008), (25.982, 8.008)), ((19.436, 8.008), (13.155, 11.705), (10.336, 17.162)), ((8.945, 19.857), (9.218, 23.078), (9, 26)))
        self.add_contour('c0', 'e2', 'e0')
        self.add_contour('c1', 'e1')
