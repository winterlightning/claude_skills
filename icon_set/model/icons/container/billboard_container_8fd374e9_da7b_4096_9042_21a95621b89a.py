"""Large Display Billboard Sign: independently authored container.

Construction plan: A large rounded sign panel supported by two equal posts and feet.
Keyshape SQUARE; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/business/billboard_8fd374e9-da7b-4096-9042-21a95621b89a.svg. Lucide calendar original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (0, 0, 64, 64).
Hosting measured with compose.py: plus does not clear, heart does not clear, check does not clear.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse

SOURCE_ICON_ID = '8fd374e9-da7b-4096-9042-21a95621b89a'
SOURCE_PATH = 'pictographic-primitives/business/billboard_8fd374e9-da7b-4096-9042-21a95621b89a.svg'
AUTHOR = 'gpt-6'


class BillboardContainer(Container64):
    icon_id = 'billboard-container'
    category = 'business'
    categories = ('business', 'other', 'primitives-generate')
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ('billboard', 'container')

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate('connect',a,b)
        rect(self,'panel',2,2,62,48,5)
        for x in (10,54):
         line(f'post-{x}',(x,48),(x,62));line(f'foot-{x}',(x-6,62),(x+6,62));join('panel',f'post-{x}');join(f'post-{x}',f'foot-{x}')
