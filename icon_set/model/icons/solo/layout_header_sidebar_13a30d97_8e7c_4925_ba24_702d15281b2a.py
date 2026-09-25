'Web Page Layout with Sidebar.\nPlan: Rounded webpage frame, full header and lower sidebar; right body divided into two panels. Bounds6..42.\nConstruction reference: Lucide panels-top-left original and atomic-debug: rounded frame and attached orthogonal divisions.\nReduction: Keep the defining silhouette and essential parts.\nKeyshape: SQUARE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '13a30d97-8e7c-4925-ba24-702d15281b2a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_25/layout 5_13a30d97-8e7c-4925-ba24-702d15281b2a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'layout-header-sidebar'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('layout', 'header', 'sidebar')

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
        self.add_line('header',(6,18),(42,18));self.add_line('sidebar',(18,18),(18,42));self.add_line('panel',(18,30),(42,30))
        for a,b in [('frame','header'),('frame','sidebar'),('frame','panel'),('header','sidebar'),('sidebar','panel')]:self.relate('connect',a,b)
