'Hands Protecting Water Drop.\nPlan: Central water drop above paired upturned hands and cuffs.\nConstruction reference: Lucide hand-heart and droplet: mirrored palms around a teardrop.\nReduction: Cuffs merged into wrist endpoints.\nKeyshape: SQUARE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e4877261-473e-44ea-bd3c-dbd7199f163e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_40/water protection drop hold_e4877261-473e-44ea-bd3c-dbd7199f163e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hands-protecting-water'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('hands', 'protecting', 'water')

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

        path('drop',(24,6),[(20,14),((28,14),4,6,False),(24,6)],True)
        path('left-hand',(6,42),[(6,26),((14,26),4,4,True),(14,34),(24,42)])
        path('right-hand',(42,42),[(42,26),((34,26),4,4,False),(34,34),(24,42)])
        self.relate('connect','left-hand','right-hand')
