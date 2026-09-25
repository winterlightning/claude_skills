'Apple with Honey Jar and Dipper.\nPlan: Apple below-right of honey dipper, with one hanging drip and diagonal handle.\nConstruction reference: Lucide apple: lobe-based fruit contour; source dipper and dripping honey retained.\nReduction: Dipper grooves reduced to a bold head and one drip.\nKeyshape: SQUARE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'efb1f8f3-2844-4c28-87ad-415937bd4b08'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_22/honey apple_efb1f8f3-2844-4c28-87ad-415937bd4b08.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'apple-with-dripping-honey-dipper'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('apple', 'with', 'dripping', 'honey', 'dipper')

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

        path('apple',(30,28),[((24,26),6,6,False),((19,32),5,6,False),((26,42),7,10,False),(30,40),(34,42),((42,32),8,10,False),((36,26),6,6,False),((30,28),6,6,False)],True)
        self.add_line('stem',(30,28),(34,20));self.relate('connect','stem','apple')
        box('dipper',6,6,18,18,4)
        self.add_line('handle',(18,10),(34,6));self.relate('connect','handle','dipper')
        self.add_line('honey',(10,18),(10,32));self.relate('connect','honey','dipper')
