"""Rebuild the glue gun with a clear nozzle, grip, rear glue stick, and glue trail.
Plan: sloped gun body and grip share one outline; nozzle and glue stick attach.
HRECT_L centerline extremes (4,8)-(44,40).
Lucide: drill; geometric contour construction adapted to SOLO48.
Independent variant; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '419e370a-9fd2-4fcf-a6d2-cbe5f602e3f8'
SOURCE_PATH = 'pictographic-primitives/tools/tools glue gun_419e370a-9fd2-4fcf-a6d2-cbe5f602e3f8.svg'
AUTHOR = 'gpt-6'

class HotGlueGunVariant2(Solo48):
    icon_id = 'hot-glue-gun-v2'
    variant_of = 'hot-glue-gun'
    variant_label = 'Batch 01: visual refinement'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/tools'
    aliases = ()
    keywords = ('glue gun', 'hot glue', 'glue', 'adhesive', 'craft', 'diy', 'nozzle', 'tool')

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
        poly('gun', (10, 16), (18, 8), (32, 8), (36, 16), (32, 24), (36, 36), (26, 36), (22, 24), (10, 24), (4, 20), closed=True)
        line('glue-stick', (36, 16), (44, 16))
        join('glue-stick', 'gun')
        path('glue', (4, 38), [('A', (12, 38), 4, 2, False), ('L', (17, 38))])
