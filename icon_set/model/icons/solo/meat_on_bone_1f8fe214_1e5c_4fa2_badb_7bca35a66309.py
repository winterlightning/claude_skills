'Meat on Bone.\nPlan: Oval meat cut face, broad curved meat body and short lobed bone. Bounds4,8..44,40.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Keep the defining silhouette and essential parts.\nKeyshape: HRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1f8fe214-1e5c-4fa2-badb-7bca35a66309'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/animal drumstick_1f8fe214-1e5c-4fa2-badb-7bca35a66309.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'meat-on-bone'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
    aliases = ()
    keywords = ('meat', 'on', 'bone')

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

        path('cut-left',(12,8),[((4,24),8,16,False),((12,40),8,16,False)])
        path('cut-right',(12,40),[((20,24),8,16,False),((12,8),8,16,False)])
        self.relate('connect','cut-left','cut-right')
        self.add_bezier('meat',(12,8),((24,8),(30,14),(30,24)),((30,34),(24,40),(12,40)))
        self.relate('connect','cut-left','meat');self.relate('connect','cut-right','meat')
        path('bone',(30,20),[(36,20),((44,20),4,4,True),(44,28),((36,28),4,4,True),(30,28)])
        self.relate('connect','bone','meat')
