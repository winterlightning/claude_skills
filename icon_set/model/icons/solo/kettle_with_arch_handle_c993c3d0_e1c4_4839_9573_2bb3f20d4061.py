'Traditional Tea Kettle.\nPlan: Rounded kettle body with tall arch handle, central lid knob and broad rising spout sharing the right wall. Bounds6..42.\nReference: Lucide cooking-pot: shared body/lid construction; source tall handle and right spout retained.\nKeyshape: SQUARE, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c993c3d0-e1c4-4839-9573-2bb3f20d4061'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_24/kettle_c993c3d0-e1c4-4839-9573-2bb3f20d4061.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'kettle-with-arch-handle'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('kettle', 'with', 'arch', 'handle')

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

        path('body',(10,24),[(20,24),(30,24),((34,28),4,4,True),(34,32),(34,38),(34,42),(30,42),(10,42),((6,38),4,4,True),(6,28),((10,24),4,4,True)],True)
        path('handle',(6,28),[(6,20),((34,20),14,14,True),(34,28)]);self.relate('connect','handle','body')
        self.add_line('knob',(20,16),(20,24));self.relate('connect','knob','body')
        self.add_polyline('spout',(34,28),(42,20),(42,34),(34,42));self.relate('connect','spout','body');self.relate('connect','spout','handle')
