"""person-at-picnic-table: Side-view seated person with forearm on picnic table and splayed table legs. Head radius 3 at (14,11); shoulder y22 gives exact 4-unit ink gap. Small bench and minimal limbs retained."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b6532fa9-401d-4d4e-a68e-967a9d97734f'
SOURCE_PATH = 'pictographic-primitives/outdoors/outdoors bench sit_b6532fa9-401d-4d4e-a68e-967a9d97734f.svg'
AUTHOR = 'gpt-6'


class PersonAtPicnicTable(Solo48):
    icon_id = 'person-at-picnic-table'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    aliases = ()
    keywords = ('picnic', 'bench', 'table', 'sitting', 'person', 'park', 'rest', 'outdoors', 'outdoors-batch-02')

    def build(self):
        # Plan: Side-view seated person with forearm on picnic table and splayed table legs. Head radius 3 at (14,11); shoulder y22 gives exact 4-unit ink gap. Small bench and minimal limbs retained.
        # Lucide landmark original and atomic-debug inspected for construction.
        # Human scenes use icon_set/references/human_ref/full_body_ref.png.
        # Centerline envelope: (4, 8, 44, 40).
        def path(name, start, commands, closed=False):
            members, here = [], start
            for i, (kind, end, *args) in enumerate(commands):
                part = f"{name}-{i}"
                if kind == 'L':
                    self.add_line(part, here, end)
                else:
                    rx, ry, sweep = args
                    self.add_arc(part, here, end, radius_x=rx, radius_y=ry, sweep=sweep)
                members.append(part)
                here = end
            self.add_contour(name, *members, closed=closed)
        def circle(name, cx, cy, r):
            path(name, (cx-r,cy), [('A',(cx+r,cy),r,r,True),('A',(cx-r,cy),r,r,True)], True)
        def rounded(name, x0, y0, x1, y1, r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line, poly = self.add_line, self.add_polyline
        join = lambda a,b: self.relate('connect',a,b)
        circle('head',14,11,3)
        poly('body',(14,22),(10,32),(20,32),(22,40))
        line('arm',(14,22),(26,22));join('arm','body')
        poly('table',(26,22),(36,22),(44,22));join('table','arm')
        poly('table-legs',(32,40),(36,22),(44,40));join('table-legs','table')
        poly('bench',(4,32),(6,32),(10,32));join('bench','body')
        line('bench-leg',(6,32),(4,40));join('bench-leg','bench')
