'Water Bed with Waves.\nPlan: Wide rounded mattress divided by a shallow water wave, shared sidewall junctions. Bounds4,10..44,38.\nReference: No useful local Lucide waterbed match; rounded mattress and coherent wave from source.\nKeyshape: HRECT_M, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3a4c0338-1ec1-482a-88b4-072b5e8b6b16'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_40/waterbed_3a4c0338-1ec1-482a-88b4-072b5e8b6b16.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'waterbed-mattress'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('waterbed', 'mattress')

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

        path('mattress',(10,10),[(38,10),((44,16),6,6,True),(44,24),(44,32),((38,38),6,6,True),(10,38),((4,32),6,6,True),(4,24),(4,16),((10,10),6,6,True)],True)
        path('water',(4,24),[((24,24),10,2,False),((44,24),10,2,True)]);self.relate('connect','water','mattress')
