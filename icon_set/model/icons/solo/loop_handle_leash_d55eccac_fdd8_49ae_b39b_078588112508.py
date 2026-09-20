'Adjustable Pet Slip Lead Leash.\nPlan: Diagonal loop handle with round upper end; lead joins a rounded lower clip at an explicit top node.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Joining collar reduced to the shared lead/handle node; clip is a simple round loop.\nKeyshape: SQUARE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd55eccac-fdd8-49ae-b39b-078588112508'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_25/leash_d55eccac-fdd8-49ae-b39b-078588112508.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'loop-handle-leash'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('loop', 'handle', 'leash')

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

        path('handle',(22,26),[(22,16),((32,6),10,10,True),((42,16),10,10,True),((32,26),10,10,True),(22,26)],True)
        path('clip',(12,30),[((18,36),6,6,True),((12,42),6,6,True),((6,36),6,6,True),((12,30),6,6,True)],True)
        self.add_line('lead',(22,26),(12,30));self.relate('connect','lead','handle');self.relate('connect','lead','clip')
