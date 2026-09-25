'Kitchen Oven Appliance.\nSymbol plan: Rounded SQUARE oven shell(6,6)-(42,42), divider y24 and three repeated round knob marks x15/24/33,y15. Lower door stays plain.\nConstruction reference: No exact Lucide oven match; rounded cabinet construction like refrigerator inspected in preceding batch.\nOriginal reference: SOURCE_PATH below.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '60f4eb7a-cdc1-4941-98b0-fe05e2ef4eea'
SOURCE_PATH = 'pictographic-primitives/other/oven 1_60f4eb7a-cdc1-4941-98b0-fe05e2ef4eea.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'three-knob-kitchen-oven'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("container", "other", "primitives-generate")
    aliases = ()
    keywords = ('three', 'knob', 'kitchen', 'oven')

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

        path('shell',(10,6),[(38,6),((42,10),4,4,True),(42,24),(42,38),((38,42),4,4,True),(10,42),((6,38),4,4,True),(6,24),(6,10),((10,6),4,4,True)],True)
        self.add_line('divider',(6,24),(42,24));self.relate('connect','shell','divider')
        for j,x in enumerate((15,24,33)):self.add_dot(f'knob-{j}',(x,15))
