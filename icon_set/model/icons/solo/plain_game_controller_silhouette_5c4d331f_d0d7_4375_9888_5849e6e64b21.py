'Video Game Controller.\nPlan: Mirrored gamepad silhouette with broad shoulders and two rounded grips. Exact4,10..44,38.\nConstruction reference: Lucide gamepad-2 paired grips and central notch; source empty face retained.\nReduction: Keep the defining silhouette and essential parts.\nKeyshape: HRECT_M; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5c4d331f-d0d7-4375-9888-5849e6e64b21'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_20/gamepad_5c4d331f-d0d7-4375-9888-5849e6e64b21.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'plain-game-controller-silhouette'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('plain', 'game', 'controller', 'silhouette')

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

        path('body',(14,10),[(34,10),((44,20),10,10,True),(44,31),((30,31),7,7,True),(28,28),(20,28),(18,31),((4,31),7,7,True),(4,20),((14,10),10,10,True)],True)
