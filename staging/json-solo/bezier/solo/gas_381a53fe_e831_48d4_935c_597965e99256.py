"""Gas (_uncategorized), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '381a53fe-e831-48d4-935c-597965e99256'
SOURCE_PATH = 'icons-json/_uncategorized_20/gas_381a53fe-e831-48d4-935c-597965e99256.json'
AUTHOR = 'json_to_solo'

class GasUncategorized(Solo48):
    icon_id = 'gas-uncategorized'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized'
    aliases = ()
    keywords = ('gas', '_uncategorized')

    def build(self):
        self.add_bezier('sym-e0', (24, 44), ((24.213, 43.999), (24.787, 44), (25, 44)))
        self.add_bezier('sym-e1', (25, 44), ((33.17, 44), (40, 37.282), (40, 30)))
        self.add_bezier('sym-e2', (40, 30), ((40, 29.855), (40, 29.145), (40, 29)))
        self.add_bezier('sym-e3', (40, 29), ((40, 28.782), (40, 28.218), (40, 28)))
        self.add_bezier('sym-e4', (40, 28), ((40, 20.909), (33.61, 14.273), (29, 9)))
        self.add_bezier('sym-e5', (29, 9), ((27.82, 7.655), (26.26, 6.282), (25, 5)))
        self.add_bezier('sym-e6', (25, 5), ((24.743, 4.734), (24.304, 4.177), (24, 4)))
        self.add_bezier('sym-e7', (24, 4), ((23.696, 4.177), (23.257, 4.734), (23, 5)))
        self.add_bezier('sym-e8', (23, 5), ((21.74, 6.282), (20.18, 7.655), (19, 9)))
        self.add_bezier('sym-e9', (19, 9), ((14.39, 14.273), (8, 20.909), (8, 28)))
        self.add_bezier('sym-e10', (8, 28), ((8, 28.218), (8, 28.782), (8, 29)))
        self.add_bezier('sym-e11', (8, 29), ((8, 29.145), (8, 29.855), (8, 30)))
        self.add_bezier('sym-e12', (8, 30), ((8, 37.282), (14.83, 44), (23, 44)))
        self.add_bezier('sym-e13', (23, 44), ((23.213, 44), (23.787, 43.999), (24, 44)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', closed=True)
