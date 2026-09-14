'power-supply-unit: Simplified the fan grille to a ring and the socket to one port stroke to preserve clearance. Keyshape HRECT_L; SOLO48 stroke 4. Reviewed at 48 px in both themes.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '89829747-3c99-4088-88f2-439e8b3d4eb2'
SOURCE_PATH = 'pictographic-primitives/computers/batch-06/power supply_89829747-3c99-4088-88f2-439e8b3d4eb2.svg'
AUTHOR = 'gpt-6'

class PowerSupplyUnit(Solo48):
    icon_id = 'power-supply-unit'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/device'
    aliases = ()
    keywords = ('power supply', 'psu', 'computer', 'fan', 'hardware', 'socket', 'electricity', 'component')

    def build(self) -> None:
        self.add_line('panel-top0', (6, 8), (42, 8))
        self.add_arc('panel-ne', (42, 8), (44, 10), radius_x=2, sweep=True)
        self.add_line('panel-right', (44, 10), (44, 38))
        self.add_arc('panel-se', (44, 38), (42, 40), radius_x=2, sweep=True)
        self.add_line('panel-bottom0', (42, 40), (6, 40))
        self.add_arc('panel-sw', (6, 40), (4, 38), radius_x=2, sweep=True)
        self.add_line('panel-left', (4, 38), (4, 10))
        self.add_arc('panel-nw', (4, 10), (6, 8), radius_x=2, sweep=True)
        self.add_contour('panel', 'panel-top0', 'panel-ne', 'panel-right', 'panel-se', 'panel-bottom0', 'panel-sw', 'panel-left', 'panel-nw', closed=True)
        self.add_arc('fan-top', (14, 24), (26, 24), radius_x=6)
        self.add_arc('fan-bottom', (26, 24), (14, 24), radius_x=6)
        self.add_contour('fan', 'fan-top', 'fan-bottom', closed=True)
        self.add_line('power-port', (35, 19), (35, 29))
