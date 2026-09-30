"""Widen the pump body and shorten its display to open the lower panel.
Construction: shared body/attachment coordinates, integer grid, 4-unit stroke.
Lucide originals and atomic-debug references inspected for enclosure, handle and rounded-join construction.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (gas-station-fuel-pump SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4. Hand-repaired after the fit: display inset 8 from the body.
"""

from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = 'claude-opus-5-5'


class GasStationFuelPump(Container64):
    icon_id = 'gas-station-fuel-pump'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ()

    def build(self) -> None:
        self.add_line('body-0', (9, 6), (41, 6))
        self.add_arc('body-1', (41, 6), (45, 10), radius_x=4)
        self.add_line('body-2', (45, 10), (45, 54))
        self.add_arc('body-3', (45, 54), (41, 58), radius_x=4)
        self.add_line('body-4', (41, 58), (9, 58))
        self.add_arc('body-5', (9, 58), (6, 54), radius_x=3, radius_y=4)
        self.add_line('body-6', (6, 54), (6, 10))
        self.add_arc('body-7', (6, 10), (9, 6), radius_x=3, radius_y=4)
        self.add_line('display-0', (16, 14), (35, 14))
        self.add_arc('display-1', (35, 14), (37, 16), radius_x=2)
        self.add_line('display-2', (37, 16), (37, 20))
        self.add_arc('display-3', (37, 20), (35, 22), radius_x=2)
        self.add_line('display-4', (35, 22), (16, 22))
        self.add_arc('display-5', (16, 22), (14, 20), radius_x=2)
        self.add_line('display-6', (14, 20), (14, 16))
        self.add_arc('display-7', (14, 16), (16, 14), radius_x=2)
        self.add_line('hose-0', (45, 42), (48, 42))
        self.add_arc('hose-1', (48, 42), (55, 36), radius_x=7, radius_y=6, sweep=False)
        self.add_line('hose-2', (55, 36), (55, 20))
        self.add_line('hose-3', (55, 20), (58, 12))
        self.add_contour('body', 'body-0', 'body-1', 'body-2', 'body-3', 'body-4', 'body-5', 'body-6', 'body-7', closed=True)
        self.add_contour('display', 'display-0', 'display-1', 'display-2', 'display-3', 'display-4', 'display-5', 'display-6', 'display-7', closed=True)
        self.add_contour('hose', 'hose-0', 'hose-1', 'hose-2', 'hose-3')
        self.relate('connect', 'body', 'hose')
