"""Pin wave (state), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '79f28f0f-6da1-42b3-a142-474d81fe6b26'
SOURCE_PATH = 'icons-json/state/pin wave_79f28f0f-6da1-42b3-a142-474d81fe6b26.json'
AUTHOR = 'json_to_solo'

class PinWaveState(Solo48):
    icon_id = 'pin-wave-state'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('pin', 'wave', 'state')

    def build(self):
        self.add_arc('sym-e0', (18, 19), (30, 19), radius_x=6, radius_y=5)
        self.add_arc('sym-e1', (30, 19), (18, 19), radius_x=6, radius_y=5)
        self.add_bezier('sym-e2', (22, 42), ((19.59, 39.573), (17.05, 36.682), (15, 34)))
        self.add_bezier('sym-e3', (15, 34), ((13.34, 31.809), (12.33, 30.373), (11, 28)))
        self.add_bezier('sym-e4', (11, 28), ((9.55, 25.418), (8, 21.955), (8, 19)))
        self.add_bezier('sym-e5', (8, 19), ((8, 18.855), (8.01, 19.145), (8, 19)))
        self.add_bezier('sym-e6', (8, 19), ((8, 18.709), (8, 18.291), (8, 18)))
        self.add_bezier('sym-e7', (8, 18), ((8, 10.764), (15.08, 4), (23, 4)))
        self.add_bezier('sym-e8', (23, 4), ((23.08, 4), (23.92, 4), (24, 4)))
        self.add_bezier('sym-e9', (24, 4), ((24.141, 4), (23.861, 4), (24, 4)))
        self.add_bezier('sym-e10', (24, 4), ((24.139, 4), (23.859, 4), (24, 4)))
        self.add_bezier('sym-e11', (24, 4), ((24.08, 4), (24.92, 4), (25, 4)))
        self.add_bezier('sym-e12', (25, 4), ((32.92, 4), (40, 10.764), (40, 18)))
        self.add_bezier('sym-e13', (40, 18), ((40, 18.291), (40, 18.709), (40, 19)))
        self.add_bezier('sym-e14', (40, 19), ((39.99, 19.145), (40, 18.855), (40, 19)))
        self.add_bezier('sym-e15', (40, 19), ((40, 21.955), (38.45, 25.418), (37, 28)))
        self.add_bezier('sym-e16', (37, 28), ((35.67, 30.373), (34.66, 31.809), (33, 34)))
        self.add_bezier('sym-e17', (33, 34), ((30.95, 36.682), (28.41, 39.573), (26, 42)))
        self.add_line('sym-e18', (26, 42), (24, 44))
        self.add_line('sym-e19', (24, 44), (22, 42))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', closed=True)
