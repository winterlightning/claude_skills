'Ocean Liner on Waves.\nPlan: Side-view liner with connected hull, cabin and smokestack. Bounds4,8..44,40. Omit water ripple detail to retain cabin and hull openings.\nReference: Lucide ship: coherent hull with attached cabin; source side view retained.\nKeyshape fitted to exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '07291854-1f36-49c3-937a-570ed40dce8d'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_25/liner_07291854-1f36-49c3-937a-570ed40dce8d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'small-liner-on-water'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('small', 'liner', 'on', 'water')

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

        self.add_polyline('hull',(4,24),(12,24),(32,24),(44,24),(36,40),(8,40),closed=True)
        self.add_polyline('cabin',(12,24),(16,16),(20,16),(28,16),(32,24));self.relate('connect','cabin','hull')
        self.add_polyline('stack',(20,16),(20,8),(28,8),(28,16));self.relate('connect','stack','cabin')
