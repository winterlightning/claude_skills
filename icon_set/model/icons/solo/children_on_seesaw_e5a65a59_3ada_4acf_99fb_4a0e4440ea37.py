"""Children on seesaw: give both seated figures an actual torso attached to the beam. Shared radius3 heads at(8,17) and(36,11), shoulders(8,28) and(36,22), exact4 painted gaps. Keep the unequal beam heights and central fulcrum; omit the broad ground bar to clear the dangling feet. Source and full_body_ref.png inspected.

Two children sit at opposite ends of a seesaw with circular heads and bent legs. The long plank tilts upward to the right above a central upright support and short foot.

Construction: Two seated children balance a diagonal seesaw on a central pivot. Bounds (4,8)-(44,40).
Lucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e5a65a59-3ada-4acf-99fb-4a0e4440ea37'
SOURCE_PATH = 'pictographic-primitives/wayfinding/family child teeter_e5a65a59-3ada-4acf-99fb-4a0e4440ea37.svg'
AUTHOR = 'gpt-6'

class ChildrenOnSeesaw(Solo48):
    icon_id = 'children-on-seesaw'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('children', 'seesaw', 'play', 'playground', 'balance', 'seat')

    def ring(self, name, x, y, r):
        self.add_arc(name + '-a', (x - r, y), (x + r, y), radius_x=r)
        self.add_arc(name + '-b', (x + r, y), (x - r, y), radius_x=r)
        self.add_contour(name, name + '-a', name + '-b', closed=True)

    def branches(self, branches):
        parts = []
        for name, points in branches:
            members = []
            for i, (a, b) in enumerate(zip(points, points[1:])):
                key = f'{name}-{i}'
                self.add_line(key, a, b)
                members.append(key)
                parts.append((key, a, b))
            if len(members) > 1:
                self.add_contour(name, *members)
        for i, (name, a, b) in enumerate(parts):
            for other, c, d in parts[i + 1:]:
                if a in (c, d) or b in (c, d):
                    self.relate('connect', name, other)

    def build(self):
        """Children on seesaw: give both seated figures an actual torso attached to the beam. Shared radius3 heads at(8,17) and(36,11), shoulders(8,28) and(36,22), exact4 painted gaps. Keep the unequal beam heights and central fulcrum; omit the broad ground bar to clear the dangling feet. Source and full_body_ref.png inspected."""
        for name, c in [('left', (8, 17)), ('right', (36, 11))]:
            self.ring(name + '-head', *c, 3)
        self.add_bezier('left-body', (8, 28), ((8, 31), (10, 33), (12, 34)))
        self.add_bezier('right-body', (36, 22), ((36, 24), (36, 26), (36, 28)))
        self.branches([('left-leg', [(12, 34), (16, 40)]), ('right-leg', [(36, 28), (40, 36)]), ('beam', [(4, 36), (12, 34), (24, 31), (36, 28), (44, 26)]), ('pivot', [(24, 31), (24, 40)])])
        for a, b in [('left-body', 'left-leg-0'), ('left-body', 'beam-0'), ('left-body', 'beam-1'), ('right-body', 'right-leg-0'), ('right-body', 'beam-2'), ('right-body', 'beam-3')]:
            self.relate('connect', a, b)
