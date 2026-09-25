'Bearded Man Avatar.\nPlan: Circular face and beard centered x24; jaw y30 touches shoulder y34 at zero ink gap. Broad curved shoulders.\nConstruction reference: human_ref/user.svg: centered circular head and curved shoulders; current zero-gap avatar construction.\nReduction: Fine hair/ears and mouth omitted; beard boundary retained.\nKeyshape: SQUARE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2289d3ea-6a6c-4cd3-aa56-0a31b534beeb'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_26/man beard 2_2289d3ea-6a6c-4cd3-aa56-0a31b534beeb.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'bearded-man'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'avatars'
    categories = ('avatars', 'primitive', 'primitives')
    aliases = ()
    keywords = ('bearded', 'man')

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

        self.add_arc('head-top',(12,18),(36,18),radius_x=12)
        self.add_arc('head-bottom',(36,18),(12,18),radius_x=12)
        self.add_contour('head','head-top','head-bottom',closed=True)
        path('beard',(12,18),[((24,20),8,6,False),((36,18),8,6,False)])
        self.relate('connect','beard','head')
        self.add_arc('body-top',(6,42),(42,42),radius_x=18,radius_y=8)
        self.add_contour('shoulders','body-top')
        self.relate('connect','head','shoulders')
