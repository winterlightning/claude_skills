'Hand Holding Acupuncture Needle.\nPlan: Raised index and curved pinching thumb grip a round-headed diagonal acupuncture needle.\nConstruction reference: Lucide hand: rounded index and coherent pinching contour.\nReduction: Fine finger creases removed.\nKeyshape: SQUARE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '219024ce-9973-4736-8ba2-b73e81755a00'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_01/acupuncture hand_219024ce-9973-4736-8ba2-b73e81755a00.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hand-pinching-acupuncture-needle'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('hand', 'pinching', 'acupuncture', 'needle')

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

        path('finger',(42,26),[(24,8),((16,8),4,2,False),(16,12),(26,22),((21,30),6,8,True)])
        circle('pin',18,30,3);self.relate('connect','pin','finger')
        path('palm',(18,33),[((30,40),12,9,False),(42,40)]);self.relate('connect','palm','pin')
        self.add_line('needle',(18,33),(6,42));self.relate('connect','needle','pin');self.relate('connect','needle','palm')

