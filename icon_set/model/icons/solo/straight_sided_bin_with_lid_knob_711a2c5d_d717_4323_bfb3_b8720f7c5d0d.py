'Trash Can with Lid.\nPlan: Straight bin with rounded bottom, broad lid and centered stem knob. Bounds8,4..40,44.\nReference: Lucide trash-2: separate lid and body with central handle reduced to stem.\nKeyshape: VRECT_L, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '711a2c5d-d717-4323-bfb3-b8720f7c5d0d'
SOURCE_PATH = 'pictographic-primitives/other/trash_711a2c5d-d717-4323-bfb3-b8720f7c5d0d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'straight-sided-bin-with-lid-knob'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('straight', 'sided', 'bin', 'with', 'lid', 'knob')

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

        self.add_polyline('lid',(8,12),(12,12),(24,12),(36,12),(40,12))
        self.add_line('knob',(24,4),(24,12));self.relate('connect','knob','lid')
        path('bin',(12,12),[(12,40),((16,44),4,4,False),(32,44),((36,40),4,4,False),(36,12)]);self.relate('connect','bin','lid')
