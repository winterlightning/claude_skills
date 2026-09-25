'Wild Spotted Jaguar.\nPlan: Left-facing spotted cat with rounded back, two clear legs and trailing tail. Bounds4,8..44,40.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Reduce four overlapping legs to two distinct openings and several spots to one; preserve ear, muzzle and tail.\nKeyshape: HRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2b294370-a335-445e-8511-74cc786c6a8b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_23/jaguar_2b294370-a335-445e-8511-74cc786c6a8b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'jaguar'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('jaguar',)

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

        path('cat',(4,18),[(10,12),(12,8),(16,12),(20,12),(28,12),((36,20),8,8,True),(36,40),(28,40),(28,30),(20,30),(20,40),(12,40),(12,24),(4,24),(4,18)],True)
        path('tail',(36,20),[(44,20),(44,32)]);self.relate('connect','cat','tail')
        self.add_dot('spot',(26,21))
