"""Layers back (design), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f17d8853-9c2e-4620-a59b-8439f073a9b7'
SOURCE_PATH = 'icons-json/design/layers back_f17d8853-9c2e-4620-a59b-8439f073a9b7.json'
AUTHOR = 'json_to_solo'

class LayersBackDesign(Solo48):
    icon_id = 'layers-back-design'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('layers', 'back', 'design')

    def build(self):
        self.add_line('e0', (33, 14), (41, 14))
        self.add_line('e1', (42, 16), (42, 41))
        self.add_line('e2', (41, 42), (16, 42))
        self.add_line('e3', (15, 41), (15, 33))
        self.add_line('e4', (33, 14), (33, 32))
        self.add_line('e5', (32, 33), (15, 33))
        self.add_line('e6', (33, 14), (33, 7))
        self.add_line('e7', (32, 6), (6, 6))
        self.add_line('e8', (6, 7), (6, 32))
        self.add_line('e9', (7, 33), (15, 33))
        self.add_bezier('e10', (41, 14), ((41.36, 14.368), (41.984, 14.812), (41.984, 15.409)), ((41.992, 15.483), (41.992, 15.548), (42, 15.622)), ((42, 15.687), (42, 15.935), (42, 16)))
        self.add_bezier('e11', (42, 41), ((41.935, 41.106), (41.935, 41.444), (41.877, 41.558)), ((41.697, 41.869), (41.254, 41.836), (41, 42)))
        self.add_bezier('e12', (16, 42), ((15.91, 41.926), (15.573, 41.918), (15.475, 41.853)), ((15.262, 41.714), (15.147, 41.205), (15, 41)))
        self.add_bezier('e13', (33, 32), ((32.959, 32.115), (32.91, 32.403), (32.869, 32.517)), ((32.689, 32.828), (32.254, 32.82), (32, 33)))
        self.add_bezier('e14', (33, 7), ((32.836, 6.763), (32.787, 6.303), (32.525, 6.131)), ((32.435, 6.065), (32.074, 6.057), (32, 6)))
        self.add_bezier('e15', (6, 6), ((6, 6.27), (6, 6.73), (6, 7)))
        self.add_bezier('e16', (6, 32), ((6.098, 32.131), (6.074, 32.509), (6.188, 32.648)), ((6.376, 32.861), (6.795, 32.861), (7, 33)))
        self.add_contour('c0', 'e0', 'e10', 'e1', 'e11', 'e2', 'e12', 'e3')
        self.add_contour('c1', 'e4', 'e13', 'e5')
        self.add_contour('c2', 'e6', 'e14', 'e7', 'e15', 'e8', 'e16', 'e9')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
