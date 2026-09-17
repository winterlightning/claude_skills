"""Compact Cargo Delivery Van: independently authored container.

Construction plan: One stepped roof silhouette and two shared-radius wheels. Cargo van keeps a unified body.
Keyshape HRECT_L; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/transportation/truck_3179d20f-4838-4c26-a054-f8bbabbc255f.svg. Lucide truck original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (0, 8, 64, 56).
Hosting measured with compose.py: plus does not clear, heart does not clear, check does not clear.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse

SOURCE_ICON_ID = '3179d20f-4838-4c26-a054-f8bbabbc255f'
SOURCE_PATH = 'pictographic-primitives/transportation/truck_3179d20f-4838-4c26-a054-f8bbabbc255f.svg'
AUTHOR = 'gpt-6'


class DeliveryVanContainer(Container64):
    icon_id = 'delivery-van-container'
    keyshape = Keyshape.HRECT_L
    aliases = ()
    keywords = ('delivery', 'van', 'container')

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate('connect',a,b)
        path(self,'body',(10,47),[('L',(2,47)),('L',(2,10)),('L',(38,10)),('L',(38,18)),('L',(48,18)),('L',(62,34)),('L',(62,47)),('L',(55,47))])
        line('sill',(24,47),(41,47));line('window',(51,34),(62,34));join('window','body')
        for x in (17,48):
            ellipse(self,f'wheel-{x}',x,47,7);join('body',f'wheel-{x}');join('sill',f'wheel-{x}')
