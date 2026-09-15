"""A video camera looks toward a shopping basket below and right.
SQUARE centerlines (6,6)-(42,42). Lucide cctv informs the camera body/lens;
shopping-basket informs the open handles and broad tapered basket.
Directional asymmetry preserves the scene. Omit the tiny basket slots and
second signal arc to preserve 48px clearance.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f69e1a62-143a-4df3-bede-848fbf7d2e87'
SOURCE_PATH = 'pictographic-primitives/payments/cashless payment camera product scanning basket_f69e1a62-143a-4df3-bede-848fbf7d2e87.svg'
AUTHOR = 'gpt-6'

class CameraScanningShoppingBasket(Solo48):
    icon_id = 'camera-scanning-shopping-basket'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/payments'
    aliases = ()
    keywords = ('camera','shopping','basket','scanning','checkout','cashless')

    def build(self):
        # One body outline with two exact lens attachment nodes.
        self.add_polyline('camera', (16, 8), (16, 6), (6, 6), (6, 18), (16, 18), (16, 16))
        self.add_polyline('lens', (16, 8), (24, 6), (24, 18), (16, 16))
        self.add_line('seam', (16, 8), (16, 16))
        self.relate('connect', 'camera', 'lens')
        self.relate('connect', 'camera', 'seam')
        self.relate('connect', 'lens', 'seam')
        self.add_arc('scan-wave', (34, 8), (42, 16), radius_x=8)
        # Basket owns its mirrored handle and taper dimensions.
        axis=32; half=10; top=30; bottom=42
        self.add_polyline('basket', (axis-half,top), (axis-7,top), (axis+7,top), (axis+half,top), (axis+half-2,bottom), (axis-half+2,bottom), closed=True)
        self.add_polyline('handle', (axis-7,top), (axis,22), (axis+7,top))
        self.relate('connect','basket','handle')
