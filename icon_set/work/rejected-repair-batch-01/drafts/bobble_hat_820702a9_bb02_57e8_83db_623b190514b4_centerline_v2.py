"""Use a true round pom-pom and an upright hat crown, replacing the flat button and squat dome. The cuff has two matching round ends.
Independent centerline revision; original snapshot preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '820702a9-bb02-57e8-83db-623b190514b4'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-02/beanie winter_820702a9-bb02-57e8-83db-623b190514b4.svg'
AUTHOR = 'gpt-6'

class BobbleHat(Solo48):
    icon_id = 'bobble-hat-centerline-v2'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/accessories'
    aliases = ()
    keywords = ('beanie', 'hat', 'bobble hat', 'winter', 'knit', 'pompom', 'cap', 'clothing')
    variant_of = 'bobble-hat'
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
        circle('pompom', 24, 8, 4)
        path('crown', (10, 34), [('L', (10, 26)), ('A', (24, 12), 14, 14, True), ('A', (38, 26), 14, 14, True), ('L', (38, 34))])
        join('pompom', 'crown')
        rounded('cuff', 8, 34, 40, 44, 3)
        join('cuff', 'crown')
