"""Bird life (transportation), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dee6f213-07ab-4305-8dd4-d656ac7937ec'
SOURCE_PATH = 'icons-json/transportation/bird life_dee6f213-07ab-4305-8dd4-d656ac7937ec.json'
AUTHOR = 'json_to_solo'

class BirdLifeTransportation(Solo48):
    icon_id = 'bird-life-transportation'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('bird', 'life', 'transportation')

    def build(self):
        self.add_line('e0', (4, 8), (16, 8))
        self.add_line('e1', (32, 8), (44, 8))
        self.add_bezier('e2', (16, 8), ((16, 8), (15.818, 8), (15.818, 8.08)), ((15.873, 8.08), (16.173, 12.16), (16.218, 12.56)), ((16.736, 17.92), (17.364, 22.4), (18.045, 26.08)), ((19.727, 35.36), (21.809, 39.92), (23.791, 39.92)), ((23.925, 39.999), (24.051, 40), (24.185, 40)), ((24.187, 40), (24.189, 40), (24.191, 40)), ((24.327, 40), (24.455, 40), (24.591, 39.92)), ((26.518, 39.92), (28.555, 35.52), (30.173, 26.08)), ((30.864, 22.08), (31.482, 17.12), (31.955, 11.2)), ((31.973, 10.96), (32.155, 8.08), (32.182, 8.08)), ((32.182, 8), (32, 8), (32, 8)))
        self.add_contour('c0', 'e0', 'e2', 'e1')
