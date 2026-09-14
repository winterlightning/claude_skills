"""Mixx logo (logos), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c4faef03-bf60-4793-81d2-30d756ff9f80'
SOURCE_PATH = 'icons-json/logos/mixx logo_c4faef03-bf60-4793-81d2-30d756ff9f80.json'
AUTHOR = 'json_to_solo'

class MixxLogoLogos(Solo48):
    icon_id = 'mixx-logo-logos'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('mixx', 'logo', 'logos')

    def build(self):
        self.add_line('e0', (20, 18), (12, 18))
        self.add_line('e1', (12, 18), (12, 40))
        self.add_line('e2', (12, 40), (4, 40))
        self.add_line('e3', (4, 40), (4, 8))
        self.add_line('e4', (4, 8), (44, 8))
        self.add_line('e5', (44, 8), (44, 40))
        self.add_line('e6', (44, 40), (36, 40))
        self.add_line('e7', (36, 40), (36, 18))
        self.add_line('e8', (36, 18), (28, 18))
        self.add_line('e9', (28, 18), (28, 40))
        self.add_line('e10', (28, 40), (20, 40))
        self.add_line('e11', (20, 40), (20, 18))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9', 'e10', 'e11', closed=True)
