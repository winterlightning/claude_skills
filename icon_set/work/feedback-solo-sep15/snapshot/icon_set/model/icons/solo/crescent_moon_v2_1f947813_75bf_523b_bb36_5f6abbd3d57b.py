"""Redraw the crescent as two tangent circular arcs with generous middle width and clear rounded tips. Independent feedback revision; parent preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1f947813-75bf-523b-bb36-5f6abbd3d57b'
SOURCE_PATH = 'pictographic-primitives/culture/batch-02/astrology moon_1f947813-75bf-523b-bb36-5f6abbd3d57b.svg'
AUTHOR = 'gpt-6'

class CrescentMoonVariant2(Solo48):
    icon_id = 'crescent-moon-v2'
    variant_of = 'crescent-moon'
    variant_label = 'Redraw the crescent as two tangent circular arcs with generous middle width and clear rounded tips.'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/culture'
    aliases = ()
    keywords = ('moon', 'crescent', 'lunar', 'night', 'astrology', 'symbol', 'sky', 'phase')

    def build(self):
        """Symbol plan: Redraw the crescent as two tangent circular arcs with generous middle width and clear rounded tips. Reference: Lucide moon: two clean opposing arcs and a legible crescent opening."""

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
        self.add_arc('outer', (24, 4), (44, 24), radius_x=20, sweep=False, large_arc=True)
        self.add_arc('inner', (44, 24), (24, 4), radius_x=20, sweep=True)
        self.add_contour('crescent', 'outer', 'inner', closed=True)
