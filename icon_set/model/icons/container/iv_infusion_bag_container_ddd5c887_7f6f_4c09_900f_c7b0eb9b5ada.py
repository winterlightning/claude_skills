"""Medical IV Infusion Bag: independently authored container.

Construction plan: Rounded bag shoulder and bottom outlet nozzle with a short delivery tube; no medical glyph.
Keyshape VRECT_L; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/health/blood bag_ddd5c887-7f6f-4c09-900f-c7b0eb9b5ada.svg. Lucide battery-charging original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (8, 0, 56, 64).
Hosting measured with compose.py: plus passes, heart passes, check passes.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse

SOURCE_ICON_ID = 'ddd5c887-7f6f-4c09-900f-c7b0eb9b5ada'
SOURCE_PATH = 'pictographic-primitives/health/blood bag_ddd5c887-7f6f-4c09-900f-c7b0eb9b5ada.svg'
AUTHOR = 'gpt-6'


class IvInfusionBagContainer(Container64):
    icon_id = 'iv-infusion-bag-container'
    category = 'health'
    keyshape = Keyshape.VRECT_L
    aliases = ()
    keywords = ('iv', 'infusion', 'bag', 'container')

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate('connect',a,b)
        path(self,'bag',(22,2),[('L',(42,2)),('A',(54,14),12,12,True),('L',(54,38)),('A',(42,50),12,12,True),('L',(38,50)),('L',(38,56)),('L',(26,56)),('L',(26,50)),('L',(22,50)),('A',(10,38),12,12,True),('L',(10,14)),('A',(22,2),12,12,True)],True)
        line('tube',(32,56),(32,62));join('tube','bag')
