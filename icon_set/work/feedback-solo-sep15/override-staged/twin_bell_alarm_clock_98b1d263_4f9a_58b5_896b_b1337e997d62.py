"""Move the two bells inward symmetrically; widen the round clock face to preserve the vertical envelope. Applied to the original icon identity."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '98b1d263-4f9a-58b5-896b-b1337e997d62'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-02/decoration clock retro_98b1d263-4f9a-58b5-896b-b1337e997d62.svg'
AUTHOR = 'gpt-6'

class TwinBellAlarmClock(Solo48):
    icon_id = 'twin-bell-alarm-clock'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/decoration'
    aliases = ()
    keywords = ('clock', 'alarm', 'bells', 'time', 'retro', 'round', 'feet')

    def build(self):
        """Symbol plan: Move the two bells inward symmetrically; widen the round clock face to preserve the vertical envelope. Reference: inspected current parent; no useful exact Lucide match selected."""

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
        oval('clock', 24, 30, 16, 14)
        path('bell-left', (10, 8), [('A', (20, 8), 5, 4, True)])
        path('bell-right', (28, 8), [('A', (38, 8), 5, 4, True)])
        poly('hands', (24, 25), (24, 30), (20, 32))
