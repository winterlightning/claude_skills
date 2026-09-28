'Universal Prohibited Symbol.\nSymbol plan: Circle centered24 with radius20. Descending slash joins circle at the exact integer 12/16 radius points.\nConstruction reference: Lucide ban: one ring and a diagonal chord.\nOriginal reference: SOURCE_PATH below.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'badfb3fb-3163-4fe5-ac3e-3bdfcaf0174b'
SOURCE_PATH = 'pictographic-primitives/other/prohitbition_badfb3fb-3163-4fe5-ac3e-3bdfcaf0174b.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'prohibition-circle-descending-slash'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("container", "other", "primitives-generate")
    aliases = ()
    keywords = ('prohibition', 'circle', 'descending', 'slash')

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

        path('ring',(12,8),[((36,40),20,20,True),((12,8),20,20,True)],True)
        self.add_line('slash',(12,8),(36,40))
        self.relate('connect','ring','slash')
