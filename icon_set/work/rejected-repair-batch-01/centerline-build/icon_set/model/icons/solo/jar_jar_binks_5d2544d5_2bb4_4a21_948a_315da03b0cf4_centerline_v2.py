"""Widen the separation between the two eye stalks and give the long hanging ears a clean outward flare; remove the pinched bridge above the face.
Independent centerline revision; original snapshot preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5d2544d5-2bb4-4a21-948a-315da03b0cf4'
SOURCE_PATH = 'pictographic-primitives/video/jar jar binks gungan_5d2544d5-2bb4-4a21-948a-315da03b0cf4.svg'
AUTHOR = 'gpt-6'

class JarJarBinks(Solo48):
    icon_id = 'jar-jar-binks-centerline-v2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/media'
    aliases = ()
    keywords = ('jar jar binks', 'gungan', 'character', 'face', 'alien', 'ears', 'star wars')

    def circle(self, name, cx, cy, r):
        self.add_arc(name + '-top', (cx - r, cy), (cx + r, cy), radius_x=r)
        self.add_arc(name + '-bottom', (cx + r, cy), (cx - r, cy), radius_x=r)
        self.add_contour(name, name + '-top', name + '-bottom', closed=True)

    def rounded(self, name, x, y, w, h, r):
        pts = [(x + r, y), (x + w - r, y), (x + w, y + r), (x + w, y + h - r), (x + w - r, y + h), (x + r, y + h), (x, y + h - r), (x, y + r)]
        ids = []
        for i, a in enumerate(pts):
            b = pts[(i + 1) % 8]
            ident = name + '-' + str(i)
            ids.append(ident)
            if i % 2:
                self.add_arc(ident, a, b, radius_x=r)
            else:
                self.add_line(ident, a, b)
        self.add_contour(name, *ids, closed=True)
    variant_of = 'jar-jar-binks'
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
        path('face', (10, 18), [('A', (15, 6), 5, 12, True), ('A', (20, 18), 5, 12, True), ('L', (28, 18)), ('A', (33, 6), 5, 12, True), ('A', (38, 18), 5, 12, True), ('C', (24, 42), (38, 32), (32, 42)), ('C', (10, 18), (16, 42), (10, 32))], True)
        poly('ear-left', (10, 18), (6, 42), (14, 42))
        poly('ear-right', (38, 18), (42, 42), (34, 42))
        join('ear-left', 'face')
        join('ear-right', 'face')
        path('mouth', (21, 30), [('A', (27, 30), 4, 4, False)])
