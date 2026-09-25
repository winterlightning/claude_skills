'Two Top One Bottom Layout.\nPlan: Rounded frame with full horizontal divider and upper center divider. Bounds6..42.\nConstruction reference: Lucide panels-top-left originals and atomic-debug; coherent rounded frame and attached dividers.\nReduction: Keep the defining silhouette and essential parts.\nKeyshape: SQUARE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0761f769-8f30-4e61-80e1-22be7c44ebae'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_25/layout 9_0761f769-8f30-4e61-80e1-22be7c44ebae.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'layout-two-upper-panes'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('layout', 'two', 'upper', 'panes')

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

        box('frame',6,6,42,42)
        self.add_line('horizontal',(6,24),(42,24));self.add_line('vertical',(24,6),(24,24))
        self.relate('connect','frame','horizontal');self.relate('connect','frame','vertical');self.relate('connect','horizontal','vertical')
