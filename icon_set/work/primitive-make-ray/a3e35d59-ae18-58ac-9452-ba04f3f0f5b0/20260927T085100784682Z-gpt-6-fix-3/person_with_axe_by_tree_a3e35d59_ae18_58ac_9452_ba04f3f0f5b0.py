"""Revision from the inspected source: The rejected one-sided tree looked like a hook beside an isolated blade; the reference has a pointed evergreen beside the woodcutter.

Changes: Drew a centered two-sided pine and tightened the unified axe away from its branches.
Full-body or bust construction follows icon_set/references/human_ref.
"""
"""person-with-axe-by-tree: Woodcutter holding an axe beside a simplified pine. Shared full_body_ref.png: head center (10,11), radius 3 and shoulder (10,22), exactly 4 units of ink clearance. Tree tiers omitted."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'a3e35d59-ae18-58ac-9452-ba04f3f0f5b0'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-with-axe-by-tree/20260927T083143Z-thuan-mac-1/reference/cut wood_a3e35d59-ae18-58ac-9452-ba04f3f0f5b0.svg'
AUTHOR = 'gpt-6'


class PersonWithAxeByTree(Solo48):
    icon_id = 'person-with-axe-by-tree'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    categories = ('outdoors', 'primitives')
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
        poly('tool',(20,34),(20,18),(26,14),(26,24),(20,22));join('tool','body')
        poly('tree',(34,26),(38,6),(42,26),(38,26),(38,42))
