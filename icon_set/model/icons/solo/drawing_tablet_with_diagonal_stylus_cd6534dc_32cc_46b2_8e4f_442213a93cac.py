'Digital Drawing Tablet with Stylus.\nPlan: Rounded tablet with upper-right opening for a diagonal stylus and one control point. Inner screen and second control omitted. Bounds6..42.\nReference: No useful local Lucide tablet-pen match; source stylus diagonal retained with coherent rounded tablet.\nKeyshape: SQUARE, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cd6534dc-32cc-46b2-8e4f-442213a93cac'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_21/graphic tablet draw 1_cd6534dc-32cc-46b2-8e4f-442213a93cac.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'drawing-tablet-with-diagonal-stylus'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('drawing', 'tablet', 'with', 'diagonal', 'stylus')

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

        path('tablet',(18,16),[(10,16),((6,20),4,4,False),(6,38),((10,42),4,4,False),(38,42),((42,38),4,4,False),(42,24)])
        self.add_line('stylus',(22,28),(42,6));self.add_dot('control',(32,33))
