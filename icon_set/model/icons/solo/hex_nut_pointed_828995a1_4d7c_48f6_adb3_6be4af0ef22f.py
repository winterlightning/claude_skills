"""An upright hexagonal hardware nut with a central hole. VRECT_L extremes (8,4)-(40,44). Lucide bolt informs the six-sided outline and round center. Preserve pointed top/bottom and mirrored sides; round stroke joins soften the corners."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '828995a1-4d7c-48f6-adb3-6be4af0ef22f'
SOURCE_PATH = 'pictographic-primitives/symbol/nut_828995a1-4d7c-48f6-adb3-6be4af0ef22f.svg'
AUTHOR = 'gpt-6'


class HexNutPointed(Solo48):
    icon_id = 'hex-nut-pointed'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    aliases = ()
    keywords = ('nut', 'hex', 'hardware', 'bolt', 'settings', 'tool', 'mechanical', 'fastener')

    def build(self) -> None:
        self.add_polyline('hexagon',(24,4),(40,14),(40,34),(24,44),(8,34),(8,14),(24,4),closed=True)
        cx, cy, radius = 24, 24, 7
        self.add_arc('hole-top', (cx-radius, cy), (cx+radius, cy), radius_x=radius)
        self.add_arc('hole-bottom', (cx+radius, cy), (cx-radius, cy), radius_x=radius)
        self.add_contour('hole', 'hole-top', 'hole-bottom', closed=True)
