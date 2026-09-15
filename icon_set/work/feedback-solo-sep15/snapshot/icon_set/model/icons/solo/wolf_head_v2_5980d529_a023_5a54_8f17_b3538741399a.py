"""Rebuild the wolf head with a broad pointed ear, sloping forehead, long muzzle and defined lower jaw; keep one clear eye. Independent feedback revision; parent preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5980d529-a023-5a54-8f17-b3538741399a'
SOURCE_PATH = 'pictographic-primitives/animals/wolf_5980d529-a023-5a54-8f17-b3538741399a.svg'
AUTHOR = 'gpt-6'

class WolfHeadVariant2(Solo48):
    icon_id = 'wolf-head-v2'
    variant_of = 'wolf-head'
    variant_label = 'Rebuild the wolf head with a broad pointed ear, sloping forehead, long muzzle and defined lower jaw; keep one clear eye.'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/animals'
    aliases = ()
    keywords = ('wolf', 'head', 'profile', 'minimal', 'snout', 'ear', 'canine', 'dog')

    def build(self):
        """Symbol plan: Rebuild the wolf head with a broad pointed ear, sloping forehead, long muzzle and defined lower jaw; keep one clear eye. Reference: Lucide dog and cat: sparse facial features and a strong ear/muzzle silhouette."""

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
        poly('profile', (6, 42), (8, 24), (14, 6), (24, 16), (32, 18), (36, 24), (42, 26), (38, 34), (30, 34), (22, 42))
        dot('eye', (22, 25))
