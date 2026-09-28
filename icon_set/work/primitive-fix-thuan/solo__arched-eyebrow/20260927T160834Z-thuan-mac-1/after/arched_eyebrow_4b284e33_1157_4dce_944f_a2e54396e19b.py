'Arched Eyebrow Shape.\nPlan: Sweeping eyebrow outline with two smooth exterior quarter ellipses, rounded root and tapered right end.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Broadened arch to fit the fixed horizontal envelope; check recognizability at native size.\nKeyshape: HRECT_M; use exact SOLO48 centerline extremes from the contract.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '4b284e33-1157-4dce-944f-a2e54396e19b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__arched-eyebrow/20260927T160834Z-thuan-mac-1/reference/eyebrow_4b284e33-1157-4dce-944f-a2e54396e19b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'arched-eyebrow'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('arched', 'eyebrow')

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

        self.add_bezier('brow-rise',(4,38),((11,22),(22,12),(34,10)))
        self.add_bezier('brow-tip',(34,10),((39,10),(43,16),(44,22)))
        self.add_contour('brow','brow-rise','brow-tip')
