'Yarn Ball and Knitting Needles.\nPlan: Yarn ball with a smooth strand across its face and two crossed knitting needles behind. Bounds6..42.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Reduce many yarn strands to one broad curve; omit knobs and preserve both crossed needles.\nKeyshape: SQUARE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0768b024-3575-40e2-9a80-75d99ddaffae'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_24/knitting_0768b024-3575-40e2-9a80-75d99ddaffae.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'yarn-ball-knitting-needles'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('yarn', 'ball', 'knitting', 'needles')

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

        circle('yarn',24,26,14)
        self.add_bezier('strand',(10,26),((18,24),(30,28),(38,26)));self.relate('connect','strand','yarn')
        for n,a,z in [('needle-left',(6,6),(14,16)),('needle-right',(42,6),(34,16)),('tip-left',(14,36),(6,42)),('tip-right',(34,36),(42,42))]:
         self.add_line(n,a,z);self.relate('connect',n,'yarn')
