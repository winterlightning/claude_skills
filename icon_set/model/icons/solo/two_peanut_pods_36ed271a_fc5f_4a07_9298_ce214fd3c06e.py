'Pair of Peanuts.\nPlan: Two separate double-lobed peanut pods at upper-right and lower-left. Shared24x12 shape has rounded ends and a shallow waist; bounds6..42. Shell texture omitted.\nReference: Lucide bean: rounded organic lobes reduced to coherent arcs; source paired arrangement.\nKeyshape fitted to exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '36ed271a-fc5f-4a07-9298-ce214fd3c06e'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_19/food allegic peanut 4_36ed271a-fc5f-4a07-9298-ce214fd3c06e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'two-peanut-pods'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('two', 'peanut', 'pods')

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

        for j,(x,y) in enumerate(((18,6),(6,30))):
         path(f'pod-{j}',(x+6,y),[((x,y+6),6,6,False),((x+6,y+12),6,6,False),(x+12,y+10),(x+18,y+12),((x+24,y+6),6,6,False),((x+18,y),6,6,False),(x+12,y+2),(x+6,y)],True)
