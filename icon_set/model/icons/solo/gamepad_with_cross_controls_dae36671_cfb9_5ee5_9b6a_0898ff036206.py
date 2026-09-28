'Video Game Controller.\nSymbol plan: Continuous broad gamepad silhouette with paired upper controls and a shallow lower grip notch. Lower extra cross omitted.\nConstruction reference: Lucide gamepad-2: wide rounded grips and prominent direction controls.\nOriginal reference: SOURCE_PATH below.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dae36671-cfb9-5ee5-9b6a-0898ff036206'
SOURCE_PATH = 'pictographic-primitives/video-games/batch-13/xbox controller_dae36671-cfb9-5ee5-9b6a-0898ff036206.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'gamepad-with-cross-controls'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "video-games"
    categories = ("primitives", "video-games")
    aliases = ()
    keywords = ('gamepad', 'with', 'cross', 'controls')

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

        path('body',(12,8),[(18,10),(30,10),(36,8),((44,16),8,8,True),(44,32),((32,32),6,8,True),(28,32),(20,32),(16,32),((4,32),6,8,True),(4,16),((12,8),8,8,True)],True)
        circle('round-control',16,21,2)
        self.add_polyline('horizontal',(30,21),(32,21),(34,21))
        self.add_polyline('vertical',(32,19),(32,21),(32,23))
        self.relate('connect','horizontal','vertical')
