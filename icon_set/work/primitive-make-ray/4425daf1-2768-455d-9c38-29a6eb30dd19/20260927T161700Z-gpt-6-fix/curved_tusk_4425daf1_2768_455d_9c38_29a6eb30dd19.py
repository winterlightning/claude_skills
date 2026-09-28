'Curved Pointed Animal Tusk.\nPlan: Broad rounded root at left and tapering upward tip at42,6. Lower outside quarter arc and inner sweeping arc; seam omitted.\nReference: Lucide droplet: coherent narrowing silhouette; deliberate asymmetry preserves tusk direction.\nKeyshape: SQUARE, exact SOLO48 envelope.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '4425daf1-2768-455d-9c38-29a6eb30dd19'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__curved-tusk/20260927T161452Z-thuan-mac-1/reference/tusk_4425daf1-2768-455d-9c38-29a6eb30dd19.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'curved-tusk'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('curved', 'tusk')

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

        path('tusk',(10,42),[((6,38),4,4,True),(6,30),((10,26),4,4,True),(18,26),((42,6),24,20,False),((10,42),32,36,True)],True)
        # The source separates the blunt root from the curving point.
        self.add_line('root-seam',(18,26),(18,40))
        self.relate('connect','tusk','root-seam')
