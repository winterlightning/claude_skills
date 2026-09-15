"""arrange-number: Clear numeric sorting mark; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '774a187b-a625-438b-9b84-1427193ca713'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_04/arrange number_774a187b-a625-438b-9b84-1427193ca713.svg'
AUTHOR = 'gpt-6'

class ArrangeNumber(Solo48):
    icon_id = 'arrange-number'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_04'
    aliases = ()
    keywords = ('solo-ai-full-set', 'arrange-number')

    def build(self):

        def path(name, start, commands, closed=False):
            members = []
            here = start
            for index, command in enumerate(commands):
                ident = f'{name}-{index}'
                kind, end, *args = command
                if kind == 'L':
                    self.add_line(ident, here, end)
                elif kind == 'A':
                    rx, ry, sweep = args
                    self.add_arc(ident, here, end, radius_x=rx, radius_y=ry, sweep=sweep)
                elif kind == 'C':
                    c1, c2 = args
                    self.add_bezier(ident, here, (c1, c2, end))
                members.append(ident)
                here = end
            self.add_contour(name, *members, closed=closed)

        def circle(name, cx, cy, r):
            path(name, (cx - r, cy), [('A', (cx + r, cy), r, r, True), ('A', (cx - r, cy), r, r, True)], True)

        def rounded(name, x0, y0, x1, y1, r):
            path(name, (x0 + r, y0), [('L', (x1 - r, y0)), ('A', (x1, y0 + r), r, r, True), ('L', (x1, y1 - r)), ('A', (x1 - r, y1), r, r, True), ('L', (x0 + r, y1)), ('A', (x0, y1 - r), r, r, True), ('L', (x0, y0 + r)), ('A', (x0 + r, y0), r, r, True)], True)
        line = self.add_line
        poly = self.add_polyline
        join = lambda a, b: self.relate('connect', a, b)
        line('arrow', (13, 10), (13, 35))
        path('head', (8, 29), [('L', (13, 35)), ('L', (18, 29))])
        join('arrow', 'head')
        # Both digits use a shared 16-unit cap height and the same stroke.
        digit_height = 16
        one_top, nine_bottom = 4, 44
        nine_top = nine_bottom - digit_height
        poly('one', (32, 7), (36, one_top), (36, one_top + digit_height))
        circle('nine-bowl', 36, nine_top + 4, 4)
        path('nine-stem', (40, nine_top + 4), [('L', (40, 42)), ('C', (38, nine_bottom), (40, 43), (39, nine_bottom))])
        join('nine-bowl', 'nine-stem')
