"""Refine the horse’s ear, muzzle, and chest so the head reads less like a single horn.
Plan: continuous horse profile with raised ear, muzzle and squared hooves.
SQUARE centerline extremes (6,6)-(42,42).
Lucide: No useful subject-specific match; supplied original guides the silhouette.
Independent variant; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '11fe477f-8b48-5d9e-adf0-2f40df538526'
SOURCE_PATH = 'pictographic-primitives/animals/symbol cavalry_11fe477f-8b48-5d9e-adf0-2f40df538526.svg'
AUTHOR = 'gpt-6'

class HorseVariant2(Solo48):
    icon_id = 'horse-v2'
    variant_of = 'horse'
    variant_label = 'Batch 01: visual refinement'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('horse', 'pony', 'stallion', 'equine', 'cavalry', 'animal', 'riding', 'profile')

    def build(self):

        def path(n, start, commands, closed=False):
            here = start
            members = []
            for j, (kind, end, *args) in enumerate(commands):
                name = f'{n}-{j}'
                if kind == 'L':
                    self.add_line(name, here, end)
                elif kind == 'A':
                    self.add_arc(name, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2])
                elif kind == 'C':
                    self.add_bezier(name, here, (args[0], args[1], end))
                here = end
                members.append(name)
            self.add_contour(n, *members, closed=closed)

        def circle(n, x, y, r):
            path(n, (x - r, y), [('A', (x, y - r), r, r, True), ('A', (x + r, y), r, r, True), ('A', (x, y + r), r, r, True), ('A', (x - r, y), r, r, True)], True)
        line = self.add_line
        poly = self.add_polyline
        dot = self.add_dot
        join = lambda a, b: self.relate('connect', a, b)
        path('horse', (6, 42), [('L', (6, 30)), ('A', (16, 20), 10, 10, True), ('L', (24, 20)), ('A', (30, 14), 6, 6, False), ('L', (30, 6)), ('L', (36, 12)), ('L', (42, 18)), ('L', (42, 26)), ('L', (34, 23)), ('L', (34, 32)), ('A', (32, 34), 2, 2, True), ('L', (32, 42)), ('L', (24, 42)), ('L', (24, 32)), ('L', (14, 32)), ('L', (14, 42)), ('L', (6, 42))], True)
