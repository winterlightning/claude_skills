"""Rebuild the seated baby as a larger circular head, short upright torso and bent arms and legs, replacing the cloud-like body outline. Independent feedback revision; parent preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '10921a97-46e3-5bea-b3ba-ce5691a7278c'
SOURCE_PATH = 'pictographic-primitives/babies/baby care body_10921a97-46e3-5bea-b3ba-ce5691a7278c.svg'
AUTHOR = 'gpt-6'

class SittingBabyVariant2(Solo48):
    icon_id = 'sitting-baby-v2'
    variant_of = 'sitting-baby'
    variant_label = 'Rebuild the seated baby as a larger circular head, short upright torso and bent arms and legs, replacing the cloud-like body outline.'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'people/babies'
    aliases = ()
    keywords = ('sitting', 'baby', 'infant', 'nursery')

    def build(self):
        """Symbol plan: Rebuild the seated baby as a larger circular head, short upright torso and bent arms and legs, replacing the cloud-like body outline. Reference: Shared full_body_ref.png: circular head, bent seated limbs, exact 4-unit head-to-torso ink gap."""

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
        oval('head', 24, 13, 7, 7)
        line('torso', (24, 28), (24, 34))
        for name, side in [('left', -1), ('right', 1)]:
            poly('arm-' + name, (24, 28), (24 + side * 10, 28), (24 + side * 14, 20))
            poly('leg-' + name, (24, 34), (24 + side * 10, 42), (24 + side * 18, 42))
            join('arm-' + name, 'torso')
            join('leg-' + name, 'torso')
        join('arm-left', 'arm-right')
        join('leg-left', 'leg-right')
        self.mark_human_figure('baby', head='head', torso='torso', torso_junction='start')
