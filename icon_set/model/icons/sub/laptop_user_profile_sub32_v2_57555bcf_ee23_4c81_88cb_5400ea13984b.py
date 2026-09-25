"""Complete source composition; see the accompanying visual and validation evidence."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.sub._base import Sub32
SOURCE_ICON_ID = '57555bcf-ee23-4c81-88cb-5400ea13984b'
SOURCE_PATH = 'pictographic-primitives/symbol/laptop person_57555bcf-ee23-4c81-88cb-5400ea13984b.svg'
AUTHOR = 'gpt-6'
REFERENCE_PARTS = ('rounded laptop screen', 'circular outlined user head', 'open curved shoulders', 'trapezoidal laptop base')

class Drawing(Sub32):
    variant_of = 'laptop-user-profile-sub32'
    variant_label = 'Uniform 4px readability repair'
    REPAIR_PLAN = {'concept': 'Laptop User Profile', 'core_parts': ['rounded laptop screen', 'circular outlined user head', 'open curved shoulders', 'trapezoidal laptop base'], 'flexible_parts': 'Coordinates and proportions only; no parts removed.', 'repair': 'Remove base overshoot; test head/shoulder spacing within the complete laptop.'}
    icon_id = 'laptop-user-profile-sub32-v2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    keywords = ('laptop', 'user', 'profile')

    def build(self):
        self.box('screen', 4, 2, 28, 25, 2)
        self.circle('head', 16, 10, 3)
        self.add_bezier('shoulders', (10, 20), ((10, 18.6666666667), (22, 18.6666666667), (22, 20)))
        self.add_line('base-left', (4, 25), (2, 30))
        self.add_line('base-bottom', (2, 30), (30, 30))
        self.add_line('base-right', (30, 30), (28, 25))
        self.add_contour('base', 'base-left', 'base-bottom', 'base-right')

    def circle(self, name, cx, cy, r):
        self.add_arc(name + '-top', (cx - r, cy), (cx + r, cy), radius_x=r)
        self.add_arc(name + '-bottom', (cx + r, cy), (cx - r, cy), radius_x=r)
        self.add_contour(name, name + '-top', name + '-bottom', closed=True)

    def box(self, name, left, top, right, bottom, r):
        points = [(left + r, top), (right - r, top), (right, top + r), (right, bottom - r), (right - r, bottom), (left + r, bottom), (left, bottom - r), (left, top + r)]
        for i, a in enumerate(points):
            b = points[(i + 1) % 8]
            if i % 2:
                self.add_arc(f'{name}-{i}', a, b, radius_x=r)
            else:
                self.add_line(f'{name}-{i}', a, b)
        self.add_contour(name, *[f'{name}-{i}' for i in range(8)], closed=True)
