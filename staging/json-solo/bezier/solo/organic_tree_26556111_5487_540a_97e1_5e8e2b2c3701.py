"""Organic tree (ecology), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '26556111-5487-540a-97e1-5e8e2b2c3701'
SOURCE_PATH = 'icons-json/ecology/organic tree_26556111-5487-540a-97e1-5e8e2b2c3701.json'
AUTHOR = 'json_to_solo'

class OrganicTree26556111(Solo48):
    icon_id = 'organic-tree-26556111'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'ecology'
    aliases = ()
    keywords = ('organic', 'tree', 'ecology')

    def build(self):
        self.add_line('e0', (24, 44), (24, 12))
        self.add_line('e1', (31, 21), (24, 27))
        self.add_line('e2', (17, 21), (24, 27))
        self.add_line('e3', (19, 34), (29, 34))
        self.add_bezier('e4', (29, 34), ((29.837, 34), (30.843, 33.627), (31.606, 33.4)), ((36.345, 31.964), (39.975, 28.482), (39.975, 24.627)), ((39.975, 24.409), (40, 24.191), (40, 23.973)), ((40, 23.97), (40, 23.968), (40, 23.966)), ((40, 23.823), (39.988, 23.68), (39.988, 23.545)), ((39.988, 19.909), (37.44, 17.409), (34.055, 15.064)), ((33.945, 14.982), (34.166, 14.182), (34.178, 14.055)), ((34.326, 13.073), (34.363, 12.155), (34.166, 11.173)), ((33.489, 7.618), (29.649, 4.009), (24.418, 4.009)), ((24.237, 4.009), (24.043, 4), (23.861, 4)), ((23.858, 4), (23.855, 4), (23.852, 4)), ((23.569, 4), (23.274, 4.009), (22.991, 4.009)), ((22.326, 4.009), (21.612, 4.2), (20.985, 4.345)), ((16.714, 5.336), (13.957, 8.4), (13.588, 11.627)), ((13.514, 12.273), (13.945, 14.709), (13.834, 14.936)), ((13.711, 15.191), (11.434, 16.918), (10.954, 17.364)), ((9.206, 19.009), (8.012, 21.191), (8.012, 23.3)), ((8.012, 23.506), (8, 23.712), (8, 23.917)), ((8, 23.921), (8, 23.924), (8, 23.927)), ((8, 24.236), (8.025, 24.536), (8.025, 24.845)), ((8.025, 28.973), (13.08, 34), (19, 34)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e4', closed=True)
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c2', 'c0')
