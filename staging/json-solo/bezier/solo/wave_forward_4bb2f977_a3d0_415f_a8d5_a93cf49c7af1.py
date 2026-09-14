"""Wave forward (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4bb2f977-a3d0-415f-a8d5-a93cf49c7af1'
SOURCE_PATH = 'icons-json/interface-essential/wave forward_4bb2f977-a3d0-415f-a8d5-a93cf49c7af1.json'
AUTHOR = 'json_to_solo'

class WaveForward4bb2f977(Solo48):
    icon_id = 'wave-forward-4bb2f977'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('wave', 'forward', 'interface-essential')

    def build(self):
        self.add_bezier('sym-e0', (40, 24), ((40, 23.724), (40, 23.274), (40, 23)))
        self.add_bezier('sym-e1', (40, 23), ((40, 15.927), (34.64, 8.973), (26, 4)))
        self.add_bezier('sym-e2', (8, 11), ((13.895, 14.704), (17, 19.489), (17, 24)))
        self.add_bezier('sym-e3', (17, 24), ((17, 28.511), (13.895, 33.296), (8, 37)))
        self.add_bezier('sym-e4', (40, 24), ((40, 24.276), (40, 24.726), (40, 25)))
        self.add_bezier('sym-e5', (40, 25), ((40, 32.073), (34.64, 39.027), (26, 44)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3')
        self.add_contour('sym-c2', 'sym-e4', 'sym-e5')
        self.relate('connect', 'sym-c0', 'sym-c2')
