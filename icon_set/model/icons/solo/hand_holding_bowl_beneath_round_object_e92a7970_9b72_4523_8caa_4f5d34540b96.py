'Hand Holding Bowl for Charity.\nPlan: Flat supporting hand under a rounded bowl and a floating round object.\nConstruction reference: Lucide hand-helping: long flat supporting palm with a rounded fingertip.\nReduction: Bowl rim reduced to one lip; thumb folds omitted; floating object is smaller to maintain clearance.\nKeyshape: HRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e92a7970-9b72-4523-8caa-4f5d34540b96'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_18/feeding_e92a7970-9b72-4523-8caa-4f5d34540b96.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hand-holding-bowl-beneath-round-object'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('hand', 'holding', 'bowl', 'beneath', 'round', 'object')

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

        circle('object',24,11,3)
        path('bowl',(10,31),[((8,23),2,8,True),(36,23),((34,31),2,8,True)])
        path('hand',(4,31),[(10,31),(34,31),(40,31),((40,39),4,4,True),(24,40),(4,40)])
        self.relate('connect','bowl','hand')
