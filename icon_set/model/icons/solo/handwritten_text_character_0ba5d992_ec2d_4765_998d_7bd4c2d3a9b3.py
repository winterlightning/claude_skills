"""Handwritten text character (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0ba5d992-ec2d-4765-998d-7bd4c2d3a9b3'
SOURCE_PATH = 'icons-json/interface-essential/handwritten text character_0ba5d992-ec2d-4765-998d-7bd4c2d3a9b3.json'
AUTHOR = 'json_to_solo'

class HandwrittenTextCharacter(Solo48):
    icon_id = 'handwritten-text-character'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('handwritten', 'text', 'character', 'interface-essential')

    def build(self):
        self.add_line('e0', (21, 13), (22, 25))
        self.add_line('e1', (28, 26), (34, 12))
        self.add_bezier('e2', (6, 42), ((7.628, 32.681), (8.733, 23.157), (11.269, 14.018)), ((11.899, 11.76), (13.364, 6.008), (16.342, 6.008)), ((16.414, 6.008), (16.487, 6), (16.559, 6)), ((16.56, 6), (16.562, 6), (16.563, 6)), ((16.604, 6), (16.645, 6.008), (16.694, 6.008)), ((19.263, 6.008), (20.73, 10.963), (21, 13)))
        self.add_bezier('e3', (22, 25), ((22.188, 26.407), (23.141, 29.269), (24.573, 29.834)), ((26.234, 30.488), (27.525, 27.219), (28, 26)))
        self.add_bezier('e4', (34, 12), ((34.605, 10.437), (36.559, 6.008), (38.449, 6.008)), ((38.49, 6.008), (38.523, 6), (38.564, 6)), ((38.596, 6), (38.637, 6.008), (38.67, 6.008)), ((39.578, 6.008), (40.282, 6.957), (40.642, 7.677)), ((41.583, 9.584), (41.624, 11.965), (41.697, 14.051)), ((41.902, 19.565), (41.435, 25.088), (41.64, 30.595)), ((41.722, 32.845), (41.648, 35.103), (41.73, 37.361)), ((41.787, 38.858), (41.984, 40.38), (41.984, 41.877)), ((41.992, 41.918), (41.992, 41.959), (42, 42)))
        self.add_contour('c0', 'e2', 'e0', 'e3', 'e1', 'e4')
