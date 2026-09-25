'Hourglass Starting To Flow.\nSymbol plan: Curved hourglass with upper sand level and one lower falling grain. Detailed sand mound and stream omitted to preserve throat clearance.\nConstruction reference: Lucide hourglass: coherent mirrored neck curves and flat ends.\nOriginal reference: SOURCE_PATH below.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1611860a-84bc-43dc-bd45-4c97034225ef'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_23/hourglass start_1611860a-84bc-43dc-bd45-4c97034225ef.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'hourglass-starting-to-flow'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('hourglass', 'starting', 'to', 'flow')

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

        path('glass',(8,4),[(40,4),(40,8),((30,24),18,18,True),((40,40),18,18,False),(40,44),(8,44),(8,40),((18,24),18,18,False),((8,8),18,18,True),(8,4)],True)
        self.add_line('sand-top',(18,13),(30,13))
        self.add_dot('sand-bottom',(24,35))
