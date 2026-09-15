"""Replace the pointed lower jaw with a true horizontal oval while retaining the eye style. Applied to the original icon identity."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '194e70a7-f921-4957-b6e3-e9ba0cf49902'
SOURCE_PATH = 'pictographic-primitives/science/fiction alien_194e70a7-f921-4957-b6e3-e9ba0cf49902.svg'
AUTHOR = 'gpt-6'

class AlienHeadAngularEyes(Solo48):
    icon_id = 'alien-head-angular-eyes'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/science'
    aliases = ()
    keywords = ('alien', 'face', 'head', 'eyes', 'extraterrestrial', 'fiction')

    def segments(self, name, *points):
        for i, (a, b) in enumerate(zip(points, points[1:]), 1):
            self.add_line(f'{name}-{i}', a, b)

    def circle(self, name, x, y, r):
        points = [(x - r, y), (x, y - r), (x + r, y), (x, y + r)]
        for i, start in enumerate(points):
            self.add_arc(f'{name}-{i}', start, points[(i + 1) % 4], radius_x=r)
        self.add_contour(name, *(f'{name}-{i}' for i in range(4)), closed=True)

    def build(self):
        """Symbol plan: Replace the pointed lower jaw with a true horizontal oval while retaining the eye style. Reference: inspected current parent; no useful exact Lucide match selected."""
        self.add_arc('crown', (4, 24), (44, 24), radius_x=20, radius_y=16)
        self.add_arc('jaw-right', (44, 24), (24, 40), radius_x=20, radius_y=16)
        self.add_arc('jaw-left', (24, 40), (4, 24), radius_x=20, radius_y=16)
        self.add_contour('head', 'crown', 'jaw-right', 'jaw-left', closed=True)
        for side in (-1, 1):
            self.add_polyline(f'eye-{side}', (24 + side * 10, 20), (24 + side * 5, 25), (24 + side * 8, 25))
