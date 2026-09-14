"""Pin (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9b4b8603-58f9-4f81-8664-658ab7045658'
SOURCE_PATH = 'icons-json/interface-essential/pin_9b4b8603-58f9-4f81-8664-658ab7045658.json'
AUTHOR = 'json_to_solo'

class Pin(Solo48):
    icon_id = 'pin'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('pin', 'interface-essential')

    def build(self):
        self.add_line('e0', (29, 39), (24, 44))
        self.add_bezier('e1', (24, 44), ((19.436, 39.636), (14.56, 35.291), (11.166, 29.755)), ((9.457, 26.973), (8.017, 23.891), (8.017, 20.455)), ((8.017, 20.168), (8, 19.873), (8, 19.578)), ((8, 19.573), (8, 19.568), (8, 19.564)), ((8, 19.273), (8.017, 18.973), (8.017, 18.682)), ((8.017, 10.636), (16.303, 4.018), (23.309, 4.018)), ((23.508, 4.018), (23.716, 4), (23.915, 4)), ((23.918, 4), (23.921, 4), (23.924, 4)), ((24.202, 4), (24.472, 4.018), (24.749, 4.018)), ((32.337, 4.018), (39.983, 10.918), (39.983, 19.391)), ((39.992, 19.509), (39.992, 19.618), (40, 19.736)), ((40, 19.739), (40, 19.742), (40, 19.745)), ((40, 19.934), (39.983, 20.13), (39.983, 20.318)), ((39.983, 26.327), (36.093, 31.455), (32.522, 35.664)), ((31.419, 36.964), (30.255, 37.873), (29, 39)))
        self.add_dot('e2', (24, 19))
        self.add_contour('c0', 'e0', 'e1', closed=True)
