"""Merge the ear into one clean head outline, open the gap to the branch, and attach the reaching arm at an exact shared point; round the seated body beneath it.
Independent centerline revision; original snapshot preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '95f00a8c-536e-5767-97fa-8968fad8e99a'
SOURCE_PATH = 'pictographic-primitives/animals/koala bamboo_95f00a8c-536e-5767-97fa-8968fad8e99a.svg'
AUTHOR = 'gpt-6'

class KoalaWithBranch(Solo48):
    icon_id = 'koala-with-branch-centerline-v2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ()
    keywords = ('koala', 'branch', 'eucalyptus', 'holding', 'marsupial', 'australia', 'animal', 'sitting')
    variant_of = 'koala-with-branch'
    variant_label = 'Batch 01 centerline repair'

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

        def rounded(n, x0, y0, x1, y1, r):
            path(n, (x0 + r, y0), [('L', (x1 - r, y0)), ('A', (x1, y0 + r), r, r, True), ('L', (x1, y1 - r)), ('A', (x1 - r, y1), r, r, True), ('L', (x0 + r, y1)), ('A', (x0, y1 - r), r, r, True), ('L', (x0, y0 + r)), ('A', (x0 + r, y0), r, r, True)], True)
        line = self.add_line
        poly = self.add_polyline
        dot = self.add_dot
        join = lambda a, b: self.relate('connect', a, b)
        path('head', (20, 8), [('A', (30, 18), 10, 10, True), ('A', (26, 26), 10, 10, True), ('A', (20, 28), 10, 10, True), ('A', (12, 24), 10, 10, True), ('A', (10, 18), 10, 10, True), ('A', (6, 14), 4, 4, True), ('L', (6, 10)), ('A', (10, 6), 4, 4, True), ('L', (16, 6)), ('L', (20, 8))], True)
        dot('nose', (20, 18))
        path('body', (12, 24), [('C', (10, 36), (8, 28), (8, 34)), ('A', (20, 42), 10, 6, False), ('L', (36, 42))])
        join('body', 'head')
        line('branch', (36, 42), (42, 6))
        join('branch', 'body')
        line('arm', (26, 26), (39, 24))
        join('arm', 'head')
        join('arm', 'branch')
