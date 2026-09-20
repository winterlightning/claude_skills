'Healthy Carrot Root Vegetable.\nPlan: Broad tapered carrot with three open leaf strokes and one short root mark. Repeated surface marks omitted. Bounds8,4..40,44.\nReference: Lucide carrot: tapering root and tuft, reduced to coherent outline and sparse surface mark.\nKeyshape: VRECT_L, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0a4b8080-9d3a-4c5c-a8b8-7353f1e0033c'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_22/horseradish_0a4b8080-9d3a-4c5c-a8b8-7353f1e0033c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'carrot-root-with-leaf-tuft'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('carrot', 'root', 'with', 'leaf', 'tuft')

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

        path('root',(12,20),[(24,20),(36,20),((40,24),4,4,True),(24,44),(16,34),(8,24),((12,20),4,4,True)],True)
        self.add_polyline('leaves',(10,8),(24,20),(38,8));self.add_line('leaf-center',(24,4),(24,20));self.relate('connect','leaves','root');self.relate('connect','leaf-center','root');self.relate('connect','leaf-center','leaves')
        self.add_line('root-mark',(16,34),(20,34));self.relate('connect','root-mark','root')
