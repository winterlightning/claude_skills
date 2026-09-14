"""Server choose (servers), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '778556a1-f207-5e49-9e02-977c5f493d53'
SOURCE_PATH = 'icons-json/servers/server choose_778556a1-f207-5e49-9e02-977c5f493d53.json'
AUTHOR = 'json_to_solo'

class ServerChooseServers(Solo48):
    icon_id = 'server-choose-servers'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'servers'
    aliases = ()
    keywords = ('server', 'choose', 'servers')

    def build(self):
        self.add_line('e0', (39, 40), (10, 40))
        self.add_line('e1', (40, 29), (8, 29))
        self.add_line('e2', (39, 8), (10, 8))
        self.add_line('e3', (40, 19), (8, 19))
        self.add_bezier('e4', (40, 29), ((41.836, 30.347), (43.991, 31.848), (43.991, 34.206)), ((43.991, 34.274), (44, 34.341), (44, 34.417)), ((43.991, 34.476), (43.991, 34.543), (43.982, 34.611)), ((43.982, 37.154), (41.827, 40), (39, 40)))
        self.add_bezier('e5', (10, 40), ((9.727, 40), (9.818, 39.983), (9.555, 39.983)), ((6.382, 39.983), (4, 37.886), (4, 34.939)), ((4, 34.737), (4.018, 34.535), (4.018, 34.333)), ((4.018, 31.747), (5.991, 30.549), (8, 29)))
        self.add_bezier('e6', (40, 29), ((41.873, 27.72), (43.991, 26.787), (43.991, 24.354)), ((43.991, 24.168), (44, 23.983), (44, 23.798)), ((44, 23.604), (43.982, 23.411), (43.982, 23.217)), ((43.982, 22.998), (43.836, 22.703), (43.764, 22.484)), ((43.2, 20.825), (41.4, 20.069), (40, 19)))
        self.add_bezier('e7', (40, 19), ((41.464, 17.872), (43.982, 16.135), (43.982, 14.164)), ((43.991, 14.029), (43.991, 13.895), (44, 13.76)), ((44, 13.759), (44, 13.758), (44, 13.756)), ((44, 13.682), (44, 13.616), (43.991, 13.541)), ((43.991, 11.503), (42.245, 9.415), (40.327, 8.539)), ((39.755, 8.286), (39.6, 8.16), (39, 8)))
        self.add_bezier('e8', (10, 8), ((9.818, 8), (10, 8.017), (9.818, 8.017)), ((6.9, 8.017), (4.018, 10.189), (4.018, 13.019)), ((4.018, 13.229), (4, 13.432), (4, 13.642)), ((4, 13.878), (4.009, 14.105), (4.009, 14.333)), ((4.009, 16.547), (6.282, 17.829), (8, 19)))
        self.add_bezier('e9', (8, 19), ((6.173, 20.229), (4.009, 21.229), (4.009, 23.545)), ((4.009, 23.739), (4, 23.924), (4, 24.118)), ((4, 24.12), (4, 24.122), (4, 24.124)), ((4, 24.248), (4, 24.381), (4, 24.505)), ((4, 26.712), (6.273, 27.838), (8, 29)))
        self.add_contour('c0', 'e4', 'e0', 'e5')
        self.add_contour('c1', 'e6')
        self.add_contour('c2', 'e1')
        self.add_contour('c3', 'e7', 'e2', 'e8')
        self.add_contour('c4', 'e3')
        self.add_contour('c5', 'e9')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
