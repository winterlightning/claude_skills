"""blood bag: fresh SOLO48 repair.
Plan: Rounded bag, cap with shared attachment points, mirrored droplet, vertical outlet with a small tangent turn.
Keyshape: VRECT_M. Tall bag leaves room for the top cap and curved outlet.
Omissions: Lower connector collar omitted; outlet curve shortened.
Construction reference: droplet: pointed crown and rounded bowl.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7d002be2-8db0-591d-9e62-868a56fdf240'
SOURCE_PATH = 'pictographic-primitives/health/blood bag_7d002be2-8db0-591d-9e62-868a56fdf240.svg'
AUTHOR = 'gpt-6'
PARENT_SOURCE = 'icon_set/model/icons/solo/blood_bag_7d002be2_8db0_591d_9e62_868a56fdf240.py'

class Drawing(Solo48):
    icon_id = 'blood-bag-solo'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('blood', 'bag')

    def build(self):
        self.box('bag', 10, 12, 38, 38, 4)
        self.add_line('cap-left', (20, 12), (20, 6))
        self.add_arc('cap-tl', (20, 6), (22, 4), radius_x=2)
        self.add_line('cap-top', (22, 4), (26, 4))
        self.add_arc('cap-tr', (26, 4), (28, 6), radius_x=2)
        self.add_line('cap-right', (28, 6), (28, 12))
        self.add_contour('cap', 'cap-left', 'cap-tl', 'cap-top', 'cap-tr', 'cap-right')
        self.relate('connect', 'bag', 'cap')
        self.add_bezier('drop-left', (24, 21), ((22, 23), (20, 23), (20, 25)))
        self.add_arc('drop-bottom', (20, 25), (28, 25), radius_x=4, sweep=False)
        self.add_bezier('drop-right', (28, 25), ((28, 23), (26, 23), (24, 21)))
        self.add_contour('drop', 'drop-left', 'drop-bottom', 'drop-right', closed=True)
        self.add_line('tube-straight', (24, 38), (24, 42))
        self.add_arc('tube-bend', (24, 42), (26, 44), radius_x=2, sweep=False)
        self.add_contour('tube', 'tube-straight', 'tube-bend')
        self.relate('connect', 'bag', 'tube')

    def box(self, name, left, top, right, bottom, r=3):
        points = [(left + r, top), (right - r, top), (right, top + r), (right, bottom - r), (right - r, bottom), (left + r, bottom), (left, bottom - r), (left, top + r)]
        members = []
        for i, a in enumerate(points):
            b = points[(i + 1) % 8]
            part = f'{name}-{i}'
            if i % 2:
                self.add_arc(part, a, b, radius_x=r)
            else:
                self.add_line(part, a, b)
            members.append(part)
        self.add_contour(name, *members, closed=True)
