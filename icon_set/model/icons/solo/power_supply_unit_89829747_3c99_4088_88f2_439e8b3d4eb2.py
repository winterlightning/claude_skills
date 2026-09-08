"""A power supply rear panel has a cross-braced fan and a rectangular socket.

Keyshape HRECT_L: visible extremes (0, 6, 48, 42).
Landscape keyshape preserves side-by-side hardware. Lucide monitor informs the simple panel. Source arrangement is intentionally asymmetric."""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '89829747-3c99-4088-88f2-439e8b3d4eb2'
SOURCE_PATH = 'pictographic-primitives/computers/batch-06/power supply_89829747-3c99-4088-88f2-439e8b3d4eb2.svg'


class PowerSupplyUnit(Solo48):
    icon_id = 'power-supply-unit'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ()
    keywords = ('power supply', 'psu', 'computer', 'fan', 'hardware', 'socket', 'electricity', 'component')

    def build(self) -> None:
        self.add_line('panel-top0', (4, 8), (44, 8))
        self.add_arc('panel-ne', (44, 8), (46, 10), radius_x=2, sweep=True)
        self.add_line('panel-right', (46, 10), (46, 38))
        self.add_arc('panel-se', (46, 38), (44, 40), radius_x=2, sweep=True)
        self.add_line('panel-bottom0', (44, 40), (4, 40))
        self.add_arc('panel-sw', (4, 40), (2, 38), radius_x=2, sweep=True)
        self.add_line('panel-left', (2, 38), (2, 10))
        self.add_arc('panel-nw', (2, 10), (4, 8), radius_x=2, sweep=True)
        self.add_contour('panel', 'panel-top0', 'panel-ne', 'panel-right', 'panel-se', 'panel-bottom0', 'panel-sw', 'panel-left', 'panel-nw', closed=True)
        self.add_arc('fan0', (25, 24), (17, 32), radius_x=8, sweep=True)
        self.add_arc('fan1', (17, 32), (9, 24), radius_x=8, sweep=True)
        self.add_arc('fan2', (9, 24), (17, 16), radius_x=8, sweep=True)
        self.add_arc('fan3', (17, 16), (25, 24), radius_x=8, sweep=True)
        self.add_contour('fan', 'fan0', 'fan1', 'fan2', 'fan3', closed=True)
        self.add_line('fan-horizontal', (9, 24), (25, 24))
        self.add_line('fan-vertical', (17, 16), (17, 32))
        self.relate("connect", 'fan', 'fan-horizontal')
        self.relate("connect", 'fan', 'fan-vertical')
        self.relate("connect", 'fan-horizontal', 'fan-vertical')
        self.add_polyline('socket', (32, 19), (39, 19), (39, 29), (32, 29), closed=True)
