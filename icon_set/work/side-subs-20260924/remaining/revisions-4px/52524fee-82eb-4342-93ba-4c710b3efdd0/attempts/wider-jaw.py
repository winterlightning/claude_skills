"""Complete source composition; see the accompanying visual and validation evidence."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.sub._base import Sub32
SOURCE_ICON_ID = '52524fee-82eb-4342-93ba-4c710b3efdd0'
SOURCE_PATH = 'pictographic-primitives/other/circle skull xmark_52524fee-82eb-4342-93ba-4c710b3efdd0.svg'
AUTHOR = 'gpt-6'
REFERENCE_PARTS = ('outer circle', 'skull cranium and closed jaw', 'two eye dots', 'one central jaw divider', 'four diagonal marks behind skull')

class Drawing(Sub32):
    variant_of = 'circle-skull-crossbones-sub32'
    variant_label = 'Uniform 4px readability repair'
    REPAIR_PLAN = {'concept': 'Skull and Crossbones Danger Circle', 'core_parts': ['outer circle', 'skull cranium and closed jaw', 'two eye dots', 'one central jaw divider', 'four diagonal marks behind skull'], 'flexible_parts': 'Coordinates and proportions only; no parts removed.', 'repair': 'Raise both eye dots to separate them from the jaw and divider; preserve all four diagonals.'}
    icon_id = 'circle-skull-crossbones-sub32-v2'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    keywords = ('skull', 'and', 'crossbones', 'danger', 'circle')

    def build(self):
        self.circle('frame', 16, 16, 14)
        for name, a, b in [('bone-tl', (9, 9), (11, 11)), ('bone-tr', (23, 9), (21, 11)), ('bone-bl', (9, 23), (12, 20)), ('bone-br', (23, 23), (20, 20))]:
            self.add_line(name, a, b)
        self.skull(top=11, bottom=23)

    def circle(self, name, cx, cy, r):
        self.add_arc(name + '-top', (cx - r, cy), (cx + r, cy), radius_x=r)
        self.add_arc(name + '-bottom', (cx + r, cy), (cx - r, cy), radius_x=r)
        self.add_contour(name, name + '-top', name + '-bottom', closed=True)

    def skull(self, top=9, bottom=23, open_jaw=False):
        self.add_bezier('cranium', (10, bottom), ((10, bottom - 1), (10, bottom - 3), (9, bottom - 3)), ((8, bottom - 4), (8, top + 6), (9, top + 3)), ((10, top - 1), (14, top - 2), (16, top - 2)), ((18, top - 2), (22, top - 1), (23, top + 3)), ((24, top + 6), (24, bottom - 4), (23, bottom - 3)), ((22, bottom - 3), (22, bottom - 1), (22, bottom)))
        if not open_jaw:
            self.add_line('jaw-bottom', (22, bottom), (10, bottom))
            self.add_contour('skull', 'cranium', 'jaw-bottom', closed=True)
        self.add_dot('eye-left', (13, 15))
        self.add_dot('eye-right', (19, 15))
        self.add_line('tooth', (16, bottom - 3), (16, bottom))
        if not open_jaw:
            self.relate('connect', 'tooth', 'jaw-bottom')
