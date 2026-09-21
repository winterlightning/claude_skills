"""Widen the pump body and shorten its display to open the lower panel.
Construction: shared body/attachment coordinates, integer grid, 4-unit stroke.
Lucide originals and atomic-debug references inspected for enclosure, handle and rounded-join construction.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse
SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = 'gpt-6'

class GasStationFuelPump(Container64):
    icon_id = 'gas-station-fuel-pump'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ()

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate("connect",a,b)
        rect(self,'body',2,2,48,62,4)
        rect(self,'display',10,10,40,18,2)
        path(self,'hose',(48,46),[('L',(51,46)),('A',(58,39),7,7,False),('L',(58,16)),('L',(62,8))]);join('body','hose')
