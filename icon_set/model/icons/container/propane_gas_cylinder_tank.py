"""Widen and deepen the tank body; shorten the valve neck and base.
Construction: shared body/attachment coordinates, integer grid, 4-unit stroke.
Lucide originals and atomic-debug references inspected for enclosure, handle and rounded-join construction.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse
SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = 'gpt-6'

class PropaneGasCylinderTank(Container64):
    icon_id = 'propane-gas-cylinder-tank'
    keyshape = Keyshape.VRECT_XL
    aliases = ()
    keywords = ()

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate("connect",a,b)
        rect(self,'tank',6,10,58,54,8)
        line('cap',(18,2),(46,2))
        for x in (24,40):line(f'neck-{x}',(x,2),(x,10));join('cap',f'neck-{x}');join('tank',f'neck-{x}')
        path(self,'foot',(18,54),[('L',(10,62)),('L',(54,62)),('L',(46,54))]);join('tank','foot')
