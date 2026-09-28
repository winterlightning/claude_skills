"""Round the document perimeter and folded corner with coherent equal-radius turns. Applied to the original icon identity."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a4b94225-2c9c-42ec-947b-c3b93395b100'
SOURCE_PATH = 'pictographic-primitives/content/document_a4b94225-2c9c-42ec-947b-c3b93395b100.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class DocumentA4b94225(Solo48):
    icon_id = 'document-a4b94225'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'content'
    categories = ('content', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('document', 'content')

    def build(self):
        """Symbol plan: Round the document perimeter and folded corner with coherent equal-radius turns. Reference: inspected current parent; no useful exact Lucide match selected."""

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
        path('paper', (10, 6), [('L', (38, 6)), ('A', (42, 10), 4, 4, True), ('L', (42, 28)), ('A', (40, 32), 5, 5, True), ('L', (32, 40)), ('A', (28, 42), 5, 5, True), ('L', (10, 42)), ('A', (6, 38), 4, 4, True), ('L', (6, 10)), ('A', (10, 6), 4, 4, True)], True)
        path('fold', (42, 28), [('L', (32, 28)), ('A', (28, 32), 4, 4, False), ('L', (28, 42))])
        join('paper', 'fold')
