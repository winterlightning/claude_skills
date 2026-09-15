"""Rebuild the robe with two short horizontal rectangular sleeves and a centered collar. Independent feedback revision; parent preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '923e2f6e-dba3-5d20-9662-6b8d78e7b8fc'
SOURCE_PATH = 'pictographic-primitives/spas/bathroom robe_923e2f6e-dba3-5d20-9662-6b8d78e7b8fc.svg'
AUTHOR = 'gpt-6'

class BathrobeVariant2(Solo48):
    icon_id = 'bathrobe-v2'
    variant_of = 'bathrobe'
    variant_label = 'Rebuild the robe with two short horizontal rectangular sleeves and a centered collar.'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/wellness'
    aliases = ()
    keywords = ('spa', 'wellness', 'bathrobe')

    def build(self):
        """Symbol plan: Rebuild the robe with two short horizontal rectangular sleeves and a centered collar. Reference: Lucide shirt: mirrored sleeve and shoulder construction."""

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
        poly('robe', (16, 6), (6, 6), (6, 18), (16, 18), (16, 30), (12, 42), (36, 42), (32, 30), (32, 18), (42, 18), (42, 6), (32, 6), (16, 6), closed=True)
        poly('collar', (16, 6), (24, 18), (32, 6))
        join('collar', 'robe')
        poly('belt', (16, 30), (24, 30), (32, 30))
        join('belt', 'robe')
        line('front', (24, 18), (24, 30))
        join('front', 'collar')
        join('front', 'belt')
