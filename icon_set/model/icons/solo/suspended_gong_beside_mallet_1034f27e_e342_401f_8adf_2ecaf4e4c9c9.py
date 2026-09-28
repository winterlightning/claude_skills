'Hanging Gong with Mallet.\nPlan: Suspended circular gong with two cords, centered boss and a separate mallet.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Boss is a solid dot; two cords retained at actual gong nodes.\nKeyshape: HRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1034f27e-e342-401f-8adf-2ecaf4e4c9c9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_21/gong_1034f27e-e342-401f-8adf-2ecaf4e4c9c9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'suspended-gong-beside-mallet'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('suspended', 'gong', 'beside', 'mallet')

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

        self.add_polyline('rail',(4,8),(11,8),(23,8),(30,8))
        path('gong',(11,22),[((17,20),10,10,True),((23,22),10,10,True),((27,30),10,10,True),((17,40),10,10,True),((7,30),10,10,True),((11,22),10,10,True)],True)
        self.add_dot('boss',(17,30))
        for x in (11,23):
         self.add_line(f'cord-{x}',(x,8),(x,22));self.relate('connect',f'cord-{x}','rail');self.relate('connect',f'cord-{x}','gong')
        circle('mallet-head',40,16,4)
        self.add_line('mallet-handle',(40,20),(40,40));self.relate('connect','mallet-head','mallet-handle')
