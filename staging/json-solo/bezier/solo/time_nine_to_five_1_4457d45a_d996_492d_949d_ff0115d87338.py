"""Time nine to five 1 (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4457d45a-d996-492d-949d-ff0115d87338'
SOURCE_PATH = 'icons-json/interface-essential/time nine to five 1_4457d45a-d996-492d-949d-ff0115d87338.json'
AUTHOR = 'json_to_solo'

class TimeNineToFive1InterfaceEssential(Solo48):
    icon_id = 'time-nine-to-five-1-interface-essential'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('time', 'nine', 'to', 'five', 'interface-essential')

    def build(self):
        self.add_line('e0', (35, 32), (35, 38))
        self.add_line('e1', (40, 38), (35, 38))
        self.add_line('e2', (31, 16), (22, 26))
        self.add_bezier('e3', (24, 42), ((23.894, 42), (23.795, 41.992), (23.689, 41.992)), ((15.655, 41.992), (8.986, 36.469), (6.679, 28.975)), ((6.27, 27.649), (6.008, 26.16), (6.008, 24.769)), ((6.008, 24.672), (6, 24.584), (6, 24.487)), ((6, 24.486), (6, 24.484), (6, 24.483)), ((6, 24.164), (6.008, 23.853), (6.008, 23.534)), ((6.008, 14.28), (14.239, 6.008), (23.509, 6.008)), ((23.606, 6.008), (23.694, 6), (23.791, 6)), ((23.792, 6), (23.794, 6), (23.795, 6)), ((24.115, 6), (24.425, 6.008), (24.745, 6.008)), ((33.875, 6.008), (41.992, 14.493), (41.992, 23.534)), ((41.992, 23.687), (42, 23.832), (42, 23.985)), ((42, 23.987), (42, 23.989), (42, 23.992)), ((42, 24.221), (41.992, 24.442), (41.992, 24.671)), ((41.992, 28.516), (40.364, 32.525), (37.639, 35.242)), ((36.674, 36.199), (36.055, 37.1), (35, 38)))
        self.add_contour('c0', 'e3')
        self.add_contour('c1', 'e0')
        self.add_contour('c2', 'e1')
        self.add_contour('c3', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
