'Hand Drawing a House.\nPlan: A diagonal fingertip touches the upper-right house edge; the hand occludes the right wall.\nConstruction reference: Lucide house and hand: angular roof and rounded index finger.\nReduction: Right wall is occluded by the touching hand.\nKeyshape: SQUARE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1f58e0b9-2d9d-4e01-88b6-5e110128d93c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_20/ginger bread house_1f58e0b9-2d9d-4e01-88b6-5e110128d93c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'finger-touching-house-outline'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('finger', 'touching', 'house', 'outline')

    def build(self):

        def path(name, start, steps, closed=False):
            members, point = [], start
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

        def ellipse(name, x, y, rx, ry):
            path(name, (x-rx,y), [((x+rx,y),rx,ry,True), ((x-rx,y),rx,ry,True)], True)

        def circle(name, x, y, radius):
            ellipse(name,x,y,radius,radius)

        def box(name, left, top, right, bottom, radius=4):
            r = radius
            path(name, (left+r,top), [(right-r,top), ((right,top+r),r,r,True),
                 (right,bottom-r), ((right-r,bottom),r,r,True), (left+r,bottom),
                 ((left,bottom-r),r,r,True), (left,top+r), ((left+r,top),r,r,True)], True)

        self.add_polyline('roof',(6,22),(10,18),(22,6),(32,16))
        self.add_polyline('walls',(10,18),(10,42),(24,42));self.relate('connect','roof','walls')
        path('hand',(42,6),[(32,16),(32,20),(24,28),((32,36),6,6,False),(42,26)])
        self.relate('connect','roof','hand')
