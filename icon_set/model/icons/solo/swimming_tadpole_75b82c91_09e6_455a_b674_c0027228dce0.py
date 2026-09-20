'Swimming Tadpole Organism.\nSymbol plan: Rounded head at upper right flows into an asymmetric S-curved tail tapering lower left. No eye added. Extremes(6,6)-(42,42).\nConstruction reference: Lucide fish: smooth body-to-tail transition; original tadpole silhouette preserved.\nOriginal reference: SOURCE_PATH below.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '75b82c91-09e6-455a-b674-c0027228dce0'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_37/tadpole_75b82c91-09e6-455a-b674-c0027228dce0.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'swimming-tadpole'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('swimming', 'tadpole')

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

        path('tadpole',(18,24),[((18,18),8,8,False),((30,6),12,12,True),((42,18),12,12,True),((30,30),12,12,True),((22,34),10,10,False),(6,42),(10,30),((18,24),10,10,True)],True)
