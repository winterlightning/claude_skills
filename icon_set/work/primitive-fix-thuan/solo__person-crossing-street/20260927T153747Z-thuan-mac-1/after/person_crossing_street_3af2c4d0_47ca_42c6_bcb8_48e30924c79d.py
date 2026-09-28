'person-crossing-street: Restore a walking stride with an upright torso and a row of crossing stripes beneath the pedestrian. Repaired original in place.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '3af2c4d0-47ca-42c6-bcb8-48e30924c79d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-crossing-street/20260927T153747Z-thuan-mac-1/reference/walking cross street_3af2c4d0-47ca-42c6-bcb8-48e30924c79d.svg'
AUTHOR = 'gpt-6'

class PersonCrossingStreet(Solo48):
    icon_id = 'person-crossing-street'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('person', 'crossing', 'street', 'walking', 'pedestrian', 'road')

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
        # A forward walking figure crosses a row of three broad road marks.
        self.add_arc('head-top', (21, 9), (27, 9), radius_x=3)
        self.add_arc('head-bottom', (27, 9), (21, 9), radius_x=3)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_polyline('torso', (24, 20), (24, 26), (23, 28))
        self.add_polyline('arms', (11, 25), (24, 20), (33, 22), (40, 25))
        self.add_polyline('left-leg', (23, 28), (19, 34))
        self.add_polyline('right-leg', (23, 28), (35, 34))
        self.relate('connect', 'arms', 'torso')
        self.relate('connect', 'torso', 'left-leg')
        self.relate('connect', 'torso', 'right-leg')
        for index, (x0, x1) in enumerate(((6, 13), (21, 27), (35, 42))):
            self.add_line(f'crossing-{index}', (x0, 42), (x1, 42))
        self.mark_human_figure('walker', head='head', torso='torso-1', torso_junction='start')
