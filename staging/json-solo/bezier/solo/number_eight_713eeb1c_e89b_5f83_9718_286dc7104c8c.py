"""Number eight (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '713eeb1c-e89b-5f83-9718-286dc7104c8c'
SOURCE_PATH = 'icons-json/interface-essential/number eight_713eeb1c-e89b-5f83-9718-286dc7104c8c.json'
AUTHOR = 'json_to_solo'

class NumberEightInterfaceEssential(Solo48):
    icon_id = 'number-eight-interface-essential'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('number', 'eight', 'interface-essential')

    def build(self):
        self.add_bezier('sym-e0', (24, 23), ((25.948, 23), (28.177, 22.482), (30, 22)))
        self.add_bezier('sym-e1', (30, 22), ((40, 19.118), (40, 7.627), (30, 5)))
        self.add_bezier('sym-e2', (30, 5), ((28.693, 4.7), (27.387, 4), (26, 4)))
        self.add_bezier('sym-e3', (26, 4), ((25.853, 4), (25.147, 4), (25, 4)))
        self.add_bezier('sym-e4', (25, 4), ((24.853, 4), (25.147, 4), (25, 4)))
        self.add_bezier('sym-e5', (25, 4), ((24.773, 4), (24.227, 4), (24, 4)))
        self.add_bezier('sym-e6', (24, 4), ((23.773, 4), (23.227, 4), (23, 4)))
        self.add_bezier('sym-e7', (23, 4), ((22.853, 4), (23.147, 4), (23, 4)))
        self.add_bezier('sym-e8', (23, 4), ((22.853, 4), (22.147, 4), (22, 4)))
        self.add_bezier('sym-e9', (22, 4), ((20.613, 4), (19.307, 4.7), (18, 5)))
        self.add_bezier('sym-e10', (18, 5), ((8, 7.627), (8, 19.118), (18, 22)))
        self.add_bezier('sym-e11', (18, 22), ((19.823, 22.482), (22.052, 23), (24, 23)))
        self.add_bezier('sym-e12', (24, 44), ((24.293, 44), (24.707, 44), (25, 44)))
        self.add_bezier('sym-e13', (25, 44), ((31.547, 44), (36.907, 41.164), (39, 37)))
        self.add_bezier('sym-e14', (39, 37), ((39.44, 36.109), (40, 34.945), (40, 34)))
        self.add_bezier('sym-e15', (40, 34), ((40, 33.845), (40, 34.155), (40, 34)))
        self.add_bezier('sym-e16', (40, 34), ((40, 33.782), (40, 33.218), (40, 33)))
        self.add_bezier('sym-e17', (40, 33), ((40, 26.845), (33.733, 23.591), (25, 23)))
        self.add_bezier('sym-e18', (25, 23), ((24.51, 22.967), (24.479, 23), (24, 23)))
        self.add_bezier('sym-e19', (24, 23), ((23.521, 23), (23.49, 22.967), (23, 23)))
        self.add_bezier('sym-e20', (23, 23), ((14.267, 23.591), (8, 26.845), (8, 33)))
        self.add_bezier('sym-e21', (8, 33), ((8, 33.218), (8, 33.782), (8, 34)))
        self.add_bezier('sym-e22', (8, 34), ((8, 34.155), (8, 33.845), (8, 34)))
        self.add_bezier('sym-e23', (8, 34), ((8, 34.945), (8.56, 36.109), (9, 37)))
        self.add_bezier('sym-e24', (9, 37), ((11.093, 41.164), (16.453, 44), (23, 44)))
        self.add_bezier('sym-e25', (23, 44), ((23.293, 44), (23.707, 44), (24, 44)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', closed=True)
        self.add_contour('sym-c1', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', closed=True)
