"""Give the buffalo broader curved horns and a tapered muzzle instead of a flat forehead.
Plan: paired sweeping horns share the cheek nodes; smooth tapered face and eyes.
SQUARE centerline extremes (6,6)-(42,42).
Lucide: No useful subject-specific match; supplied original guides the silhouette.
Independent variant; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'dfa6681e-c282-4464-9e3f-8da4256d4f83'
SOURCE_PATH = 'pictographic-primitives/animals/buffalo_dfa6681e-c282-4464-9e3f-8da4256d4f83.svg'
AUTHOR = 'gpt-6'

class BuffaloHeadVariant2(Solo48):
    icon_id = 'buffalo-head-v2'
    variant_of = 'buffalo-head'
    variant_label = 'Batch 01: visual refinement'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/animals'
    aliases = ()
    keywords = ('buffalo', 'bison', 'head', 'horns', 'cattle', 'animal', 'wildlife', 'ox')

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
        path('face', (12, 18), [('C', (18, 39), (10, 26), (12, 35)), ('A', (30, 39), 6, 3, False), ('C', (36, 18), (36, 35), (38, 26))])
        path('horns', (6, 6), [('C', (12, 18), (6, 15), (8, 18)), ('C', (24, 14), (16, 18), (18, 14)), ('C', (36, 18), (30, 14), (32, 18)), ('C', (42, 6), (40, 18), (42, 15))])
        join('face', 'horns')
        dot('left-eye', (20, 24))
        dot('right-eye', (28, 24))
        line('muzzle', (23, 32), (25, 32))
