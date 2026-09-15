"""Restore a round watch dial; angle the paired straps to preserve readable proportions.
Plan: circular dial, opposed diagonal straps, and one joined hand stroke.
SQUARE centerline extremes (6,6)-(42,42).
Lucide: watch; geometric contour construction adapted to SOLO48.
Independent variant; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6f3e245f-ff22-445c-9c0b-9969d193eb11'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-01/watch_6f3e245f-ff22-445c-9c0b-9969d193eb11.svg'
AUTHOR = 'gpt-6'

class AnalogueWristwatchVariant3(Solo48):
    icon_id = 'analogue-wristwatch-v3'
    variant_of = 'analogue-wristwatch'
    variant_label = 'Batch 01: visual refinement'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/accessories'
    aliases = ()
    keywords = ('watch', 'wristwatch', 'time', 'clock', 'analogue', 'dial', 'strap', 'accessory')

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
        circle('dial', 24, 24, 12)
        poly('upper-strap', (12, 24), (6, 12), (12, 6), (24, 12))
        poly('lower-strap', (36, 24), (42, 36), (36, 42), (24, 36))
        join('upper-strap', 'dial')
        join('lower-strap', 'dial')
        poly('hands', (24, 21), (24, 24), (27, 26))
