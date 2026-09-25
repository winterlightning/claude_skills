"""A left-facing recovery truck with a rising boom and hook. Lucide truck informed cab and wheel construction. Broad keyshape fits the bed; small hubs omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e939427f-b3d8-523c-b7f9-0e367c354fd2'
SOURCE_PATH = 'pictographic-primitives/transportation/car repair tow truck_e939427f-b3d8-523c-b7f9-0e367c354fd2.svg'
SOURCE_REFERENCES = (('e939427f-b3d8-523c-b7f9-0e367c354fd2', 'pictographic-primitives/transportation/car repair tow truck_e939427f-b3d8-523c-b7f9-0e367c354fd2.svg'),)
AUTHOR = 'gpt-6'

class TowTruck(Solo48):
    icon_id = 'tow-truck'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    categories = ('transportation', 'primitives')
    aliases = ()
    keywords = ('tow truck', 'breakdown', 'recovery', 'truck', 'hook', 'roadside assistance', 'repair', 'vehicle')

    def build(self) -> None:
        """Lift the rear deck away from the wheel to open the pinched corner."""
        self.add_polyline('body', (4, 33), (4, 24), (12, 12), (22, 12), (22, 24), (44, 20), (44, 33))
        self.add_line('boom-a', (22, 24), (32, 8))
        self.add_line('boom-b', (32, 8), (44, 8))
        self.add_line('boom-c', (44, 8), (44, 16))
        self.add_arc('hook', (44, 16), (38, 16), radius_x=3)
        self.add_contour('boom', 'boom-a', 'boom-b', 'boom-c', 'hook')
        self.relate('connect', 'boom', 'body')
        for side, x in [('rear', 11), ('front', 37)]:
            self.add_arc(side + '-upper', (x - 7, 33), (x + 7, 33), radius_x=7)
            self.add_arc(side + '-lower', (x + 7, 33), (x - 7, 33), radius_x=7)
            self.add_contour(side + '-wheel', side + '-upper', side + '-lower', closed=True)
        self.add_line('chassis', (18, 33), (30, 33))
        for wheel in ['rear-wheel', 'front-wheel']:
            self.relate('connect', 'body', wheel)
            self.relate('connect', 'chassis', wheel)
