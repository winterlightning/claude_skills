'Horizontal Milestone Timeline Arrow.\nPlan: Upper right arrow and lower timeline with two circle milestones. Shared line/circle endpoints and wide vertical gap. Bounds4,8..44,40.\nReference: No exact Lucide match; coherent timeline diagram per saved brief, separate status badge not inferred.\nKeyshape: HRECT_L, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4537d41f-fa5c-4ffe-a98c-a284311f8d37'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_38/timeline arrow_4537d41f-fa5c-4ffe-a98c-a284311f8d37.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'timeline-with-direction-arrow'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('timeline', 'with', 'direction', 'arrow')

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

        self.add_line('arrow-shaft',(4,16),(44,16))
        self.add_polyline('arrowhead',(36,8),(44,16),(36,24));self.relate('connect','arrow-shaft','arrowhead')
        for j,x in enumerate((10,28)):circle(f'milestone-{j}',x,36,4)
        self.add_line('segment-0',(14,36),(24,36));self.add_line('segment-1',(32,36),(44,36))
        self.relate('connect','segment-0','milestone-0');self.relate('connect','segment-0','milestone-1');self.relate('connect','segment-1','milestone-1')
