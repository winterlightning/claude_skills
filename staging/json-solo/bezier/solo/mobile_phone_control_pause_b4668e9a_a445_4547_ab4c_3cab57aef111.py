"""Mobile phone control pause (state), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b4668e9a-a445-4547-ab4c-3cab57aef111'
SOURCE_PATH = 'icons-json/state/mobile phone control pause_b4668e9a-a445-4547-ab4c-3cab57aef111.json'
AUTHOR = 'json_to_solo'

class MobilePhoneControlPauseState(Solo48):
    icon_id = 'mobile-phone-control-pause-state'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('mobile', 'phone', 'control', 'pause', 'state')

    def build(self):
        self.add_line('sym-e0', (40, 36), (8, 36))
        self.add_line('sym-e1', (8, 36), (8, 8))
        self.add_bezier('sym-e2', (8, 8), ((8, 6.355), (9.897, 4), (12, 4)))
        self.add_bezier('sym-e3', (12, 4), ((12.034, 4), (12.966, 4), (13, 4)))
        self.add_line('sym-e4', (13, 4), (24, 4))
        self.add_line('sym-e5', (24, 4), (35, 4))
        self.add_bezier('sym-e6', (35, 4), ((35.034, 4), (35.966, 4), (36, 4)))
        self.add_bezier('sym-e7', (36, 4), ((38.103, 4), (40, 6.355), (40, 8)))
        self.add_line('sym-e8', (40, 8), (40, 36))
        self.add_line('sym-e9', (40, 36), (40, 37))
        self.add_bezier('sym-e10', (40, 37), ((40, 37.482), (40, 37.518), (40, 38)))
        self.add_bezier('sym-e11', (40, 38), ((40, 40.282), (38.8, 43.118), (36, 44)))
        self.add_bezier('sym-e12', (36, 44), ((35.634, 44), (35.4, 44), (35, 44)))
        self.add_bezier('sym-e13', (35, 44), ((34.92, 44), (34.08, 44), (34, 44)))
        self.add_line('sym-e14', (34, 44), (24, 44))
        self.add_line('sym-e15', (24, 44), (14, 44))
        self.add_bezier('sym-e16', (14, 44), ((13.92, 44), (13.08, 44), (13, 44)))
        self.add_bezier('sym-e17', (13, 44), ((12.6, 44), (12.366, 44), (12, 44)))
        self.add_bezier('sym-e18', (12, 44), ((9.2, 43.118), (8, 40.282), (8, 38)))
        self.add_bezier('sym-e19', (8, 38), ((8, 37.518), (8, 37.482), (8, 37)))
        self.add_line('sym-e20', (8, 37), (8, 36))
        self.add_line('sym-e21', (19, 14), (19, 26))
        self.add_line('sym-e22', (29, 14), (29, 26))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20')
        self.add_contour('sym-c1', 'sym-e21')
        self.add_contour('sym-c2', 'sym-e22')
