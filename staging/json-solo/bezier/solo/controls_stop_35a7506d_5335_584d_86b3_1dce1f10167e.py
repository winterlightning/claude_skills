"""Controls stop (video), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '35a7506d-5335-584d-86b3-1dce1f10167e'
SOURCE_PATH = 'icons-json/video/controls stop_35a7506d-5335-584d-86b3-1dce1f10167e.json'
AUTHOR = 'json_to_solo'

class ControlsStopVideo(Solo48):
    icon_id = 'controls-stop-video'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video'
    aliases = ()
    keywords = ('controls', 'stop', 'video')

    def build(self):
        self.add_line('sym-e0', (24, 6), (40, 6))
        self.add_bezier('sym-e1', (40, 6), ((40.245, 6), (39.746, 6), (40, 6)))
        self.add_bezier('sym-e2', (40, 6), ((40.974, 6), (42, 7.092), (42, 8)))
        self.add_bezier('sym-e3', (42, 8), ((42, 8.065), (42, 7.935), (42, 8)))
        self.add_bezier('sym-e4', (42, 8), ((42, 8.131), (42, 7.869), (42, 8)))
        self.add_line('sym-e5', (42, 8), (42, 24))
        self.add_line('sym-e6', (42, 24), (42, 40))
        self.add_bezier('sym-e7', (42, 40), ((42, 40.131), (42, 39.869), (42, 40)))
        self.add_bezier('sym-e8', (42, 40), ((42, 40.065), (42, 39.935), (42, 40)))
        self.add_bezier('sym-e9', (42, 40), ((42, 40.908), (40.974, 42), (40, 42)))
        self.add_bezier('sym-e10', (40, 42), ((39.746, 42), (40.245, 42), (40, 42)))
        self.add_line('sym-e11', (40, 42), (24, 42))
        self.add_line('sym-e12', (24, 42), (8, 42))
        self.add_bezier('sym-e13', (8, 42), ((7.755, 42), (8.254, 42), (8, 42)))
        self.add_bezier('sym-e14', (8, 42), ((7.026, 42), (6, 40.908), (6, 40)))
        self.add_bezier('sym-e15', (6, 40), ((6, 39.935), (6, 40.065), (6, 40)))
        self.add_bezier('sym-e16', (6, 40), ((6, 39.869), (6, 40.131), (6, 40)))
        self.add_line('sym-e17', (6, 40), (6, 24))
        self.add_line('sym-e18', (6, 24), (6, 8))
        self.add_bezier('sym-e19', (6, 8), ((6, 7.869), (6, 8.131), (6, 8)))
        self.add_bezier('sym-e20', (6, 8), ((6, 7.935), (6, 8.065), (6, 8)))
        self.add_bezier('sym-e21', (6, 8), ((6, 7.092), (7.026, 6), (8, 6)))
        self.add_bezier('sym-e22', (8, 6), ((8.254, 6), (7.755, 6), (8, 6)))
        self.add_line('sym-e23', (8, 6), (24, 6))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', closed=True)
