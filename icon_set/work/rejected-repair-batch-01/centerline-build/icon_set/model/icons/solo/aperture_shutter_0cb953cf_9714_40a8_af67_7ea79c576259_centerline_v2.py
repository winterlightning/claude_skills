"""Replace the six inconsistent rim arcs with one true circle. Rebuild the six shutter blades as rotational pairs with a regular central hexagon.
Independent centerline revision; original snapshot preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0cb953cf-9714-40a8-af67-7ea79c576259'
SOURCE_PATH = 'pictographic-primitives/symbol/lens shutter_0cb953cf-9714-40a8-af67-7ea79c576259.svg'
AUTHOR = 'gpt-6'

class ApertureShutter(Solo48):
    icon_id = 'aperture-shutter-centerline-v2'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/symbols'
    aliases = ()
    keywords = ('aperture', 'shutter', 'camera', 'lens', 'photography', 'iris', 'focus', 'photo')
    variant_of = 'aperture-shutter'
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
        circle('rim', 24, 24, 20)
        points = [(14, 24), (18, 16), (30, 16), (34, 24), (30, 32), (18, 32)]
        poly('aperture', *points, closed=True)
        for i, (a, b) in enumerate([((14, 24), (8, 12)), ((18, 16), (24, 4)), ((30, 16), (40, 12)), ((34, 24), (40, 36)), ((30, 32), (24, 44)), ((18, 32), (8, 36))]):
            line(f'blade-{i}', a, b)
            join(f'blade-{i}', 'aperture')
            join(f'blade-{i}', 'rim')
