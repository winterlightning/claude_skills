'Video Game Controller.\nSymbol plan: Mirrored rounded grips reach(4,8)-(44,40), two thumbstick circles radius2 centered(16,21)/(32,21). Shallow upper notch and lower grip opening retained.\nConstruction reference: Lucide gamepad-2: continuous grip outline and sparse controls.\nOriginal reference: SOURCE_PATH below.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a65bc77c-6835-5101-a87d-a93ba7fad5b2'
SOURCE_PATH = 'pictographic-primitives/video-games/batch-08/playstation controller_a65bc77c-6835-5101-a87d-a93ba7fad5b2.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'gamepad-with-paired-thumbsticks'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "video-games"
    categories = ("primitives", "video-games")
    aliases = ()
    keywords = ('gamepad', 'with', 'paired', 'thumbsticks')

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
        for j,x in enumerate((16,32)): circle(f'stick-{j}',x,21,2)
