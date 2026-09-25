'Three Horizontal Row Layout.\nPlan: One rounded frame partitioned into three equal horizontal rows.\nConstruction reference: Lucide table: repeated structural separators.\nReduction: No omissions.\nKeyshape: SQUARE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6cd1da2f-b4eb-4479-b78e-8c2fcaecc164'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_25/layout three columns 1_6cd1da2f-b4eb-4479-b78e-8c2fcaecc164.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'layout-three-rows'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'design'
    categories = ('design', 'primitive', 'primitives')
    aliases = ()
    keywords = ('layout', 'three', 'rows')

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
        for y in (18,30):self.add_line(f'row-{y}',(6,y),(42,y));self.relate('connect',f'row-{y}','frame')
