"""Enlarge the head and body; center the head over the upper torso with exactly four visible units of separation. Applied to the original icon identity."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '47d26a02-2221-453b-a560-39c0733c3bec'
SOURCE_PATH = 'pictographic-primitives/sports/athletics running 1_47d26a02-2221-453b-a560-39c0733c3bec.svg'
AUTHOR = 'gpt-6'

class AthleteRunningRight(Solo48):
    icon_id = 'athlete-running-right'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'sports'
    categories = ('sports', 'primitives')
    aliases = ()
    keywords = ('athlete', 'running', 'right')

    def circle(self, name, x, y, radius):
        self.add_arc(name + '-top', (x - radius, y), (x + radius, y), radius_x=radius)
        self.add_arc(name + '-bottom', (x + radius, y), (x - radius, y), radius_x=radius)
        self.add_contour(name, name + '-top', name + '-bottom', closed=True)

    def skeleton(self, branches):
        segments = []
        for name, points in branches:
            for index, (a, b) in enumerate(zip(points, points[1:])):
                key = f'{name}-{index}'
                self.add_line(key, a, b)
                segments.append((key, a, b))
            if len(points) > 2:
                self.add_contour(name, *[f'{name}-{i}' for i in range(len(points) - 1)])
        for index, (a, p, q) in enumerate(segments):
            for b, r, s in segments[index + 1:]:
                if p in (r, s) or q in (r, s):
                    self.relate('connect', a, b)

    def oval(self, name, x, y, rx, ry):
        self.add_arc(name + '-top', (x - rx, y), (x + rx, y), radius_x=rx, radius_y=ry)
        self.add_arc(name + '-bottom', (x + rx, y), (x - rx, y), radius_x=rx, radius_y=ry)
        self.add_contour(name, name + '-top', name + '-bottom', closed=True)

    def build(self):
        """Symbol plan: Enlarge the head and body; center the head over the upper torso with exactly four visible units of separation. Reference: icon_set/references/human_ref/full_body_ref.png: circular head, coherent limbs, exact 4-unit detached head-to-torso gap."""

        def path(n, start, commands, closed=False):
            here = start
            members = []
            for i, c in enumerate(commands):
                kind, end, *args = c
                name = f'{n}-{i}'
                if kind == 'L':
                    self.add_line(name, here, end)
                elif kind == 'A':
                    self.add_arc(name, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2])
                elif kind == 'C':
                    self.add_bezier(name, here, (args[0], args[1], end))
                members.append(name)
                here = end
            self.add_contour(n, *members, closed=closed)

        def oval(n, x, y, rx, ry):
            path(n, (x - rx, y), [('A', (x + rx, y), rx, ry, True), ('A', (x - rx, y), rx, ry, True)], True)

        def box(n, l, t, r, b, rad=4):
            path(n, (l + rad, t), [('L', (r - rad, t)), ('A', (r, t + rad), rad, rad, True), ('L', (r, b - rad)), ('A', (r - rad, b), rad, rad, True), ('L', (l + rad, b)), ('A', (l, b - rad), rad, rad, True), ('L', (l, t + rad)), ('A', (l + rad, t), rad, rad, True)], True)
        line = self.add_line
        poly = self.add_polyline
        dot = self.add_dot
        join = lambda a, b: self.relate('connect', a, b)
        oval('head', 24, 11, 5, 5)
        self.add_bezier('torso', (24, 24), ((24, 27), (21, 30), (18, 32)))
        poly('back-arm', (24, 24), (14, 24), (6, 30))
        poly('front-arm', (24, 24), (34, 24), (42, 16))
        poly('back-leg', (18, 32), (10, 42), (6, 42))
        poly('front-leg', (18, 32), (32, 34), (28, 42))
        for a, b in [('torso', 'back-arm'), ('torso', 'front-arm'), ('back-arm', 'front-arm'), ('torso', 'back-leg'), ('torso', 'front-leg'), ('back-leg', 'front-leg')]:
            join(a, b)
        self.mark_human_figure('runner', head='head', torso='torso', torso_junction='start')
