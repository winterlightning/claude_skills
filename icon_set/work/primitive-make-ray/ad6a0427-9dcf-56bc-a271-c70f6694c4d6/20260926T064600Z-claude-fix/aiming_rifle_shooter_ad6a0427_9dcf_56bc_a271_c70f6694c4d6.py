"""Enlarge the shooter head and align it above the torso; preserve the horizontal aiming direction. Applied to the original icon identity."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'ad6a0427-9dcf-56bc-a271-c70f6694c4d6'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__aiming-rifle-shooter/20260926T064521Z-thuan-mac/reference/shooting rifle person aim_ad6a0427-9dcf-56bc-a271-c70f6694c4d6.svg'
AUTHOR = "claude-opus-5-5"

class AimingRifleShooter(Solo48):
    icon_id = 'aiming-rifle-shooter'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'sports'
    categories = ('sports', 'primitives')
    aliases = ()
    keywords = ('shooting', 'rifle', 'shooter', 'aim', 'target', 'sport')

    def build(self):
        """Revision per review: the arm triangle is shorter and closer to the body - elbow (22, 32), hand on the stock at (28, 24) instead of (30, 32)/(34, 24); the front leg is steeper ((12, 31) to (16, 42)) so the arm and leg diverge by more than 30 degrees and the elbow stays 9 from it. Symbol plan: Enlarge the shooter head and align it above the torso; preserve the horizontal aiming direction. Reference: icon_set/references/human_ref/full_body_ref.png: circular head, coherent limbs, exact 4-unit detached head-to-torso gap."""

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
        poly('legs', (6, 42), (12, 31), (16, 42))
        join('torso', 'legs')
        poly('rifle', (12, 24), (28, 24), (42, 24))
        join('rifle', 'torso')
        poly('arms', (12, 24), (22, 32), (28, 24))
        join('arms', 'torso')
        join('arms', 'rifle')
        self.mark_human_figure('shooter', head='head', torso='torso', torso_junction='start')
