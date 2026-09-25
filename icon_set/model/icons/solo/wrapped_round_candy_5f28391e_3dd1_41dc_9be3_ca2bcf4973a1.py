'Wrapped Piece of Candy.\nPlan: Round candy with flared wrappers joined on either side. Bounds4,10..44,38.\nConstruction reference: Lucide candy original/atomic-debug: coherent candy body with opposite twisted ends; source horizontal arrangement.\nReduction: Keep the defining silhouette and essential parts.\nKeyshape: HRECT_M; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5f28391e-3dd1-41dc-9be3-ca2bcf4973a1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_37/sweets_5f28391e-3dd1-41dc-9be3-ca2bcf4973a1.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'wrapped-round-candy'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('wrapped', 'round', 'candy')

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

        circle('candy',24,24,12)
        self.add_polyline('left-wrap',(12,18),(4,10),(4,38),(12,30));self.add_polyline('right-wrap',(36,18),(44,10),(44,38),(36,30))
        self.relate('connect','candy','left-wrap');self.relate('connect','candy','right-wrap')
