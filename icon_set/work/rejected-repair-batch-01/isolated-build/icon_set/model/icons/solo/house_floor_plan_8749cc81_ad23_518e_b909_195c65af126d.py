"""House Floor Plan. Stepped house footprint with adjoining rooms and interrupted interior walls. Retain one curved door swing; omit the second to keep passageways clear. Deliberately irregular footprint.
Keyshape SQUARE, visible extremes (4, 4, 44, 44); centerline envelope inset by 2.
Construction: Lucide house: coherent structural contour; no useful exact local floor-plan match. Source establishes the subject and pose.
Shared circles and rounded rectangles keep repeated radii coherent."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8749cc81-ad23-518e-b909-195c65af126d'
SOURCE_PATH = 'pictographic-primitives/real-estate/real estate dimensions plan_8749cc81-ad23-518e-b909-195c65af126d.svg'
AUTHOR = 'gpt-6'


class HouseFloorPlan(Solo48):
    icon_id = 'house-floor-plan'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/real-estate"
    aliases = ()
    keywords = ('house', 'floor', 'plan')

    def build(self) -> None:
        self.add_line('perimeter-1', (6, 6), (20, 6))
        self.add_line('perimeter-2', (20, 6), (30, 6))
        self.add_line('perimeter-3', (30, 6), (30, 14))
        self.add_line('perimeter-4', (30, 14), (42, 14))
        self.add_line('perimeter-5', (42, 14), (42, 26))
        self.add_line('perimeter-6', (42, 26), (42, 42))
        self.add_line('perimeter-7', (42, 42), (20, 42))
        self.add_line('perimeter-8', (20, 42), (6, 42))
        self.add_line('perimeter-9', (6, 42), (6, 26))
        self.add_line('perimeter-10', (6, 26), (6, 6))
        self.add_contour('perimeter', 'perimeter-1', 'perimeter-2', 'perimeter-3', 'perimeter-4', 'perimeter-5', 'perimeter-6', 'perimeter-7', 'perimeter-8', 'perimeter-9', 'perimeter-10', closed=True)
        self.add_line('wall-upper', (20, 6), (20, 20))
        self.add_line('wall-lower', (20, 34), (20, 42))
        self.add_line('wall-left', (6, 26), (12, 26))
        self.add_line('wall-right', (28, 26), (42, 26))
        self.relate("connect", 'wall-upper', 'perimeter')
        self.relate("connect", 'wall-lower', 'perimeter')
        self.relate("connect", 'wall-left', 'perimeter')
        self.relate("connect", 'wall-right', 'perimeter')
        self.add_arc('door-swing', (20, 34), (28, 26), radius_x=8, radius_y=8, sweep=False)
        self.relate("connect", 'door-swing', 'wall-lower')
        self.relate("connect", 'door-swing', 'wall-right')
