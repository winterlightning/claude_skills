"""Broaden and deepen the cargo box; keep a compact cab and both wheels.
Construction: shared body/attachment coordinates, integer grid, 4-unit stroke.
Lucide originals and atomic-debug references inspected for enclosure, handle and rounded-join construction.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse
SOURCE_ICON_ID = '131a3477-dd9d-4552-84ba-f2f3f7a573ed'
SOURCE_PATH = 'pictographic-primitives/transportation/truck 1_131a3477-dd9d-4552-84ba-f2f3f7a573ed.svg'
AUTHOR = 'gpt-6'

class CargoDeliveryTruckContainer(Container64):
    icon_id = 'cargo-delivery-truck-container'
    category = 'transportation'
    categories = ('transportation', 'primitives')
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ()

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate("connect",a,b)
        path(self,'body',(8,55),[('L',(2,55)),('L',(2,2)),('L',(44,2)),('L',(44,42))])
        path(self,'cab',(44,24),[('L',(52,24)),('A',(62,34),10,10,True),('L',(62,55)),('L',(55,55))]);join('body','cab')
        line('windshield',(52,34),(62,34));join('windshield','cab')
        line('axle',(22,55),(41,55));join('axle','wheel-15')
        for x in (15,48):ellipse(self,f'wheel-{x}',x,55,7)
        join('body','wheel-15');join('cab','wheel-48');join('axle','wheel-48')
