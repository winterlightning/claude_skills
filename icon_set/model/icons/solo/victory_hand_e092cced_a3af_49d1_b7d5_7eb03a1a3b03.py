'Victory Hand Gesture.\nPlan: Victory hand with separated long fingers, rounded palm and open wrist. Bounds10,4..38,44.\nConstruction reference: Lucide hand continuous outline and rounded finger ends; source V gesture.\nReduction: Reduce folded-finger/thumb folds to one open palm crease.\nKeyshape: VRECT_M; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e092cced-a3af-49d1-b7d5-7eb03a1a3b03'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_38/toys finger_e092cced-a3af-49d1-b7d5-7eb03a1a3b03.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'victory-hand'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('victory', 'hand')

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

        path('hand',(16,44),[(16,38),((10,32),6,6,True),(10,8),((18,8),4,4,True),(22,22),(26,22),(30,8),((38,8),4,4,True),(34,28),(34,36),((30,40),4,4,True),(30,44)])
        
