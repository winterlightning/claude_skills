'Apple with Stem and Leaf.\nPlan: Broad apple centered x24 with a shallow notch, rounded shoulders and curved stem.\nConstruction reference: Lucide apple: broad shoulders and curved stem.\nReduction: Leaf omitted after crowding repairs; broad fruit proportions retained.\nKeyshape: SQUARE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd1bb3d09-8e65-4d8f-9376-1327277b0224'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_20/fruit apple_d1bb3d09-8e65-4d8f-9376-1327277b0224.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'broad-apple-with-curved-stem'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('broad', 'apple', 'with', 'curved', 'stem')

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

        path('fruit',(24,20),[((15,16),9,4,False),((6,25),9,9,False),((15,42),9,17,False),((24,40),9,2,False),((33,42),9,2,False),((42,25),9,17,False),((33,16),9,9,False),((24,20),9,4,False)],True)
        path('stem',(24,20),[(24,12),((18,6),6,6,False)])
        self.relate('connect','stem','fruit')
