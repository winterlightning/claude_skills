'Horizontal Center Alignment.\nPlan: Unequal horizontal bars centered on one guide. Structural guide shares the bars at their exact center nodes.\nConstruction reference: Lucide network: centered connecting guide and geometric bars.\nReduction: Guide remains visible through both bar centers.\nKeyshape: VRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0e1df90f-62f9-43ae-a7f3-da34a63d86b4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_01/align center_0e1df90f-62f9-43ae-a7f3-da34a63d86b4.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'center-aligned-horizontal-bars'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('center', 'aligned', 'horizontal', 'bars')

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

        self.add_polyline('top-bar',(16,10),(24,10),(32,10), (36,14),(36,18),(32,22),(24,22),(16,22),(12,18),(12,14),closed=True)
        self.add_polyline('bottom-bar',(12,30),(24,30),(36,30),(40,34),(40,38),(36,42),(24,42),(12,42),(8,38),(8,34),closed=True)
        self.add_polyline('guide',(24,4),(24,10),(24,22),(24,30),(24,42),(24,44))
        self.relate('connect','guide','top-bar');self.relate('connect','guide','bottom-bar')
