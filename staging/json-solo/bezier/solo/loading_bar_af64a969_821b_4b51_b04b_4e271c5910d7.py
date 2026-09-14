"""Loading bar (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'af64a969-821b-4b51-b04b-4e271c5910d7'
SOURCE_PATH = 'icons-json/interface-essential/loading bar_af64a969-821b-4b51-b04b-4e271c5910d7.json'
AUTHOR = 'json_to_solo'

class LoadingBarAf64a969(Solo48):
    icon_id = 'loading-bar-af64a969'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('loading', 'bar', 'interface-essential')

    def build(self):
        self.add_line('e0', (31, 8), (37, 8))
        self.add_line('e1', (38, 40), (11, 40))
        self.add_line('e2', (10, 8), (31, 8))
        self.add_line('e3', (31, 8), (19, 40))
        self.add_bezier('e4', (37, 8), ((37.255, 8), (37.236, 8.046), (37.491, 8.046)), ((40.118, 8.046), (42.473, 12.091), (43.509, 18.149)), ((43.727, 19.406), (43.982, 20.846), (43.982, 22.24)), ((43.991, 22.578), (44, 22.893), (44, 23.23)), ((44, 23.235), (44, 23.24), (44, 23.246)), ((43.991, 23.566), (43.991, 23.909), (43.982, 24.229)), ((43.982, 31.177), (40.745, 40), (38, 40)))
        self.add_bezier('e5', (11, 40), ((10.855, 40), (10.973, 40), (10.827, 39.977)), ((8.091, 39.977), (5.855, 35.291), (4.664, 29.394)), ((4.327, 27.726), (4.009, 25.92), (4.009, 24)), ((4, 23.817), (4, 23.634), (4, 23.429)), ((4, 23.426), (4, 23.423), (4, 23.42)), ((4, 23.24), (4, 23.06), (4, 22.88)), ((4, 16.343), (7.591, 8), (10.145, 8)), ((10.218, 8), (9.927, 8), (10, 8)))
        self.add_contour('c0', 'e0', 'e4', 'e1', 'e5', 'e2', 'e3')
