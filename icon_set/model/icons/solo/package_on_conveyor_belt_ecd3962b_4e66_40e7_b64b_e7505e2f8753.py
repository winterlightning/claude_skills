'Package on Conveyor Belt.\nPlan: Package resting on capsule conveyor with three roller marks. Bounds4,8..44,40.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Omit tiny package sealing tab; retain three rollers.\nKeyshape: HRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ecd3962b-4e66-40e7-b64b-e7505e2f8753'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/conveyor belt_ecd3962b-4e66-40e7-b64b-e7505e2f8753.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'package-on-conveyor-belt'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('package', 'on', 'conveyor', 'belt')

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

        box('belt',4,22,44,40,8)
        self.add_polyline('package',(12,22),(12,8),(36,8),(36,22));self.relate('connect','belt','package')
        for x in (14,24,34):self.add_dot('roller-'+str(x),(x,31))
