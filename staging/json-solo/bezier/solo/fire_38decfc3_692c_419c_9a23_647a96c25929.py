"""Fire (weather), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '38decfc3-692c-419c-9a23-647a96c25929'
SOURCE_PATH = 'icons-json/weather/fire_38decfc3-692c-419c-9a23-647a96c25929.json'
AUTHOR = 'json_to_solo'

class Fire38decfc3(Solo48):
    icon_id = 'fire-38decfc3'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'weather'
    aliases = ()
    keywords = ('fire', 'weather')

    def build(self):
        self.add_line('e0', (17, 16), (12, 21))
        self.add_line('e1', (27, 8), (22, 4))
        self.add_bezier('e2', (22, 4), ((21.83, 5.073), (21.64, 6.8), (21.34, 8.118)), ((20.72, 10.855), (18.96, 13.864), (17, 16)))
        self.add_bezier('e3', (12, 21), ((9.81, 23.391), (8.01, 26.882), (8.01, 30.064)), ((8.01, 30.234), (8, 30.395), (8, 30.565)), ((8, 30.567), (8, 30.57), (8, 30.573)), ((8, 30.745), (8.02, 30.927), (8.02, 31.1)), ((8.02, 38.127), (15.99, 43.991), (23.37, 43.991)), ((23.47, 43.991), (23.56, 44), (23.66, 44)), ((23.663, 44), (23.667, 44), (23.67, 44)), ((23.877, 44), (24.083, 44), (24.29, 44)), ((32.27, 44), (39.99, 37.836), (39.99, 30.391)), ((39.99, 30.301), (40, 30.203), (40, 30.113)), ((40, 30.112), (40, 30.111), (40, 30.109)), ((40, 29.845), (39.99, 29.582), (39.99, 29.318)), ((39.99, 22.436), (32.79, 12.209), (27, 8)))
        self.add_contour('c0', 'e2', 'e0', 'e3', 'e1', closed=True)
