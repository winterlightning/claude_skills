'Hands Pulling Paper Towel.\nPlan: Wall dispenser, hanging paper with a torn bottom edge and opposed gripping hands.\nConstruction reference: Lucide hand: rounded gripping fingers; geometric dispenser.\nReduction: One torn edge replaces multiple fine towel folds.\nKeyshape: SQUARE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8e334d1c-5734-4a71-968a-6135a8683135'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_40/wayfinding tissue_8e334d1c-5734-4a71-968a-6135a8683135.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'pulling-paper-towel'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('pulling', 'paper', 'towel')

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

        box('dispenser',6,6,42,18,4)
        self.add_polyline('paper',(14,18),(14,34),(20,30),(26,34),(32,30),(34,34),(34,18));self.relate('connect','paper','dispenser')
        path('left-hand',(6,42),[(6,34),((14,34),4,4,True),(14,38)])
        path('right-hand',(42,42),[(42,34),((34,34),4,4,False),(34,38)])
        self.relate('connect','paper','left-hand');self.relate('connect','paper','right-hand')
