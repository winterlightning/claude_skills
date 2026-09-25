'Heartbeat Pulse Rate.\nPlan: One continuous pulse stroke with unequal peaks and a deep trough; flat baseline at both ends.\nConstruction reference: Lucide activity: continuous trace and distinct peak/trough rhythm.\nReduction: No omissions.\nKeyshape: HRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd9e7e403-cd0a-42ac-a1f0-40f2dd09a8d9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_21/graph stats_d9e7e403-cd0a-42ac-a1f0-40f2dd09a8d9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'pulse-trace-with-two-peaks'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('pulse', 'trace', 'with', 'two', 'peaks')

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

        self.add_polyline('pulse',(4,24),(14,24),(20,8),(26,40),(32,16),(36,24),(44,24))
