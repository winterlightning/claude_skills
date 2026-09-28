"""Small side-view liner with a sloped hull, compact bridge, funnel, and separate wave. The local Lucide ship informed connected hull construction; the source sets the side profile."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '07291854-1f36-49c3-937a-570ed40dce8d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__small-liner-on-water/20260927T172707Z-thuan-mac-1/reference/liner_07291854-1f36-49c3-937a-570ed40dce8d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'small-liner-on-water'
    keyshape = Keyshape.SQUARE
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

        # Low open hull, compact bridge, one funnel and the water line below.
        self.add_polyline('hull',(6,22),(42,22),(34,30),(10,30),closed=True)
        self.add_polyline('cabin',(14,22),(18,14),(30,14),(34,22));self.relate('connect','cabin','hull')
        self.add_polyline('stack',(20,14),(20,6),(29,6),(29,14));self.relate('connect','stack','cabin')
        self.add_bezier('water',(6,42),((12,38),(18,38),(24,42)),((30,38),(36,38),(42,42)))
