"""A hooded person with a blank circular face.
Plan: VRECT_L follows the tall hood and shoulders. Visible ink bounds: (6, 2, 42, 46).
Reduction: Sleeve lines omitted and jacket seam shortened. Shoulders rebuilt as a centered ellipse with explicit hood attachment nodes.
Construction: Shared human user.svg and human-reference.md: circular face, curved shoulders and touching bust construction."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4eebbb0e-3d47-4014-a9b8-95819896ada8'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_33/rogue_4eebbb0e-3d47-4014-a9b8-95819896ada8.svg'
AUTHOR = 'gpt-6'
PLAN = 'A hooded person with a blank circular face.'
OMISSIONS = 'Sleeve lines omitted and jacket seam shortened. Shoulders rebuilt as a centered ellipse with explicit hood attachment nodes.'
CONSTRUCTION_REFERENCES = 'Shared human user.svg and human-reference.md: circular face, curved shoulders and touching bust construction.'
KEYSHAPE_INK_BOUNDS = (6, 2, 42, 46)

class Drawing(Solo48):
    aliases = ()
    semantic_kind = 'noun'
    semantic_role = 'MAIN'
    icon_id = 'hooded-person-with-blank-face'
    keyshape = Keyshape.VRECT_L
    human_construction = 'bust'
    category = 'objects'
    keywords = ('hooded', 'person', 'with', 'blank', 'face')

    def build(self):

        def path(name, start, steps, closed=False):
            (members, point) = ([], start)
            for (index, step) in enumerate(steps):
                member = f'{name}-{index}'
                if len(step) == 2:
                    self.add_line(member, point, step)
                    point = step
                else:
                    (end, rx, ry, sweep) = step
                    self.add_arc(member, point, end, radius_x=rx, radius_y=ry, sweep=sweep)
                    point = end
                members.append(member)
            self.add_contour(name, *members, closed=closed)

        def ellipse(name, x, y, rx, ry):
            path(name, (x - rx, y), [((x + rx, y), rx, ry, True), ((x - rx, y), rx, ry, True)], True)

        def circle(name, x, y, r):
            ellipse(name, x, y, r, r)

        def box(name, l, t, r, b, rad=4):
            path(name, (l + rad, t), [(r - rad, t), ((r, t + rad), rad, rad, True), (r, b - rad), ((r - rad, b), rad, rad, True), (l + rad, b), ((l, b - rad), rad, rad, True), (l, t + rad), ((l + rad, t), rad, rad, True)], True)
        circle('face', 24, 24, 6)
        self.add_bezier('hood', (15, 36), ((10, 34), (8, 28), (8, 24)), ((8, 16), (18, 4), (24, 4)), ((30, 4), (40, 16), (40, 24)), ((40, 28), (38, 34), (33, 36)))
        self.add_arc('shoulder-left', (9, 44), (15, 36), radius_x=15, radius_y=10)
        self.add_arc('shoulder-center', (15, 36), (33, 36), radius_x=15, radius_y=10)
        self.add_arc('shoulder-right', (33, 36), (39, 44), radius_x=15, radius_y=10)
        self.add_contour('shoulders', 'shoulder-left', 'shoulder-center', 'shoulder-right')
        self.relate('connect', 'hood', 'shoulders')
        self.relate('connect', 'face', 'shoulders')
        self.add_line('seam', (24, 43), (24, 44))
