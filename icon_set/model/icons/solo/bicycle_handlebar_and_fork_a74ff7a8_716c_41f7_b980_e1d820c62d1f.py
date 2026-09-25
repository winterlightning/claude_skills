'Bicycle Handlebar and Fork.\nPlan: Symmetric raised handlebar, central stem, fork with two prongs; junction nodes shared.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Grips reduced to thick round-ended handlebar strokes.\nKeyshape: HRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a74ff7a8-716c-41f7-b980-e1d820c62d1f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_22/handlebar_a74ff7a8-716c-41f7-b980-e1d820c62d1f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'bicycle-handlebar-and-fork'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('bicycle', 'handlebar', 'and', 'fork')

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

        path('handlebar',(4,8),[(10,8),((18,16),8,8,False),(24,16),(30,16),((38,8),8,8,False),(44,8)])
        self.add_line('stem',(24,16),(24,28));self.relate('connect','stem','handlebar')
        path('fork',(16,40),[(16,36),((24,28),8,8,True),((32,36),8,8,True),(32,40)])
        self.relate('connect','stem','fork')
