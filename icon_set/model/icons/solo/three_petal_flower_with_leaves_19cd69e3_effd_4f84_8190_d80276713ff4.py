'Flower with Stem and Leaves.\nSymbol plan: Three-lobed flower above stem and two staggered pointed leaves. Center circle and leaf veins omitted. Left leaf spans y25–35, right leaf y34–44, with readable openings.\nConstruction reference: Lucide flower-2: lobed bloom, single stem and joined leaves.\nOriginal reference: SOURCE_PATH below.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '19cd69e3-effd-4f84-8190-d80276713ff4'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_21/gladiolus_19cd69e3-effd-4f84-8190-d80276713ff4.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'three-petal-flower-with-leaves'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('three', 'petal', 'flower', 'with', 'leaves')

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

        path('bloom',(18,10),[((24,4),6,6,True),((30,10),6,6,True),((36,14),6,5,True),((24,18),12,4,True),((12,14),12,4,True),((18,10),6,5,True)],True)
        self.add_polyline('stem',(24,18),(24,35),(24,44));self.relate('connect','bloom','stem')
        path('left-leaf',(24,35),[((8,25),16,10,False),((24,35),16,10,False)],True)
        path('right-leaf',(24,44),[((40,34),16,10,False),((24,44),16,10,False)],True)
        self.relate('connect','stem','left-leaf');self.relate('connect','stem','right-leaf')
