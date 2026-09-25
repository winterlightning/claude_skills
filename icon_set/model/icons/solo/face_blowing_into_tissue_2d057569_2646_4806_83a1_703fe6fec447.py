'Face Blowing Nose with Tissue.\nPlan: Circular face with centered closed eyes and a folded tissue interrupting the lower face outline. Eye centers18/30, tissue wide enough to show its folds. Bounds6..42.\nReference: Human circular face vocabulary; source closed eyes and large tissue; no useful Lucide exact match.\nKeyshape fitted to exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2d057569-2646-4806-83a1-703fe6fec447'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_18/face tissue_2d057569-2646-4806-83a1-703fe6fec447.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'face-blowing-into-tissue'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('face', 'blowing', 'into', 'tissue')

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

        path('face',(10,34),[((6,24),18,18,True),((42,24),18,18,True),((38,34),18,18,True)])
        for j,x in enumerate((18,30)):path(f'eye-{j}',(x-2,19),[((x+2,19),2,1,False)])
        self.add_polyline('tissue',(10,34),(18,28),(30,28),(38,34),(34,42),(24,38),(14,42),(10,34))
        self.relate('connect','face','tissue')
