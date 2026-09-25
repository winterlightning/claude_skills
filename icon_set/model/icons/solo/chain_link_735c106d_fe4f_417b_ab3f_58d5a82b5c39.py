'Two Interlocked Chain Links.\nPlan: Two open diagonal links with rounded outer ends and a central connector.\nConstruction reference: Lucide link: opposing open contours expose the central interlock.\nReduction: Small closed connector reduced to a stroke.\nKeyshape: SQUARE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '735c106d-fe4f-417b-ab3f-58d5a82b5c39'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_25/link slash_735c106d-fe4f-417b-ab3f-58d5a82b5c39.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'chain-link'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('chain', 'link')

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

        path('lower',(14,22),[(6,30),(6,34),((14,42),8,8,False),(18,42),(26,34)])
        path('upper',(22,14),[(30,6),(34,6),((42,14),8,8,True),(42,18),(34,26)])
        self.add_line('connector',(18,30),(30,18))
