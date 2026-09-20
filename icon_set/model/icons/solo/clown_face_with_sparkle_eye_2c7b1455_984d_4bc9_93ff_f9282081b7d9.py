'Smiling Clown Face.\nPlan: Open clown face with large nose, one sparkle eye, round opposite eye and low curved smile. Sparkle reduced to crossed rounded strokes. Bounds6..42.\nReference: Lucide party-popper: sparse celebratory strokes; clown features reconstructed from source.\nKeyshape: SQUARE, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2c7b1455-984d-4bc9-93ff-f9282081b7d9'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_20/funny face_2c7b1455-984d-4bc9-93ff-f9282081b7d9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'clown-face-with-sparkle-eye'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('clown', 'face', 'with', 'sparkle', 'eye')

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

        self.add_polyline('sparkle-v',(14,6),(14,14),(14,22))
        self.add_polyline('sparkle-h',(6,14),(14,14),(22,14));self.relate('connect','sparkle-v','sparkle-h')
        circle('eye',37,12,3);circle('nose',26,25,3)
        path('smile',(6,32),[((42,32),18,10,False)])
