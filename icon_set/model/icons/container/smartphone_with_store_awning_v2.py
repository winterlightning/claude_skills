# Variant of smartphone-with-store-awning; parent file remains unchanged.
'Smartphone with store awning: independent spacing revision.\n\nEight-unit canopy band; remove bezel stripe and move home mark clear of phone base.\nNative container family, VRECT_L keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: Original subject render; no exact Lucide match selected.\n'
from ...keyshapes import Keyshape
from ._base import Container64
AUTHOR = 'gpt-6'

class SmartphoneWithStoreAwningVariant2(Container64):
    icon_id = 'smartphone-with-store-awning-v2'
    variant_of = 'smartphone-with-store-awning'
    variant_label = 'Roomier spacing — remaining review'
    keyshape = Keyshape.VRECT_L
    aliases = ()
    keywords = ('smartphone', 'with', 'store', 'awning')

    def build(self) -> None:
        self.add_line('canopy-top', (20, 2), (44, 2))
        self.add_arc('canopy-ne', (44, 2), (50, 10), radius_x=6, radius_y=8)
        self.add_line('canopy-right', (50, 10), (54, 18))
        self.add_arc('lobe-right', (54, 18), (40, 18), radius_x=7, radius_y=5)
        self.add_arc('lobe-center', (40, 18), (24, 18), radius_x=8, radius_y=5)
        self.add_arc('lobe-left', (24, 18), (10, 18), radius_x=7, radius_y=5)
        self.add_line('canopy-left', (10, 18), (14, 10))
        self.add_arc('canopy-nw', (14, 10), (20, 2), radius_x=6, radius_y=8)
        self.add_contour('canopy', 'canopy-top', 'canopy-ne', 'canopy-right', 'lobe-right', 'lobe-center', 'lobe-left', 'canopy-left', 'canopy-nw', closed=True)
        self.add_line('awning-rule', (14, 10), (50, 10))
        self.add_line('stripe-left', (27, 10), (24, 18))
        self.add_line('stripe-right', (37, 10), (40, 18))
        self.relate('connect', 'awning-rule', 'canopy')
        for part in ('stripe-left', 'stripe-right'):
            self.relate('connect', part, 'awning-rule')
            self.relate('connect', part, 'canopy')
        self.add_line('body-right', (47, 23), (47, 56))
        self.add_arc('body-se', (47, 56), (41, 62), radius_x=6)
        self.add_line('body-base', (41, 62), (23, 62))
        self.add_arc('body-sw', (23, 62), (17, 56), radius_x=6)
        self.add_line('body-left', (17, 56), (17, 23))
        self.add_contour('body', 'body-right', 'body-se', 'body-base', 'body-sw', 'body-left')
        self.relate('connect', 'body', 'canopy')
        self.add_line('home', (30, 53), (34, 53))

SOURCE_ICON_ID = None

SOURCE_PATH = None
