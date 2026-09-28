'Top View Soccer Field.\nPlan: Top-down soccer field with halfway circle and two penalty areas.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Halfway line stops at center circle to keep the central opening clear.\nKeyshape: HRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a9a6edef-bdcf-4d2b-a622-4aa5cc8d5351'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_18/field 2_a9a6edef-bdcf-4d2b-a622-4aa5cc8d5351.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'soccer-pitch-from-above'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'sports'
    categories = ('sports', 'primitive', 'primitives')
    aliases = ()
    keywords = ('soccer', 'pitch', 'from', 'above')

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

        box('field',4,8,44,40,3)
        circle('center',24,24,3)
        self.add_line('half-top',(24,8),(24,21));self.add_line('half-bottom',(24,27),(24,40))
        for n in ('half-top','half-bottom'):
         self.relate('connect',n,'center');self.relate('connect',n,'field')
        for n,x,inner in [('left',4,12),('right',44,36)]:
         self.add_polyline(n,(x,16),(inner,16),(inner,32),(x,32));self.relate('connect',n,'field')
