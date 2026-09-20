'Interlocking Tetris Game Blocks.\nPlan: Three stepped blocks on a shared8-unit module; two touch on left, one offset right. Bounds4,8..44,40.\nReference: Lucide blocks: stepped polygon silhouettes and explicit shared edges.\nKeyshape: HRECT_L, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '89ea164a-d04d-4d12-bd7f-55b7ebb393a2'
SOURCE_PATH = 'pictographic-primitives/video-games/batch-11/tetris_89ea164a-d04d-4d12-bd7f-55b7ebb393a2.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'tetris-block-group'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('tetris', 'block', 'group')

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

        self.add_polyline('upper-left',(4,8),(12,8),(12,16),(20,16),(20,24),(12,24),(4,24),closed=True)
        self.add_polyline('lower-left',(4,24),(12,24),(12,32),(20,32),(20,40),(4,40),closed=True);self.relate('connect','upper-left','lower-left')
        self.add_polyline('right',(28,8),(36,8),(36,16),(44,16),(44,32),(36,32),(36,24),(28,24),closed=True)
