"""Tags (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'eb9aab75-b57d-5009-bb88-39158cb8ee4a'
SOURCE_PATH = 'icons-json/interface-essential/tags_eb9aab75-b57d-5009-bb88-39158cb8ee4a.json'
AUTHOR = 'json_to_solo'

class TagsInterfaceEssential(Solo48):
    icon_id = 'tags-interface-essential'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('tags', 'interface-essential')

    def build(self):
        self.add_arc('sym-e0', (20, 18), (28, 18), radius_x=4)
        self.add_arc('sym-e1', (28, 18), (20, 18), radius_x=4)
        self.add_bezier('sym-e2', (8, 39), ((8, 39.091), (8, 39.909), (8, 40)))
        self.add_bezier('sym-e3', (8, 40), ((8, 41.982), (9.96, 43.445), (12, 44)))
        self.add_bezier('sym-e4', (12, 44), ((12.34, 44), (12.65, 44), (13, 44)))
        self.add_bezier('sym-e5', (13, 44), ((13.43, 44), (13.57, 44), (14, 44)))
        self.add_bezier('sym-e6', (14, 44), ((14.68, 44), (15.32, 44), (16, 44)))
        self.add_line('sym-e7', (16, 44), (24, 44))
        self.add_line('sym-e8', (24, 44), (32, 44))
        self.add_bezier('sym-e9', (32, 44), ((32.68, 44), (33.32, 44), (34, 44)))
        self.add_bezier('sym-e10', (34, 44), ((34.43, 44), (34.57, 44), (35, 44)))
        self.add_bezier('sym-e11', (35, 44), ((35.35, 44), (35.66, 44), (36, 44)))
        self.add_bezier('sym-e12', (36, 44), ((38.04, 43.445), (40, 41.982), (40, 40)))
        self.add_bezier('sym-e13', (40, 40), ((40, 39.909), (40, 39.091), (40, 39)))
        self.add_line('sym-e14', (40, 39), (40, 19))
        self.add_bezier('sym-e15', (40, 19), ((40, 18.873), (40, 18.118), (40, 18)))
        self.add_bezier('sym-e16', (40, 18), ((40, 17.936), (40, 18.064), (40, 18)))
        self.add_bezier('sym-e17', (40, 18), ((40, 16.745), (38.9, 15.818), (38, 15)))
        self.add_line('sym-e18', (38, 15), (28, 6))
        self.add_bezier('sym-e19', (28, 6), ((26.84, 4.945), (25.82, 4), (24, 4)))
        self.add_bezier('sym-e20', (24, 4), ((23.878, 4), (24.119, 4), (24, 4)))
        self.add_bezier('sym-e21', (24, 4), ((23.881, 4), (24.122, 4), (24, 4)))
        self.add_bezier('sym-e22', (24, 4), ((22.18, 4), (21.16, 4.945), (20, 6)))
        self.add_line('sym-e23', (20, 6), (10, 15))
        self.add_bezier('sym-e24', (10, 15), ((9.1, 15.818), (8, 16.745), (8, 18)))
        self.add_bezier('sym-e25', (8, 18), ((8, 18.064), (8, 17.936), (8, 18)))
        self.add_bezier('sym-e26', (8, 18), ((8, 18.118), (8, 18.873), (8, 19)))
        self.add_line('sym-e27', (8, 19), (8, 39))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27', closed=True)
