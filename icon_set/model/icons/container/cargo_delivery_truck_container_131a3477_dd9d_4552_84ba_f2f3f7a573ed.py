"""Cargo Delivery Truck: independently authored container.

Construction plan: Cargo rectangle and curved cab above two shared-radius wheel circles; deliberately directional.
Keyshape HRECT_L; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/transportation/truck 1_131a3477-dd9d-4552-84ba-f2f3f7a573ed.svg. Lucide truck original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (0, 8, 64, 56).
Hosting measured with compose.py: plus does not clear, heart passes, check passes.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse

SOURCE_ICON_ID = '131a3477-dd9d-4552-84ba-f2f3f7a573ed'
SOURCE_PATH = 'pictographic-primitives/transportation/truck 1_131a3477-dd9d-4552-84ba-f2f3f7a573ed.svg'
AUTHOR = 'gpt-6'


class CargoDeliveryTruckContainer(Container64):
    icon_id = 'cargo-delivery-truck-container'
    keyshape = Keyshape.HRECT_L
    aliases = ()
    keywords = ('cargo', 'delivery', 'truck', 'container')

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate('connect',a,b)
        path(self,'body',(10,47),[('L',(2,47)),('L',(2,10)),('L',(34,10)),('L',(34,47)),('L',(24,47))])
        path(self,'cab',(34,18),[('L',(48,18)),('A',(62,32),14,14,True),('L',(62,47)),('L',(55,47))])
        line('axle',(34,47),(41,47));join('body','axle');join('body','cab')
        line('windshield',(50,32),(62,32));join('windshield','cab')
        for x in (17,48):
         ellipse(self,f'wheel-{x}',x,47,7)
        join('body','wheel-17');join('cab','wheel-48');join('axle','wheel-48')
