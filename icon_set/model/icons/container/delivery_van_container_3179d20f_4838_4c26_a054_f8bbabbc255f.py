"""Increase van body height, retaining the stepped roof, sloping windshield and wheels.
Construction: shared body/attachment coordinates, integer grid, 4-unit stroke.
Lucide originals and atomic-debug references inspected for enclosure, handle and rounded-join construction.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse
SOURCE_ICON_ID = '3179d20f-4838-4c26-a054-f8bbabbc255f'
SOURCE_PATH = 'pictographic-primitives/transportation/truck_3179d20f-4838-4c26-a054-f8bbabbc255f.svg'
AUTHOR = 'gpt-6'

class DeliveryVanContainer(Container64):
    icon_id = 'delivery-van-container'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ()

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate("connect",a,b)
        path(self,'body',(8,55),[('L',(2,55)),('L',(2,2)),('L',(46,2)),('L',(46,18)),('L',(50,18)),('L',(62,34)),('L',(62,55)),('L',(55,55))])
        line('sill',(22,55),(41,55));line('window',(51,34),(62,34));join('window','body')
        for x in (15,48):
         ellipse(self,f'wheel-{x}',x,55,7);join('body',f'wheel-{x}');join('sill',f'wheel-{x}')
