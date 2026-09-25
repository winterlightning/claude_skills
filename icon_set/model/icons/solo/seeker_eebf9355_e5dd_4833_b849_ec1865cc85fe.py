"""A person with a large search magnifier in front.
Plan: SQUARE accommodates the partial bust and diagonal handle. Visible ink bounds: (4, 4, 44, 44).
Reduction: Right torso edge omitted behind the lens; visible arm line shortened. Head and lens separated, and the handle joins the lens radially.
Construction: Shared human user.svg: circular head and shoulder; Lucide search: round lens with a radial handle."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'eebf9355-e5dd-4833-b849-ec1865cc85fe'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_33/seeker_eebf9355-e5dd-4833-b849-ec1865cc85fe.svg'
AUTHOR = 'gpt-6'
PLAN = 'A person with a large search magnifier in front.'
OMISSIONS = 'Right torso edge omitted behind the lens; visible arm line shortened. Head and lens separated, and the handle joins the lens radially.'
CONSTRUCTION_REFERENCES = 'Shared human user.svg: circular head and shoulder; Lucide search: round lens with a radial handle.'
KEYSHAPE_INK_BOUNDS = (4, 4, 44, 44)

class Drawing(Solo48):
    icon_id = 'seeker'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('seeker',)

    def circle(self, name, cx, cy, r):
        self.add_arc(name + '-top', (cx - r, cy), (cx + r, cy), radius_x=r)
        self.add_arc(name + '-bottom', (cx + r, cy), (cx - r, cy), radius_x=r)
        self.add_contour(name, name + '-top', name + '-bottom', closed=True)

    def build(self):
        self.circle('head', 12, 10, 4)
        self.add_line('body-side', (6, 42), (6, 28))
        self.add_arc('shoulder', (6, 28), (12, 22), radius_x=6)
        self.add_contour('body', 'body-side', 'shoulder')
        self.add_line('arm-edge', (15, 38), (15, 42))
        pts = [(20, 26), (30, 16), (40, 26), (36, 34), (20, 26)]
        for (j, (a, b)) in enumerate(zip(pts, pts[1:])):
            self.add_arc(f'lens-{j}', a, b, radius_x=10)
        self.add_contour('lens', *(f'lens-{j}' for j in range(4)), closed=True)
        self.add_line('handle', (36, 34), (42, 42))
        self.relate('connect', 'lens', 'handle')
