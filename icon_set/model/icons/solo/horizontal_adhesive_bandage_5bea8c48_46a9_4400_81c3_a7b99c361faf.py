'Adhesive Bandage Strip.\nPlan: One rounded horizontal strip with shared pad divider nodes at x16 and32.\nConstruction reference: Lucide bandage: rounded strip with two structural pad dividers.\nReduction: Divider curves straightened for a clean geometric pad.\nKeyshape: HRECT_M; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5bea8c48-46a9-4400-81c3-a7b99c361faf'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_18/fascia_5bea8c48-46a9-4400-81c3-a7b99c361faf.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'horizontal-adhesive-bandage'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('horizontal', 'adhesive', 'bandage')

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

        path('strip',(16,10),[(32,10),((44,22),12,12,True),(44,26),((32,38),12,12,True),(16,38),((4,26),12,12,True),(4,22),((16,10),12,12,True)],True)
        for x in (16,32):
         self.add_line(f'pad-{x}',(x,10),(x,38));self.relate('connect','strip',f'pad-{x}')
