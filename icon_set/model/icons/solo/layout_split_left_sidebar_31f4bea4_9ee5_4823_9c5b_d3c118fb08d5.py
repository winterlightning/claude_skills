'Three Panel Grid Layout.\nPlan: Rounded frame with a split left sidebar and a full-height right pane.\nConstruction reference: Lucide table: shared partition junctions inside a rounded frame.\nReduction: Left panes equalized; both near-identical source layouts share this concept.\nKeyshape: SQUARE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '31f4bea4-9ee5-4823-9c5b-d3c118fb08d5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_25/layout 19_31f4bea4-9ee5-4823-9c5b-d3c118fb08d5.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'layout-split-left-sidebar'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'design'
    categories = ('design', 'primitive', 'primitives')
    aliases = ()
    keywords = ('layout', 'split', 'left', 'sidebar')

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

        box('frame',6,6,42,42,4)
        self.add_polyline('vertical',(24,6),(24,24),(24,42));self.relate('connect','vertical','frame')
        self.add_line('horizontal',(6,24),(24,24));self.relate('connect','horizontal','frame');self.relate('connect','horizontal','vertical')

SOURCE_REFERENCES = [('dad53ab4-ff1c-4177-b122-a8e6f43fe7ff', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_25/layout 21_dad53ab4-ff1c-4177-b122-a8e6f43fe7ff.svg'), ('3f0fe35d-a077-42b6-a4a0-3e97b71f5323', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_25/layout 8_3f0fe35d-a077-42b6-a4a0-3e97b71f5323.svg')]
