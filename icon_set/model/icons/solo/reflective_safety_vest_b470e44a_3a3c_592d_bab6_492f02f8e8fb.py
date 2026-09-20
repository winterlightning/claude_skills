'High Visibility Safety Vest.\nSymbol plan: Two symmetric vest panels with V neck and curved armholes. Shared center seam and one broad reflective band. Box(8,4)-(40,44).\nConstruction reference: Lucide shirt: intrinsic neckline and armholes; source sleeveless vest retained.\nOriginal reference: SOURCE_PATH below.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b470e44a-3a3c-592d-bab6-492f02f8e8fb'
SOURCE_PATH = 'pictographic-primitives/wayfinding/safety vest_b470e44a-3a3c-592d-bab6-492f02f8e8fb.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'reflective-safety-vest'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('reflective', 'safety', 'vest')

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

        path('vest',(8,4),[(16,4),(24,20),(32,4),(40,4),(40,16),(36,24),(40,28),(40,36),(40,40),((36,44),4,4,True),(24,44),(12,44),((8,40),4,4,True),(8,36),(8,28),(12,24),(8,16),(8,4)],True)
        self.add_polyline('seam',(24,20),(24,28),(24,36),(24,44));self.relate('connect','vest','seam')
        for j,y in enumerate((28,36)):
         self.add_polyline(f'band-{j}',(8,y),(24,y),(40,y));self.relate('connect','band-'+str(j),'vest');self.relate('connect','band-'+str(j),'seam')
