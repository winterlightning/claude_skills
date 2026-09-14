"""Elixir logo (logos), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f9e47a24-4d30-4374-ad67-03f530d919fb'
SOURCE_PATH = 'icons-json/logos/elixir logo_f9e47a24-4d30-4374-ad67-03f530d919fb.json'
AUTHOR = 'json_to_solo'

class ElixirLogo(Solo48):
    icon_id = 'elixir-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('elixir', 'logo', 'logos')

    def build(self):
        self.add_line('e0', (36, 22), (30, 18))
        self.add_bezier('e1', (30, 18), ((27.66, 16.227), (25.29, 11.618), (24.85, 8.918)), ((24.68, 7.836), (24.72, 6.755), (24.85, 5.673)), ((24.92, 5.118), (24.98, 4.555), (25.05, 4)), ((25.041, 4.004), (25.033, 4), (25.024, 4)), ((24.473, 4), (23.921, 4.568), (23.37, 4.845)), ((21.67, 5.7), (19.9, 7.564), (18.63, 8.9)), ((14.07, 13.7), (8.02, 22.773), (8.02, 29.245)), ((8.02, 29.38), (8, 29.505), (8, 29.639)), ((8, 29.641), (8, 29.643), (8, 29.645)), ((8, 29.982), (8.02, 30.318), (8.02, 30.655)), ((8.02, 37.936), (15.79, 43.991), (23.55, 43.991)), ((23.629, 43.991), (23.708, 44), (23.786, 44)), ((23.788, 44), (23.789, 44), (23.79, 44)), ((24.19, 44), (24.6, 43.991), (25, 43.991)), ((32.06, 43.991), (39.99, 38.282), (39.99, 31.536)), ((39.99, 31.339), (40, 31.134), (40, 30.928)), ((40, 30.925), (40, 30.921), (40, 30.918)), ((40, 30.773), (39.98, 30.636), (39.98, 30.491)), ((39.98, 27.982), (38.09, 23.582), (36, 22)))
        self.add_contour('c0', 'e0', 'e1', closed=True)
