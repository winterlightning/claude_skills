"""Make both owl ear tufts truly triangular and mirrored; round the lower face symmetrically and center the eyes and beak. Applied to the original icon identity."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '09901c1f-7237-596c-94c4-12d2991e2fed'
SOURCE_PATH = 'pictographic-primitives/animals/wild bird owl body_09901c1f-7237-596c-94c4-12d2991e2fed.svg'
AUTHOR = 'gpt-6'

class StandingOwl(Solo48):
    icon_id = 'standing-owl'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    categories = ('animals', 'primitives')
    aliases = ()
    keywords = ('owl', 'standing', 'wise', 'bird', 'night', 'feathers', 'nocturnal', 'perch')

    def build(self):
        """Symbol plan: Make both owl ear tufts truly triangular and mirrored; round the lower face symmetrically and center the eyes and beak. Reference: Lucide cat: paired triangular ears and mirrored dot eyes."""

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
        path('owl', (6, 24), [('L', (6, 6)), ('L', (16, 12)), ('L', (32, 12)), ('L', (42, 6)), ('L', (42, 24)), ('A', (24, 42), 18, 18, True), ('A', (6, 24), 18, 18, True)], True)
        for x in [16, 32]:
            dot('eye-' + str(x), (x, 24))
        poly('beak', (22, 31), (24, 33), (26, 31))
