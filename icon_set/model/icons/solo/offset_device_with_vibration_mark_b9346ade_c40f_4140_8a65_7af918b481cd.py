'Haptic Feedback Vibration Motor.\nPlan: Two offset rounded device parts joined by a short diagonal neck; zigzag vibration cue upper-left.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Rounded forms simplified to oblong contours; connecting neck retained.\nKeyshape: HRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b9346ade-c40f-4140-8a65-7af918b481cd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_22/haptic sensor vibration_b9346ade-c40f-4140-8a65-7af918b481cd.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'offset-device-with-vibration-mark'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('offset', 'device', 'with', 'vibration', 'mark')

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

        box('upper',26,12,44,22,5)
        box('lower',4,28,28,40,6)
        self.add_line('connector',(32,22),(20,28));self.relate('connect','connector','upper');self.relate('connect','connector','lower')
        self.add_polyline('vibration',(4,16),(8,8),(16,14),(16,8))
