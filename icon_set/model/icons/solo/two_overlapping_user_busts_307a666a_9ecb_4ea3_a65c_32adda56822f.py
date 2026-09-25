'Two People Figures.\nPlan: Two equal round heads above overlapping rounded shoulders. Heads radius5 at15/33,y11; shoulders top24 giving exact4 ink gap. Bounds6..42; right shoulder partially occluded.\nReference: human_ref/user.svg: equal circular heads and rounded shoulder strokes; source overlap retained.\nKeyshape: SQUARE, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '307a666a-9ecb-4ea3-a65c-32adda56822f'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_18/fellow_307a666a-9ecb-4ea3-a65c-32adda56822f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'two-overlapping-user-busts'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('two', 'overlapping', 'user', 'busts')

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

        for j,x in enumerate((15,33)):circle(f'head-{j}',x,11,5)
        path('left-body',(6,42),[(6,33),((15,24),9,9,True),(18,24),((27,33),9,9,True),(27,42)])
        path('right-body',(33,24),[((42,33),9,9,True),(42,42)])
