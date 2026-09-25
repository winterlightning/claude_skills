'Two Overlapping Camping Tents.\nPlan: Triangular front and broad side joined by horizontal ridge. Entrance reduced to short center seam. Bounds4,8..44,40.\nReference: Lucide tent: triangular sides and shared base; source perspective ridge retained.\nKeyshape: HRECT_L, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8c12b85b-0398-481e-9425-0c9f848d74b1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_37/tents_8c12b85b-0398-481e-9425-0c9f848d74b1.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'perspective-camping-tent'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('perspective', 'camping', 'tent')

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

        self.add_polyline('outline',(4,40),(16,8),(32,8),(44,40),(28,40),(16,40),closed=True)
        self.add_line('front-slope',(16,8),(28,40));self.relate('connect','front-slope','outline')
        self.add_line('entrance',(16,32),(16,40));self.relate('connect','entrance','outline')
