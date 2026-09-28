"""Twin Scuba Tanks. Matched domed cylinders joined by a hose; omit shoulder bands and hanging regulator for clearance.
Keyshape VRECT_L, visible extremes (6, 2, 42, 46); centerline envelope inset by 2.
Construction: Lucide caravan: repeated rounded enclosure geometry. Source establishes the subject and pose.
Shared circles and rounded rectangles keep repeated radii coherent."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '9708d5a5-cd09-4cbc-a3e5-7d793dab1198'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__twin-scuba-tanks/20260927T094425Z-thuan-mac-1/reference/diving oxygen tank_9708d5a5-cd09-4cbc-a3e5-7d793dab1198.svg'
AUTHOR = "gpt-6"
REVISION_COMPARISON = 'The rejected U-shaped hose hid the source’s round pressure gauge.'
REVISION_CHANGE = 'Replaced it with a gauge linked to the right tank, leaving both cylinders distinct.'



class TwinScubaTanks(Solo48):
    icon_id = 'twin-scuba-tanks'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "recreation"
    categories = ("primitives", "recreation")
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
        self.add_arc('gauge-top', (20, 8), (28, 8), radius_x=4, radius_y=4, sweep=True)
        self.add_arc('gauge-bottom', (28, 8), (20, 8), radius_x=4, radius_y=4, sweep=True)
        self.add_contour('gauge', 'gauge-top', 'gauge-bottom', closed=True)
        self.add_line('gauge-hose',(24,12),(35,16))
        self.relate('connect','gauge-hose','gauge')
        self.relate('connect','gauge-hose','right')
