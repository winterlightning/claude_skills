'Master Yoda Character Head.\nPlan: Circular upper head and jaw with integrated wide pointed ears and paired eye dots. Ear dividers and forehead wrinkles omitted; collar reduced to short neck. Bounds4,8..44,40.\nReference: No useful local Lucide Yoda match; source wide ears and round character head, human circular face vocabulary.\nKeyshape: HRECT_L, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '71971a82-4494-515a-9221-165cabaf6cc3'
SOURCE_PATH = 'pictographic-primitives/video-games/batch-13/yoda_71971a82-4494-515a-9221-165cabaf6cc3.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'yoda-head'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'video-games'
    categories = ('primitives', 'video-games')
    aliases = ()
    keywords = ('yoda', 'head')

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

        path('head',(12,16),[((24,8),13,13,True),((36,16),13,13,True),(44,12),(36,26),((24,34),13,13,True),((12,26),13,13,True),(4,12),(12,16)],True)
        
        self.add_dot('eye-left',(20,20));self.add_dot('eye-right',(28,20));self.add_line('neck',(24,34),(24,40));self.relate('connect','neck','head')
