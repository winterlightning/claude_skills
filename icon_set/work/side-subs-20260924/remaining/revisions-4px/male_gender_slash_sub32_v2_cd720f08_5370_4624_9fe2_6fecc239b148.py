"""Complete source composition; see the accompanying visual and validation evidence."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.sub._base import Sub32
SOURCE_ICON_ID = 'cd720f08-5370-4624-9fe2-6fecc239b148'
SOURCE_PATH = 'pictographic-primitives/pets/male stablization_cd720f08-5370-4624-9fe2-6fecc239b148.svg'
AUTHOR = 'gpt-6'
REFERENCE_PARTS = ('lower-left circle', 'upper-right arrow with two-stroke head', 'diagonal upper-left to lower-right slash')

class Drawing(Sub32):
    variant_of = 'male-gender-slash-sub32'
    variant_label = 'Uniform 4px readability repair'
    REPAIR_PLAN = {'concept': 'Male Gender Symbol with Slash', 'core_parts': ['lower-left circle', 'upper-right arrow with two-stroke head', 'diagonal upper-left to lower-right slash'], 'flexible_parts': 'Coordinates and proportions only; no parts removed.', 'repair': 'Retain the already readable all-4px symbol unchanged.'}
    icon_id = 'male-gender-slash-sub32-v2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    keywords = ('male', 'gender', 'symbol', 'with', 'slash')

    def build(self):
        self.circle('circle', 12, 20, 10)
        self.add_line('shaft', (18, 12), (30, 2))
        self.add_polyline('arrowhead', (23, 2), (30, 2), (30, 9))
        self.relate('connect', 'shaft', 'arrowhead-1', 'arrowhead-2')
        self.relate('connect', 'shaft', 'circle-top')
        self.add_line('slash', (2, 10), (22, 30))
        self.relate('connect', 'slash', 'circle-top')
        self.relate('connect', 'slash', 'circle-bottom')

    def circle(self, name, cx, cy, r):
        self.add_arc(name + '-top', (cx - r, cy), (cx + r, cy), radius_x=r)
        self.add_arc(name + '-bottom', (cx + r, cy), (cx - r, cy), radius_x=r)
        self.add_contour(name, name + '-top', name + '-bottom', closed=True)
