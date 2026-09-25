'Arch Tunnel Entrance.\nPlan: Concentric arch crowns with 10u radius difference; joined baseline at both inner piers.\nConstruction reference: Lucide church: arch crown and straight jambs; source nested tunnel geometry retained.\nReduction: Keep the defining silhouette and essential parts.\nKeyshape: SQUARE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0fae8c9d-7bdc-44a7-99d9-77bffd1e5ec2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_38/tunnel_0fae8c9d-7bdc-44a7-99d9-77bffd1e5ec2.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'arched-tunnel-entrance'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('arched', 'tunnel', 'entrance')

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

        path('outer',(6,42),[(6,24),((42,24),18,18,True),(42,42),(32,42),(16,42),(6,42)],True)
        path('opening',(16,42),[(16,24),((32,24),8,8,True),(32,42)])
        self.relate('connect','outer','opening')
