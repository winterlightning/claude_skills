'Elderly Woman with Bun and Glasses.\nPlan: Circular lower face, broad upper face, bun cap, paired round glasses and shallow smile. Lens centers19/29 at y24,r2; face top13, bun top4, bottom44. Ears and parted hair omitted for clearance.\nReference: human_ref/user.svg circular head vocabulary; Lucide glasses paired circles and short bridge.\nKeyshape fitted to exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dec0f26b-6bfa-439d-afa0-f23e952da678'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_21/great grandmother_dec0f26b-6bfa-439d-afa0-f23e952da678.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'smiling-woman-head-with-bun-and-glasses'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('smiling', 'woman', 'head', 'with', 'bun', 'and', 'glasses')

    def build(self):
        def path(name, start, steps, closed=False):
            members = []
            point = start
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

        def circle(name, x, y, radius):
            path(name, (x-radius,y), [((x+radius,y),radius,radius,True),
                 ((x-radius,y),radius,radius,True)], True)

        def box(name, left, top, right, bottom, radius):
            r = radius
            path(name, (left+r,top), [(right-r,top), ((right,top+r),r,r,True),
                 (right,bottom-r), ((right-r,bottom),r,r,True), (left+r,bottom),
                 ((left,bottom-r),r,r,True), (left,top+r), ((left+r,top),r,r,True)], True)

        path('face',(16,13),[(32,13),((40,21),8,8,True),(40,28),((8,28),16,16,True),(8,21),((16,13),8,8,True)],True)
        path('bun',(16,13),[((32,13),8,9,True)]);self.relate('connect','bun','face')
        for j,x in enumerate((19,29)):circle(f'lens-{j}',x,24,2)
        self.add_line('bridge',(21,24),(27,24))
        for j in range(2):self.relate('connect','bridge',f'lens-{j}')
        path('smile',(22,34),[((26,34),2,1,False)])
