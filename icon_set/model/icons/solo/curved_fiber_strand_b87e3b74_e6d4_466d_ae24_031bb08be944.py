'Single Curved Fiber Strand.\nPlan: Single tangent S-like strand from8,44 to40,4; two quarter ellipses meet at24,24 with common vertical tangent.\nReference: No useful Lucide fiber match; minimal uninterrupted source strand.\nKeyshape: VRECT_L, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b87e3b74-e6d4-466d-ae24-031bb08be944'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_18/fibre_b87e3b74-e6d4-466d-ae24-031bb08be944.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'curved-fiber-strand'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('curved', 'fiber', 'strand')

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

        path('fiber',(8,44),[((24,24),16,20,False),((40,4),16,20,True)])
