"""Open the lower arches and remove the cramped wave trapped beneath the piers. Give the two bridge openings full circular crowns and a separate water baseline.
Independent centerline revision; original snapshot preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8a6886ef-7a4b-5e6a-b9d3-1d5cb49e0192'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-06/bridge_8a6886ef-7a4b-5e6a-b9d3-1d5cb49e0192.svg'
AUTHOR = 'gpt-6'

class ArchedStoneBridge(Solo48):
    icon_id = 'arched-stone-bridge-centerline-v2'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'places/landmarks'
    aliases = ()
    keywords = ('bridge', 'arch', 'viaduct', 'river', 'water', 'crossing', 'stone', 'landmark', 'infrastructure')
    variant_of = 'arched-stone-bridge'
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
        poly('bridge', (4, 30), (4, 8), (44, 8), (44, 30))
        for i, x in enumerate((4, 24)):
            path(f'arch-{i}', (x, 30), [('A', (x + 10, 20), 10, 10, True), ('A', (x + 20, 30), 10, 10, True)])
            join(f'arch-{i}', 'bridge')
        line('pier', (24, 8), (24, 30))
        join('pier', 'bridge')
        join('pier', 'arch-0')
        join('pier', 'arch-1')
        join('arch-0', 'arch-1')
        line('water', (4, 40), (44, 40))
