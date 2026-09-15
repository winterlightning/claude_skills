"""A person falls backward above a short flat ground line, with both arms raised. The torso tilts diagonally and the bent legs lift leftward away from the floor.

Construction: Backward-tilted figure throws both arms upward and lifts the feet above a short ground mark. Bounds (6,6)-(42,42).
Lucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '83429111-05e6-413f-a4b9-97c0747e3712'
SOURCE_PATH = 'pictographic-primitives/wayfinding/safety slippery_83429111-05e6-413f-a4b9-97c0747e3712.svg'
AUTHOR = 'gpt-6'

class PersonSlippingVariant2(Solo48):
    icon_id = 'person-slipping-v2'
    variant_of = 'person-slipping'
    variant_label = 'Hole and centerline reconstruction'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/wayfinding'
    aliases = ()
    keywords = ('slipping', 'falling', 'person', 'floor', 'hazard', 'safety')

    def build(self):
        """Lift the extended leg to open the space between the two feet and knees."""
        self.add_arc('person-head-top', (23, 9), (29, 9), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('person-head-bottom', (29, 9), (23, 9), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('person-torso-1', (26,20), (20, 28))
        self.add_line('person-arms-1', (12, 14), (18, 23))
        self.add_line('person-arms-2', (18, 23), (26,20))
        self.add_line('person-arms-3', (26,20), (42,20))
        self.add_line('person-legs-1', (6, 25), (20, 28))
        self.add_line('person-legs-2', (20, 28), (14, 34))
        self.add_line('person-legs-3', (14, 34), (6, 34))
        self.add_line('ground', (6, 42), (14, 42))
        self.add_contour('person-head', 'person-head-top', 'person-head-bottom', closed=True)
        self.add_contour('person-torso', 'person-torso-1', closed=False)
        self.add_contour('person-arms','person-arms-2','person-arms-3')
        self.relate('connect','person-arms-1','person-arms')
        self.add_contour('person-legs', 'person-legs-1', 'person-legs-2', 'person-legs-3', closed=False)
        self.relate('connect', 'person-torso', 'person-arms')
        self.relate('connect', 'person-torso', 'person-legs')
