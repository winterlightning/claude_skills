'Three Petal Trillium Flower.\nPlan: Three broad pointed trillium petals meet a circular center.\nConstruction reference: Lucide flower: radial petals joined around a central circle.\nReduction: Petal veins omitted; all three petals retained.\nKeyshape: SQUARE; use exact SOLO48 centerline extremes from the contract.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '52786bcf-1504-49f9-a5c7-0a9a8ad3d047'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__trillium-flower/20260927T173930Z-thuan-mac-1/reference/trillium_52786bcf-1504-49f9-a5c7-0a9a8ad3d047.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'trillium-flower'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('trillium', 'flower')

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

        circle('center',24,26,3)
        self.add_line('top-0',(21,26),(16,18))
        self.add_bezier('top-1',(16,18),((14,14),(20,8),(24,6)))
        self.add_bezier('top-2',(24,6),((28,8),(34,14),(32,18)))
        self.add_line('top-3',(32,18),(27,26))
        self.add_contour('top','top-0','top-1','top-2','top-3')
        path('left',(21,26),[((6,42),15,16,False),((24,29),18,13,False)])
        path('right',(27,26),[((42,42),15,16,True),((24,29),18,13,True)])
        for a,b in [('center','top'),('center','left'),('center','right'),('top','left'),('top','right'),('left','right')]:self.relate('connect',a,b)
