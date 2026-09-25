'Hand Wash Laundry Symbol.\nPlan: Downward hand above a wavy laundry basin.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Finger creases omitted; hand remains visibly separate above the water surface.\nKeyshape: SQUARE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a4f18a57-0c02-4aa1-b46a-d6e8fea6bc96'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_25/laundry hand wash_a4f18a57-0c02-4aa1-b46a-d6e8fea6bc96.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hand-wash-laundry'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('hand', 'wash', 'laundry')

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

        path('hand',(14,6),[(14,17),((22,17),4,4,False),(22,12),(30,12),(34,20),(42,20)])
        path('basin',(6,32),[(10,42),(38,42),(42,32)])
        path('water',(6,32),[((18,32),6,2,False),((30,32),6,2,True),((42,32),6,2,False)])
        self.relate('connect','water','basin')
