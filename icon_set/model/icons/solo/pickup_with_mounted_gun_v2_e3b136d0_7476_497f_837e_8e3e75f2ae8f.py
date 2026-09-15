"""Pickup with mounted gun: independent spacing revision.

Separate receiver and cab, move barrel above roof, preserve mounted-gun pickup.
Native solo family, HRECT_XL keyshape. The original model is preserved.
Directional and natural asymmetry follows the supplied subject.
Final construction review: Original subject render; no exact Lucide match selected.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e3b136d0-7476-497f-837e-8e3e75f2ae8f'
SOURCE_PATH = 'pictographic-primitives/war/van machine gun_e3b136d0-7476-497f-837e-8e3e75f2ae8f.svg'
AUTHOR = 'gpt-6'

class PickupWithMountedGunVariant2(Solo48):
    icon_id = 'pickup-with-mounted-gun-v2'
    variant_of = 'pickup-with-mounted-gun'
    variant_label = 'Hole and centerline reconstruction'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/war'
    aliases = ()
    keywords = ('pickup', 'truck', 'gun', 'mounted', 'military', 'vehicle')

    def build(self):
        """Lower and slightly reduce both repeated wheels to clear the bed corners while preserving the mounted gun spacing."""
        self.add_arc('rear-wheela', (6, 35), (16, 35), radius_x=5, radius_y=5)
        self.add_arc('rear-wheelb', (16, 35), (6, 35), radius_x=5, radius_y=5)
        self.add_contour('rear-wheel', 'rear-wheela', 'rear-wheelb', closed=True)
        self.add_arc('front-wheela', (32, 35), (42, 35), radius_x=5, radius_y=5)
        self.add_arc('front-wheelb', (42, 35), (32, 35), radius_x=5, radius_y=5)
        self.add_contour('front-wheel', 'front-wheela', 'front-wheelb', closed=True)
        self.add_polyline('body', (6, 35), (4, 35), (4, 24), (14, 24), (30, 24), (30, 16), (36, 16), (44, 24), (44, 35), (42, 35), closed=False)
        self.add_line('chassis', (16, 35), (32, 35))
        self.add_polyline('gun', (8, 8), (20, 8), (20, 16), (14, 16), (8, 16), closed=True)
        self.add_line('mount', (14, 16), (14, 24))
        self.add_line('barrel', (20, 8), (44, 8))
        self.relate('connect', 'body', 'rear-wheel')
        self.relate('connect', 'body', 'front-wheel')
        self.relate('connect', 'chassis', 'rear-wheel')
        self.relate('connect', 'chassis', 'front-wheel')
        self.relate('connect', 'gun', 'mount')
        self.relate('connect', 'body', 'mount')
        self.relate('connect', 'gun', 'barrel')
