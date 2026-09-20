'Plus Sign and Dot Sparkles.\nPlan: Large plus at left, dot in center and smaller plus at right. Bounds4,10..44,38.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Preserve the visible two crosses and dot; do not invent slime from the filename.\nKeyshape: HRECT_M; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '91a7c45e-5aa1-4a35-82fe-2336553239bd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/making slime_91a7c45e-5aa1-4a35-82fe-2336553239bd.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'sparkle-marks'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('sparkle', 'marks')

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

        self.add_line('large-horizontal',(4,24),(22,24));self.add_line('large-vertical',(13,10),(13,38));self.relate('connect','large-horizontal','large-vertical')
        self.add_dot('dot',(31,27))
        self.add_line('small-horizontal',(36,16),(44,16));self.add_line('small-vertical',(40,12),(40,20));self.relate('connect','small-horizontal','small-vertical')
