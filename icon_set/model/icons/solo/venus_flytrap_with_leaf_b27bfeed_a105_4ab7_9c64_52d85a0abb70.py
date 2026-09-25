'Venus Flytrap Plant.\nPlan: Open jagged flytrap with two large teeth, curved stalk and separate side leaf. Bounds8,4..40,44.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Reduce jaw teeth to two large points and retain one leaf, opening crowded sawtooth gaps.\nKeyshape: VRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b27bfeed-a105-4ab7-9c64-52d85a0abb70'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_19/flytrap_b27bfeed-a105-4ab7-9c64-52d85a0abb70.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'venus-flytrap-with-leaf'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('venus', 'flytrap', 'with', 'leaf')

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

        path('trap',(8,4),[(8,14),((32,22),14,14,False),(40,10),(26,16),(28,4),(16,12),(8,4)],True)
        self.add_bezier('stem',(16,22),((8,30),(20,34),(20,44)))
        self.relate('connect','stem','trap')
        self.add_bezier('leaf',(20,44),((20,34),(30,32),(38,32)),((38,40),(28,44),(20,44)))
        self.relate('connect','stem','leaf')
