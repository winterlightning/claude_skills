'High Temperature Thermometer.\nPlan: Thermometer with high column, small reservoir and two right-hand ticks.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Keep the defining silhouette and essential parts.\nKeyshape: VRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '26bf3af8-64f9-4d16-aa6c-a43c72408de7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_37/temperature high_26bf3af8-64f9-4d16-aa6c-a43c72408de7.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'high-column-two-tick-thermometer'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('high', 'column', 'two', 'tick', 'thermometer')

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

        path('outline',(10,26),[(10,13),((28,13),9,9,True),(28,26),((30,34),2,8,True),((8,34),11,10,True),((10,26),2,8,True)],True)
        circle('reservoir',19,33,2)
        self.add_line('column',(19,14),(19,31));self.relate('connect','column','reservoir')
        for j,y in enumerate((14,24)):self.add_line(f'tick-{j}',(38,y),(40,y))
