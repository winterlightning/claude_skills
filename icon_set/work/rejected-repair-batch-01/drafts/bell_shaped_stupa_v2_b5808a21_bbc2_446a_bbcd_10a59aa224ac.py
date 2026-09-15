"""Restore the rounded bell dome with a centered finial and a broad plinth.
Plan: round bell dome, central finial, broad attached base.
VRECT_L centerline extremes (8,4)-(40,44).
Lucide: bell; geometric contour construction adapted to SOLO48.
Independent variant; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b5808a21-bbc2-446a-bbcd-10a59aa224ac'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-05/wat phra kaew_b5808a21-bbc2-446a-bbcd-10a59aa224ac.svg'
AUTHOR = 'gpt-6'

class BellShapedStupaVariant2(Solo48):
    icon_id = 'bell-shaped-stupa-v2'
    variant_of = 'bell-shaped-stupa'
    variant_label = 'Batch 01: visual refinement'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/landmarks'
    aliases = ()
    keywords = ('wat phra kaew', 'stupa', 'chedi', 'thailand', 'temple', 'buddhist', 'landmark', 'religion')

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
        path('dome', (8, 36), [('L', (8, 28)), ('A', (24, 12), 16, 16, True), ('A', (40, 28), 16, 16, True), ('L', (40, 36))])
        line('finial', (24, 4), (24, 12))
        join('finial', 'dome')
        poly('base', (8, 36), (8, 44), (40, 44), (40, 36), (8, 36))
        join('dome', 'base')
