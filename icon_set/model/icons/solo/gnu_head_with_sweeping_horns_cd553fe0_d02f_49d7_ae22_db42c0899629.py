'Horned Gnu Animal Head.\nPlan: Long left-facing gnu muzzle under two sweeping horns with a sloping rear neck.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Ear and small nose crease omitted to preserve muzzle and two sweeping horns.\nKeyshape: HRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cd553fe0-d02f-49d7-ae22-db42c0899629'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_21/gnu_cd553fe0-d02f-49d7-ae22-db42c0899629.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'gnu-head-with-sweeping-horns'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('gnu', 'head', 'with', 'sweeping', 'horns')

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

        path('head',(4,32),[(14,18),((28,18),14,10,True),(44,36)])
        path('jaw',(4,32),[((12,40),8,8,False),(24,34),((30,26),10,10,False)]);self.relate('connect','head','jaw')
        path('horn-left',(14,18),[((10,8),10,10,True),(20,8)])
        path('horn-right',(28,18),[((40,8),14,14,False)])
        self.relate('connect','head','horn-left');self.relate('connect','head','horn-right')
        self.add_dot('eye',(18,27))
