'Heavy Construction Excavator Machine.\nPlan: Left-facing excavator with cabin, continuous track and articulated open scoop.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Track rollers and cabin window removed; open scoop avoids a narrow boom/bucket pocket.\nKeyshape: HRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9bc0c97b-66cb-4cc5-b2e7-1d858df40775'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_17/excavator 1_9bc0c97b-66cb-4cc5-b2e7-1d858df40775.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'tracked-excavator-facing-left'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('tracked', 'excavator', 'facing', 'left')

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

        box('track',22,32,44,40,4)
        self.add_polyline('cab',(26,32),(26,24),(26,8),(38,8),(38,32));self.relate('connect','cab','track')
        self.add_polyline('boom',(26,24),(16,14),(8,18));self.relate('connect','boom','cab')
        path('bucket',(8,18),[(4,26),((12,30),8,4,False)]);self.relate('connect','bucket','boom')
