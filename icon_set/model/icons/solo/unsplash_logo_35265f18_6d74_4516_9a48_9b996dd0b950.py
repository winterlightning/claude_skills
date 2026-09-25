"""Small rectangular camera top above a wide stepped tray. Preserve the two-part silhouette with shared straight offsets."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '35265f18-6d74-4516-9a48-9b996dd0b950'
SOURCE_PATH = 'pictographic-primitives/logos/unsplash logo_35265f18-6d74-4516-9a48-9b996dd0b950.svg'
AUTHOR = 'gpt-6'

class UnsplashLogo(Solo48):
    icon_id = 'unsplash-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('unsplash', 'photos', 'stock', 'camera', 'logo', 'brand', 'images')

    def build(self):
        # Plan: Small rectangular camera top above a wide stepped tray. Preserve the two-part silhouette with shared straight offsets.
        # Exact keyshape ink extremes are owned by Keyshape.HRECT_L on SOLO48.

        self.add_polyline('top',(16,8),(32,8),(32,16),(16,16),closed=True)
        self.add_polyline('tray',(4,24),(12,24),(12,32),(36,32),(36,24),(44,24),(44,40),(4,40),closed=True)

