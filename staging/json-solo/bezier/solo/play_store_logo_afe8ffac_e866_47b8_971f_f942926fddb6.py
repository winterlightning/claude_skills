"""Play store logo (logos), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'afe8ffac-e866-47b8-971f-f942926fddb6'
SOURCE_PATH = 'icons-json/logos/play store logo_afe8ffac-e866-47b8-971f-f942926fddb6.json'
AUTHOR = 'json_to_solo'

class PlayStoreLogoLogos(Solo48):
    icon_id = 'play-store-logo-logos'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('play', 'store', 'logo', 'logos')

    def build(self):
        self.add_line('e0', (8, 7), (8, 41))
        self.add_line('e1', (12, 44), (38, 27))
        self.add_line('e2', (38, 21), (13, 5))
        self.add_bezier('e3', (13, 5), ((12.453, 4.645), (11.756, 4.009), (11.091, 4.009)), ((11.057, 4.009), (11.024, 4), (10.991, 4)), ((10.991, 4), (10.99, 4), (10.989, 4)), ((10.905, 4), (10.829, 4.009), (10.745, 4.009)), ((9.314, 4.009), (8.421, 5.755), (8, 7)))
        self.add_bezier('e4', (8, 41), ((8, 41.827), (9.272, 43.982), (10.122, 43.982)), ((10.156, 43.991), (10.189, 43.991), (10.232, 44)), ((10.535, 44), (10.846, 43.982), (11.149, 43.982)), ((11.326, 43.982), (11.503, 44), (11.672, 44)), ((11.848, 44), (11.823, 44), (12, 44)))
        self.add_bezier('e5', (38, 27), ((38.488, 26.673), (39.992, 24.727), (39.992, 24.109)), ((39.992, 24.037), (40, 23.975), (40, 23.903)), ((40, 23.902), (40, 23.901), (40, 23.9)), ((40, 23.864), (39.992, 23.818), (39.992, 23.782)), ((39.992, 23.109), (38.514, 21.336), (38, 21)))
        self.add_contour('c0', 'e3', 'e0', 'e4', 'e1', 'e5', 'e2', closed=True)
