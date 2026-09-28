'Trash Can with Lid.\nPlan: Tapered trash bin with raised lid handle and one front rib.\nConstruction reference: Lucide trash-2: handle/lid/body hierarchy and sparse front ribs.\nReduction: Three ribs reduced to one.\nKeyshape: VRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cd1ee2ff-26a3-4c8c-bbea-41076e024cf7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_38/trash can_cd1ee2ff-26a3-4c8c-bbea-41076e024cf7.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'trash-can-reference-cd1ee2ff'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('trash', 'can', 'reference', 'cd1ee2ff')

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

        path('lid',(8,12),[(18,12),(30,12),(40,12),(40,20),(36,20),(12,20),(8,20),(8,12)],True)
        self.add_polyline('handle',(18,12),(18,4),(30,4),(30,12));self.relate('connect','handle','lid')
        path('bin',(12,20),[(14,40),((18,44),4,4,False),(30,44),((34,40),4,4,False),(36,20)]);self.relate('connect','bin','lid')
        self.add_line('rib',(24,29),(24,35))
