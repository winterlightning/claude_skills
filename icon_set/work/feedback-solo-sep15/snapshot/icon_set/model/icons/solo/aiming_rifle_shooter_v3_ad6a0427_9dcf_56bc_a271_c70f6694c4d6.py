"""Enlarge the shooter head and align it above the torso; preserve the horizontal aiming direction. Independent feedback revision; parent preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ad6a0427-9dcf-56bc-a271-c70f6694c4d6'
SOURCE_PATH = 'pictographic-primitives/sports/shooting rifle person aim_ad6a0427-9dcf-56bc-a271-c70f6694c4d6.svg'
AUTHOR = 'gpt-6'

class AimingRifleShooterVariant3(Solo48):
    icon_id = 'aiming-rifle-shooter-v3'
    variant_of = 'aiming-rifle-shooter'
    variant_label = 'Enlarge the shooter head and align it above the torso; preserve the horizontal aiming direction.'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/sports'
    aliases = ()
    keywords = ('shooting', 'rifle', 'shooter', 'aim', 'target', 'sport')

    def build(self):
        """Symbol plan: Enlarge the shooter head and align it above the torso; preserve the horizontal aiming direction. Reference: icon_set/references/human_ref/full_body_ref.png: circular head, coherent limbs, exact 4-unit detached head-to-torso gap."""

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
        oval('head', 12, 11, 5, 5)
        line('torso', (12, 24), (12, 31))
        poly('legs', (6, 42), (12, 31), (18, 42))
        join('torso', 'legs')
        poly('rifle', (12, 24), (34, 24), (42, 24))
        join('rifle', 'torso')
        poly('arms', (12, 24), (30, 32), (34, 24))
        join('arms', 'torso')
        join('arms', 'rifle')
        self.mark_human_figure('shooter', head='head', torso='torso', torso_junction='start')
