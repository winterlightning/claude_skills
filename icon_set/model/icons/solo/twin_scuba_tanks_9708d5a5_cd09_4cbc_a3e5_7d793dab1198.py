"""Twin Scuba Tanks. Matched domed cylinders joined by a hose; omit shoulder bands and hanging regulator for clearance.
Keyshape VRECT_L, visible extremes (6, 2, 42, 46); centerline envelope inset by 2.
Construction: Lucide caravan: repeated rounded enclosure geometry. Source establishes the subject and pose.
Shared circles and rounded rectangles keep repeated radii coherent."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9708d5a5-cd09-4cbc-a3e5-7d793dab1198'
SOURCE_PATH = 'pictographic-primitives/recreation/diving oxygen tank_9708d5a5-cd09-4cbc-a3e5-7d793dab1198.svg'
AUTHOR = 'gpt-6'


class TwinScubaTanks(Solo48):
    icon_id = 'twin-scuba-tanks'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "recreation"
    aliases = ()
    keywords = ('twin', 'scuba', 'tanks')

    def build(self) -> None:
        self.add_arc('left-dome', (8, 23), (18, 23), radius_x=5, radius_y=7, sweep=True)
        self.add_line('left-wall-1', (18, 23), (18, 44))
        self.add_line('left-wall-2', (18, 44), (8, 44))
        self.add_line('left-wall-3', (8, 44), (8, 23))
        self.add_contour('left', 'left-dome', 'left-wall-1', 'left-wall-2', 'left-wall-3', closed=True)
        self.add_arc('right-dome', (30, 23), (40, 23), radius_x=5, radius_y=7, sweep=True)
        self.add_line('right-wall-1', (40, 23), (40, 44))
        self.add_line('right-wall-2', (40, 44), (30, 44))
        self.add_line('right-wall-3', (30, 44), (30, 23))
        self.add_contour('right', 'right-dome', 'right-wall-1', 'right-wall-2', 'right-wall-3', closed=True)
        self.add_line('valve-left', (13, 16), (13, 9))
        self.add_line('valve-right', (35, 16), (35, 9))
        self.relate("connect", 'valve-left', 'left')
        self.relate("connect", 'valve-right', 'right')
        self.add_arc('hose', (13, 9), (35, 9), radius_x=11, radius_y=5, sweep=True)
        self.relate("connect", 'hose', 'valve-left')
        self.relate("connect", 'hose', 'valve-right')
