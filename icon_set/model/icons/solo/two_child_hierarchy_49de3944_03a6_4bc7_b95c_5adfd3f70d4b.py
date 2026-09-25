'Hierarchical Structure Diagram.\nPlan: Upper-left parent and two equal right-side children on a common branch.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Keep the defining silhouette and essential parts.\nKeyshape: SQUARE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '49de3944-03a6-4bc7-b95c-5adfd3f70d4b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_40/workflow gantt chart 11_49de3944-03a6-4bc7-b95c-5adfd3f70d4b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'two-child-hierarchy'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('two', 'child', 'hierarchy')

    def build(self):

        def path(name, start, steps, closed=False):
            members, point = [], start
            for index, step in enumerate(steps):
                member = f"{name}-{index}"
                if len(step) == 2:
                    self.add_line(member, point, step)
                    point = step
                else:
                    end, rx, ry, sweep = step
                    self.add_arc(member, point, end, radius_x=rx, radius_y=ry, sweep=sweep)
                    point = end
                members.append(member)
            self.add_contour(name, *members, closed=closed)

        def ellipse(name, x, y, rx, ry):
            path(name, (x-rx,y), [((x+rx,y),rx,ry,True), ((x-rx,y),rx,ry,True)], True)

        def circle(name, x, y, radius):
            ellipse(name,x,y,radius,radius)

        def box(name, left, top, right, bottom, radius=4):
            r = radius
            path(name, (left+r,top), [(right-r,top), ((right,top+r),r,r,True),
                 (right,bottom-r), ((right-r,bottom),r,r,True), (left+r,bottom),
                 ((left,bottom-r),r,r,True), (left,top+r), ((left+r,top),r,r,True)], True)

        self.add_polyline('parent',(6,6),(22,6),(22,14),(14,14),(6,14),closed=True)
        self.add_polyline('trunk',(14,14),(14,22),(14,38));self.relate('connect','parent','trunk')
        for j,y in enumerate((18,34)):
         self.add_polyline(f'child-{j}',(30,y),(42,y),(42,y+8),(30,y+8),(30,y+4),closed=True)
         self.add_line(f'branch-{j}',(14,y+4),(30,y+4));self.relate('connect',f'branch-{j}',f'child-{j}');self.relate('connect',f'branch-{j}','trunk')
