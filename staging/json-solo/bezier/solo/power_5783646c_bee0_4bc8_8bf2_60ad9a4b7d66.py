"""Power (state), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5783646c-bee0-4bc8-8bf2-60ad9a4b7d66'
SOURCE_PATH = 'icons-json/state/power_5783646c-bee0-4bc8-8bf2-60ad9a4b7d66.json'
AUTHOR = 'json_to_solo'

class PowerState(Solo48):
    icon_id = 'power-state'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('power', 'state')

    def build(self):
        self.add_line('e0', (24, 23), (24, 4))
        self.add_bezier('e1', (15, 14), ((11.303, 17.1), (8.017, 20.964), (8.017, 26.327)), ((8.017, 26.627), (8, 26.927), (8, 27.227)), ((8, 27.231), (8, 27.235), (8, 27.239)), ((8, 27.48), (8.008, 27.722), (8.008, 27.955)), ((8.008, 36.236), (15.646, 44), (23.234, 44)), ((23.235, 44), (23.236, 44), (23.236, 44)), ((23.295, 44), (23.361, 44), (23.419, 44)), ((23.613, 44), (23.806, 43.991), (24, 43.991)), ((32.328, 43.991), (39.992, 36.482), (39.992, 27.309)), ((39.992, 27.229), (40, 27.139), (40, 27.058)), ((40, 27.057), (40, 27.056), (40, 27.055)), ((40, 26.991), (39.992, 26.927), (39.992, 26.864)), ((39.992, 21.482), (36.933, 16.145), (33, 13)))
        self.add_contour('c0', 'e1')
        self.add_contour('c1', 'e0')
