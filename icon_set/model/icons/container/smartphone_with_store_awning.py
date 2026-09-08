"""A mobile storefront with a striped scalloped awning, bezel and home dash. Three wider scallops replace four narrow ones.

Keyshape: VRECT_L; centerline extremes recorded in build.
Construction reference: Lucide store and smartphone: repeated canopy lobes and rounded phone base.. Mirrored about x=32.
Hosting measured with compose.py: plus blocked, heart blocked, check blocked.
"""
from ...keyshapes import Keyshape
from ._base import Container64


class SmartphoneWithStoreAwning(Container64):
    icon_id = 'smartphone-with-store-awning'
    keyshape = Keyshape.VRECT_L
    aliases = ()
    keywords = ('smartphone', 'with', 'store', 'awning')

    def build(self) -> None:
        # Centerline (10,2)-(54,62).
        self.add_line('canopy-top',(20,2),(44,2))
        self.add_arc('canopy-ne',(44,2),(50,8),radius_x=6)
        self.add_line('canopy-right',(50,8),(54,18))
        self.add_arc('lobe-right',(54,18),(40,18),radius_x=7,radius_y=5)
        self.add_arc('lobe-center',(40,18),(24,18),radius_x=8,radius_y=5)
        self.add_arc('lobe-left',(24,18),(10,18),radius_x=7,radius_y=5)
        self.add_line('canopy-left',(10,18),(14,8))
        self.add_arc('canopy-nw',(14,8),(20,2),radius_x=6)
        self.add_contour('canopy','canopy-top','canopy-ne','canopy-right','lobe-right','lobe-center','lobe-left','canopy-left','canopy-nw',closed=True)
        self.add_line('awning-rule',(14,8),(50,8))
        self.add_line('stripe-left',(27,8),(24,18))
        self.add_line('stripe-right',(37,8),(40,18))
        self.relate('connect','awning-rule','canopy')
        for part in ('stripe-left','stripe-right'):
            self.relate('connect',part,'awning-rule')
            self.relate('connect',part,'canopy')
        self.add_line('body-right',(47,23),(47,56))
        self.add_arc('body-se',(47,56),(41,62),radius_x=6)
        self.add_line('body-base',(41,62),(23,62))
        self.add_arc('body-sw',(23,62),(17,56),radius_x=6)
        self.add_line('body-left',(17,56),(17,23))
        self.add_contour('body','body-right','body-se','body-base','body-sw','body-left')
        self.relate('connect','body','canopy')
        self.add_line('bezel',(17,49),(47,49))
        self.relate('connect','bezel','body')
        self.add_line('home',(30,55),(34,55))
