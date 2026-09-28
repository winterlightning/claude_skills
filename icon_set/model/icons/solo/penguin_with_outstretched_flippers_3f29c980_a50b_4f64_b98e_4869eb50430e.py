'Cute penguin character.\nSymbol plan: Mirrored rounded penguin head, flippers, short feet and broad belly arch meeting the body at(14,34)/(34,34). Two eyes at(20,16)/(28,16). Tiny beak omitted to retain the distinctive belly.\nConstruction reference: No useful exact Lucide penguin match; mirrored coherent bird contour and minimal facial marks.\nOriginal reference: SOURCE_PATH below.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3f29c980-a50b-4f64-b98e-4869eb50430e'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_39/video game antarctic adventure_3f29c980-a50b-4f64-b98e-4869eb50430e.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'penguin-with-outstretched-flippers'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('penguin', 'with', 'outstretched', 'flippers')

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

        path('body',(11,24),[(11,17),((24,4),13,13,True),((37,17),13,13,True),(37,24),(40,24),(34,34),(34,38),(32,40),(28,44),(20,44),(16,40),(14,38),(14,34),(8,24),(11,24)],True)
        for j,x in enumerate((20,28)):self.add_dot(f'eye-{j}',(x,16))
        path('belly',(14,34),[((24,24),10,10,True),((34,34),10,10,True)])
        self.relate('connect','belly','body')
        self.add_line('foot-left',(14,44),(20,44));self.add_line('foot-right',(28,44),(34,44))
        self.relate('connect','body','foot-left');self.relate('connect','body','foot-right')
