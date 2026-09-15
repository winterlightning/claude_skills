"""A fuel dispenser with a rectangular display and a rising hose and nozzle.

SQUARE: visible (0, 0, 64, 64); centerline (2, 2)-(62, 62).
Reference: batch_05 source render. Lucide fuel hose bend and smartphone rounded enclosure inform the two main contours..
Consolidates both fuel-pump briefs; tiny trigger and redundant inset dash omitted for clearance. Hose stays asymmetrical on the right.
Hosting measured with compose.py: plus: pass; heart: does not clear; check: pass.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'astra-chatgpt'


class GasStationFuelPump(Container64):
    icon_id = "gas-station-fuel-pump"
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ('gas', 'station', 'fuel', 'pump')

    def build(self) -> None:
        self.add_line('body-0', (6, 2), (36, 2))
        self.add_arc('body-1', (36, 2), (40, 6), radius_x=4, sweep=True)
        self.add_line('body-2', (40, 6), (40, 58))
        self.add_arc('body-3', (40, 58), (36, 62), radius_x=4, sweep=True)
        self.add_line('body-4', (36, 62), (6, 62))
        self.add_arc('body-5', (6, 62), (2, 58), radius_x=4, sweep=True)
        self.add_line('body-6', (2, 58), (2, 6))
        self.add_arc('body-7', (2, 6), (6, 2), radius_x=4, sweep=True)
        self.add_contour('body', 'body-0', 'body-1', 'body-2', 'body-3', 'body-4', 'body-5', 'body-6', 'body-7', closed=True)
        self.add_line('display-0', (12, 10), (30, 10))
        self.add_arc('display-1', (30, 10), (32, 12), radius_x=2, sweep=True)
        self.add_line('display-2', (32, 12), (32, 22))
        self.add_arc('display-3', (32, 22), (30, 24), radius_x=2, sweep=True)
        self.add_line('display-4', (30, 24), (12, 24))
        self.add_arc('display-5', (12, 24), (10, 22), radius_x=2, sweep=True)
        self.add_line('display-6', (10, 22), (10, 12))
        self.add_arc('display-7', (10, 12), (12, 10), radius_x=2, sweep=True)
        self.add_contour('display', 'display-0', 'display-1', 'display-2', 'display-3', 'display-4', 'display-5', 'display-6', 'display-7', closed=True)
        self.add_line('hose-out', (40, 46), (43, 46))
        self.add_arc('hose-bend', (43, 46), (52, 37), radius_x=9, sweep=False)
        self.add_line('hose-rise', (52, 37), (52, 16))
        self.add_line('nozzle', (52, 16), (62, 6))
        self.add_contour('hose', 'hose-out', 'hose-bend', 'hose-rise', 'nozzle', closed=False)
        self.relate("connect", 'body', 'hose')
