"""Show four diagonal rotor tips around the helicopter body, with the middle shaft hidden by the fuselage. Open the crowded crossed center and keep the cockpit, hub, and tail distinct.
Independent centerline revision; original snapshot preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9b4b7495-29fd-5179-a217-6ff424a24d21'
SOURCE_PATH = 'pictographic-primitives/transportation/helicopter top view_9b4b7495-29fd-5179-a217-6ff424a24d21.svg'
AUTHOR = 'gpt-6'

class HelicopterTopView(Solo48):
    icon_id = 'helicopter-top-view-centerline-v2'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('helicopter', 'top view', 'aerial', 'rotor', 'aircraft', 'chopper', 'aviation', 'overhead')
    variant_of = 'helicopter-top-view'
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
        path('fuselage', (14, 14), [('A', (24, 4), 10, 10, True), ('A', (34, 14), 10, 10, True), ('L', (34, 34)), ('L', (24, 36)), ('L', (14, 34)), ('L', (14, 14))], True)
        for n, a, b in [('nw', (8, 8), (14, 14)), ('ne', (40, 8), (34, 14)), ('sw', (8, 40), (14, 34)), ('se', (40, 40), (34, 34))]:
            line('rotor-' + n, a, b)
            join('rotor-' + n, 'fuselage')
        dot('hub', (24, 24))
        line('tail', (24, 36), (24, 44))
        line('tail-rotor', (18, 44), (30, 44))
        join('tail', 'fuselage')
        join('tail', 'tail-rotor')
