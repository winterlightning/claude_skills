"""Shorten the reaching arms while retaining a long raised leg; align the circular head with the upper torso. Independent feedback revision; parent preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e0692252-7dbb-4ed1-8ecb-dd659f3bd9b0'
SOURCE_PATH = 'pictographic-primitives/sports/yoga stretch_e0692252-7dbb-4ed1-8ecb-dd659f3bd9b0.svg'
AUTHOR = 'gpt-6'

class BoatPoseUpwardReachVariant2(Solo48):
    icon_id = 'boat-pose-upward-reach-v2'
    variant_of = 'boat-pose-upward-reach'
    variant_label = 'Shorten the reaching arm and lengthen the raised leg; align the head to the torso with an exact four-unit gap.'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/sports'
    aliases = ()
    keywords = ('boat', 'pose', 'upward', 'reach', 'yoga', 'exercise')

    def build(self):
        """Symbol plan: Shorten the reaching arms while retaining a long raised leg; align the circular head with the upper torso. Reference: Shared full_body_ref.png: head bottom23 and torso start31 give exactly four units of visible clearance."""

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
        oval('head', 11, 18, 5, 5)
        self.add_bezier('torso', (11, 31), ((11, 34), (18, 39), (21, 42)))
        line('leg', (21, 42), (42, 6))
        join('torso', 'leg')
        line('arm', (11, 31), (18, 31))
        join('arm', 'torso')
        self.mark_human_figure('person', head='head', torso='torso', torso_junction='start')
