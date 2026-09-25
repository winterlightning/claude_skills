'Winged Circle Symbol.\nPlan: Round base at lower-left with layered wing sweeping right. Bounds4,8..44,40. Two outer feather tiers, one interior division.\nReference: Lucide feather: coherent feather outline and sparse internal division; source round base retained.\nKeyshape: HRECT_L, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd7cc5400-99c3-58b3-8b89-c51b214e0db0'
SOURCE_PATH = 'pictographic-primitives/video-games/batch-10/shwings_d7cc5400-99c3-58b3-8b89-c51b214e0db0.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'single-wing-with-round-base'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'video-games'
    aliases = ()
    keywords = ('single', 'wing', 'with', 'round', 'base')

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

        circle('base',12,32,8)
        path('wing',(12,24),[((28,8),16,16,True),(44,8),((36,20),8,12,True),((30,30),6,10,True),(20,32)])
        self.relate('connect','wing','base')
        self.add_line('feather',(28,20),(36,20));self.relate('connect','feather','wing')
