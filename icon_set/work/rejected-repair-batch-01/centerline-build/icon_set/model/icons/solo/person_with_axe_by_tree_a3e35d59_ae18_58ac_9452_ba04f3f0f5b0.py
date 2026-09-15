"""person-with-axe-by-tree: Woodcutter holding an axe beside a simplified pine. Shared full_body_ref.png: head center (10,11), radius 3 and shoulder (10,22), exactly 4 units of ink clearance. Tree tiers omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a3e35d59-ae18-58ac-9452-ba04f3f0f5b0'
SOURCE_PATH = 'pictographic-primitives/outdoors/cut wood_a3e35d59-ae18-58ac-9452-ba04f3f0f5b0.svg'
AUTHOR = 'gpt-6'


class PersonWithAxeByTree(Solo48):
    icon_id = 'person-with-axe-by-tree'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    aliases = ()
    keywords = ('woodcutting', 'axe', 'tree', 'lumberjack', 'person', 'forest', 'chopping', 'pine', 'outdoors-batch-01')

    def build(self):
        # Plan: Woodcutter holding an axe beside a simplified pine. Shared full_body_ref.png: head center (10,11), radius 3 and shoulder (10,22), exactly 4 units of ink clearance. Tree tiers omitted.
        # Lucide axe: original and atomic-debug inspected for contour construction.
        # Keyshape centerline extremes: (6, 6, 42, 42).

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
        circle('head',10,11,3)
        poly('body',(6,42),(10,30),(10,22),(20,26))
        poly('leg',(10,30),(18,42));join('leg','body')
        poly('handle',(20,18),(20,26),(20,34));join('handle','body')
        poly('axe',(20,18),(28,14),(28,24),(20,22));join('axe','handle')
        poly('tree',(34,6),(42,30),(34,30),(34,42))
