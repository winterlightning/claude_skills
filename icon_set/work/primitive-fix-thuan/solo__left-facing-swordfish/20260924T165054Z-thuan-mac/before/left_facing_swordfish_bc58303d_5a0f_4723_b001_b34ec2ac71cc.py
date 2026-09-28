'Swimming Swordfish Icon.\nPlan: Left-facing swordfish with integrated fins and a crescent tail.\nConstruction reference: Lucide fish: fins integrated into one silhouette.\nReduction: Eye and internal fin seams omitted; bill and both fins remain.\nKeyshape: HRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bc58303d-5a0f-4723-b001-b34ec2ac71cc'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_37/swordfish_bc58303d-5a0f-4723-b001-b34ec2ac71cc.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'left-facing-swordfish'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('left', 'facing', 'swordfish')

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

        path('fish',(10,24),[((18,18),20,10,True),(24,8),(24,18),(36,20),((44,14),18,18,True),((44,38),18,18,False),((36,30),18,18,True),(24,30),(26,40),(18,30),((10,24),20,10,True)],True)
        self.add_line('bill',(4,24),(10,24));self.relate('connect','bill','fish')
