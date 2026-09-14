"""Astrology moon (religion), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6dd077fd-c745-464e-9bfc-be53b27bf22e'
SOURCE_PATH = 'icons-json/religion/astrology moon_6dd077fd-c745-464e-9bfc-be53b27bf22e.json'
AUTHOR = 'json_to_solo'

class AstrologyMoonReligion(Solo48):
    icon_id = 'astrology-moon-religion'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'religion'
    aliases = ()
    keywords = ('astrology', 'moon', 'religion')

    def build(self):
        self.add_line('e0', (8, 42), (14, 40))
        self.add_line('e1', (12, 7), (8, 6))
        self.add_bezier('e2', (8, 6), ((10.97, 5.291), (14.3, 4.018), (17.46, 4.018)), ((17.647, 4.018), (17.834, 4), (18.021, 4)), ((18.024, 4), (18.027, 4), (18.03, 4)), ((18.3, 4), (18.58, 4.018), (18.85, 4.018)), ((20.28, 4.018), (21.75, 4.3), (23.13, 4.6)), ((30.95, 6.273), (37.23, 12.136), (39.3, 19.118)), ((39.68, 20.391), (39.99, 21.755), (39.99, 23.082)), ((39.99, 23.153), (40, 23.216), (40, 23.288)), ((40, 23.289), (40, 23.29), (40, 23.291)), ((40, 23.755), (39.99, 24.209), (39.99, 24.673)), ((39.99, 33.282), (32.73, 40.936), (23.82, 43.2)), ((22.27, 43.591), (20.54, 43.982), (18.92, 43.982)), ((18.61, 43.982), (18.3, 44), (18, 44)), ((17.997, 44), (17.995, 44), (17.992, 44)), ((17.835, 44), (17.677, 43.982), (17.52, 43.982)), ((14.4, 43.982), (10.93, 42.655), (8, 42)))
        self.add_bezier('e3', (14, 40), ((16.32, 39.3), (18.55, 37.827), (20.16, 36.218)), ((27.64, 28.7), (26.63, 16.091), (17.88, 9.745)), ((16.16, 8.5), (14.16, 7.491), (12, 7)))
        self.add_contour('c0', 'e2', 'e0', 'e3', 'e1', closed=True)
