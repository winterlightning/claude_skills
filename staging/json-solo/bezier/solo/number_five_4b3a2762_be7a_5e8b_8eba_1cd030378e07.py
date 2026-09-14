"""Number five (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4b3a2762-be7a-5e8b-8eba-1cd030378e07'
SOURCE_PATH = 'icons-json/interface-essential/number five_4b3a2762-be7a-5e8b-8eba-1cd030378e07.json'
AUTHOR = 'json_to_solo'

class NumberFiveInterfaceEssential(Solo48):
    icon_id = 'number-five-interface-essential'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('number', 'five', 'interface-essential')

    def build(self):
        self.add_line('e0', (9, 22), (14, 4))
        self.add_line('e1', (14, 4), (38, 4))
        self.add_bezier('e2', (8, 37), ((10.523, 40.264), (14.006, 42.655), (19.126, 43.6)), ((19.963, 43.755), (20.935, 43.982), (21.797, 43.982)), ((22.166, 43.982), (22.548, 44), (22.917, 44)), ((22.923, 44), (22.93, 44), (22.936, 44)), ((23.336, 44), (23.748, 43.982), (24.148, 43.982)), ((32.985, 43.982), (39.988, 38.564), (39.988, 32.091)), ((39.988, 31.805), (40, 31.509), (40, 31.214)), ((40, 31.209), (40, 31.205), (40, 31.2)), ((39.988, 31.055), (39.988, 30.909), (39.975, 30.764)), ((39.975, 29.373), (39.545, 27.882), (38.978, 26.564)), ((36.074, 19.727), (25.711, 17.455), (17.009, 19.345)), ((14.166, 19.964), (11.523, 20.845), (9, 22)))
        self.add_contour('c0', 'e2', 'e0', 'e1')
