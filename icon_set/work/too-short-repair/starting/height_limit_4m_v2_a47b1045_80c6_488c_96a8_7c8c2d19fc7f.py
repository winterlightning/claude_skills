# Variant of height-limit-4m; parent file remains unchanged.
"""A 4M vertical clearance sign with inward chevrons. VRECT_L ink (6,6)-(42,42). Lucide type informs monoline letter construction; lettering remains asymmetric and chevrons mirror vertically."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a47b1045-80c6-488c-96a8-7c8c2d19fc7f'
SOURCE_PATH = 'pictographic-primitives/transportation/4m high_a47b1045-80c6-488c-96a8-7c8c2d19fc7f.svg'
AUTHOR = 'gpt-6'

class HeightLimit4MVariant2(Solo48):
    icon_id = 'height-limit-4m-v2'
    variant_of = 'height-limit-4m'
    variant_label = 'Height envelope and full spacing repair'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('height', 'limit', 'clearance', 'restriction', '4m', 'road sign', 'vehicle', 'traffic')

    def build(self) -> None:
        self.add_polyline('top-chevron', (19, 6), (24, 9), (29, 6))
        self.add_polyline('bottom-chevron', (19, 42), (24, 39), (29, 42))
        self.add_polyline('four', (8, 18), (8, 26), (18, 26), (18, 18), (18, 30))
        self.add_polyline('metres', (26, 30), (26, 18), (33, 25), (40, 18), (40, 30))
