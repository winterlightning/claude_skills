# Variant of smartphone-home-bar-container; parent file remains unchanged.
"""Modern Smartphone Device: independently authored container.

Construction plan: Rounded smartphone with bottom bezel, top earpiece and centered home bar; shared central axis.
Keyshape VRECT_L; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/phones/mobile phone_e676ebab-d256-40ae-9c9a-301b15d45e29.svg. Lucide smartphone original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (8, 0, 56, 64).
Hosting measured with compose.py: plus passes, heart does not clear, check does not clear.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse
SOURCE_ICON_ID = 'e676ebab-d256-40ae-9c9a-301b15d45e29'
SOURCE_PATH = 'pictographic-primitives/phones/mobile phone_e676ebab-d256-40ae-9c9a-301b15d45e29.svg'
AUTHOR = 'gpt-6'

class SmartphoneHomeBarContainerVariant2(Container64):
    icon_id = 'smartphone-home-bar-container-v2'
    variant_of = 'smartphone-home-bar-container'
    variant_label = 'More interior space'
    keyshape = Keyshape.VRECT_L
    aliases = ()
    keywords = ('smartphone', 'home', 'bar', 'container')

    def build(self):
        line, poly = (self.add_line, self.add_polyline)

        def join(a, b):
            self.relate('connect', a, b)
        rect(self, 'phone', 10, 2, 54, 62, 6)
        # Open display: earpiece and home bar retain the phone identity.
        line('speaker', (28, 12), (36, 12))
        line('home', (28, 54), (36, 54))
