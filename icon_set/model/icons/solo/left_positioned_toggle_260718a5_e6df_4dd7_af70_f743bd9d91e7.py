'Horizontal Toggle Switch Off.\nPlan: Wide capsule track with one left-positioned circular knob.\nConstruction reference: Lucide toggle-left: capsule and left knob with generous internal clearance.\nReduction: No omissions.\nKeyshape: HRECT_M; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '260718a5-e6df-4dd7-af70-f743bd9d91e7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_38/toggle large on_260718a5-e6df-4dd7-af70-f743bd9d91e7.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'left-positioned-toggle'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('left', 'positioned', 'toggle')

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

        path('track',(18,10),[(30,10),((44,24),14,14,True),((30,38),14,14,True),(18,38),((4,24),14,14,True),((18,10),14,14,True)],True)
        circle('knob',18,24,5)
