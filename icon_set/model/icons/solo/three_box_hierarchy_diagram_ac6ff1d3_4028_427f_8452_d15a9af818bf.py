'Hierarchical Chart Structure.\nPlan: Parent box branches into two lower child boxes with a central descending stub.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Keep the defining silhouette and essential parts.\nKeyshape: SQUARE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ac6ff1d3-4028-427f-8452-d15a9af818bf'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_21/h3_ac6ff1d3-4028-427f-8452-d15a9af818bf.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-box-hierarchy-diagram'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('three', 'box', 'hierarchy', 'diagram')

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

        self.add_polyline('parent',(18,6),(30,6),(30,16),(24,16),(18,16),closed=True)
        self.add_polyline('trunk',(24,16),(24,24),(24,32));self.relate('connect','trunk','parent')
        self.add_polyline('branch',(11,34),(11,24),(24,24),(37,24),(37,34));self.relate('connect','branch','trunk')
        for j,x in enumerate((6,32)):
         self.add_polyline(f'child-{j}',(x,34),(x+5,34),(x+10,34),(x+10,42),(x,42),closed=True)
         self.relate('connect',f'child-{j}','branch')
