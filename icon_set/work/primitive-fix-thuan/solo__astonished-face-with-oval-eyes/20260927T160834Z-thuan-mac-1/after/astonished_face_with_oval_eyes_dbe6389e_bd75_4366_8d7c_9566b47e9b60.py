'Surprised Face with Wide Eyes.\nPlan: Raised eyebrows, two compact eyes and a small open round mouth inside a circular face.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Large oval eyes and pupils reduced to compact eye marks to preserve the surprised expression at 48 pixels.\nKeyshape: CIRCLE; use exact SOLO48 centerline extremes from the contract.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'dbe6389e-bd75-4366-8d7c-9566b47e9b60'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__astonished-face-with-oval-eyes/20260927T160834Z-thuan-mac-1/reference/face astonished_dbe6389e-bd75-4366-8d7c-9566b47e9b60.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'astonished-face-with-oval-eyes'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('astonished', 'face', 'with', 'oval', 'eyes')

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

        circle('face',24,24,20)
        ellipse('eye-left',17,20,3,4);ellipse('eye-right',31,20,3,4)
        circle('open-mouth',24,33,2)
