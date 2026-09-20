'Vulcan Salute Hand Gesture.\nPlan: Raised palm with four staggered rounded fingertips and thumb projecting right. Exact6..42.\nConstruction reference: Lucide hand originals and atomic-debug for rounded fingers and continuous palm.\nReduction: Reduce wrist detail and thumb length; retain all four raised fingers.\nKeyshape: SQUARE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e707413f-0adc-48cf-b5cf-de4b6e2e3b22'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_39/vulcan salute 2_e707413f-0adc-48cf-b5cf-de4b6e2e3b22.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'vulcan-salute-hand'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('vulcan', 'salute', 'hand')

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

        path('hand',(6,26),[(6,18),((14,18),4,4,True),(14,12),((22,12),4,4,True),(22,10),((30,10),4,4,True),(30,14),((38,14),4,4,True),(38,22),(42,22),(42,26),((24,42),18,16,True),((6,26),18,16,True)],True)
        for x,y in ((14,18),(22,12),(30,14)):
         self.add_line(f'finger-{x}',(x,y),(x,26));self.relate('connect','hand',f'finger-{x}')
