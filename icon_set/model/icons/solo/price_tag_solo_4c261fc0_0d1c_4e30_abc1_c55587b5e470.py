'Retail Product Price Tag.\nPlan: Diagonal clipped tag with rounded upper-right corner and small round punched hole. Bounds6..42.\nReference: Lucide tag: clipped polygon and tiny punched eye; source direction points upper-right.\nKeyshape: SQUARE, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4c261fc0-0d1c-4e30-abc1-c55587b5e470'
SOURCE_PATH = 'pictographic-primitives/other/tag_4c261fc0-0d1c-4e30-abc1-c55587b5e470.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'price-tag-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('price', 'tag', 'solo')

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

        path('tag',(6,26),[(26,6),(34,6),((42,14),8,8,True),(42,26),(26,42),(6,26)],True)
        circle('hole',30,18,2)
