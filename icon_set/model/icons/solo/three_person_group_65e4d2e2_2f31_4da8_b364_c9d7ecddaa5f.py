'Group of Three People.\n\nSymbol plan: Three heads with simplified shoulder outlines. Central head radius5, center(24,13), bottom18; central shoulder top26 yields exact4-unit ink gap. Side heads radius3, centers(7,17)/(41,17), bottom20; body top28 yields the same gap. Interior arm seams omitted.\nConstruction reference: human_ref/user.svg and Lucide users: repeated circular heads and smooth shoulders.\nOriginal reference: SOURCE_PATH below.\n'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '65e4d2e2-2f31-4da8-b364-c9d7ecddaa5f'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_38/troop_65e4d2e2-2f31-4da8-b364-c9d7ecddaa5f.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'three-person-group'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('three', 'person', 'group')

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

        circle('center-head',24,13,5)
        for j,x in enumerate((7,41)): circle(f'side-head-{j}',x,17,3)
        path('center-body',(14,40),[(14,36),((24,26),10,10,True),((34,36),10,10,True),(34,40)])
        path('left-body',(4,40),[(4,31),((7,28),3,3,True)])
        path('right-body',(41,28),[((44,31),3,3,True),(44,40)])
