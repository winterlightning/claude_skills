'Wheat Grain Stalk.\nPlan: Wheat ear with terminal oval grain, two broad paired grain tiers and a central stalk. Bounds8,4..40,44.\nConstruction reference: Lucide wheat paired repeated grains with shared central stem; source upright ear.\nReduction: Reduce three pairs to two broad tiers while keeping a terminal grain and stalk.\nKeyshape: VRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1388b7e3-83fe-4163-af51-758131c15177'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_21/gran_1388b7e3-83fe-4163-af51-758131c15177.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'wheat-ear-on-stem'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('wheat', 'ear', 'on', 'stem')

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

        ellipse('terminal',24,10,4,6)
        self.add_line('stem',(24,16),(24,44));self.relate('connect','terminal','stem')
        for side in (-1,1):
         def p(x,y):return (24+side*x,y)
         self.add_bezier(f'grains-{side}',p(0,16),(p(6,16),p(10,16),p(16,16)),(p(16,24),p(8,28),p(0,28)),(p(6,28),p(10,28),p(16,28)),(p(16,36),p(8,40),p(0,40)))
         self.relate('connect','stem',f'grains-{side}')
         self.relate('connect','terminal',f'grains-{side}')
        self.relate('connect','grains--1','grains-1')
