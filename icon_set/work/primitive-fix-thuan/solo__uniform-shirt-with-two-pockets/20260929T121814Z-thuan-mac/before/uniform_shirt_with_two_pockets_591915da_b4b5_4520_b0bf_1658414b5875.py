'Uniform Shirt with Pockets.\nPlan: Mirrored uniform shirt, open collar and two flap-shaped pockets. Exact4,8..44,40 envelope.\nConstruction reference: Lucide shirt rounded shoulders and mirrored structure; source collar and paired pointed pocket bottoms.\nReduction: Omit placket and tiny flap seams to preserve two open pockets with full clearance.\nKeyshape: HRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '591915da-b4b5-4520-b0bf-1658414b5875'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_18/fatigues_591915da-b4b5-4520-b0bf-1658414b5875.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'uniform-shirt-with-two-pockets'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('uniform', 'shirt', 'with', 'two', 'pockets')

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

        self.add_bezier('shoulder-left',(16,8),((8,8),(4,12),(4,20)))
        self.add_polyline('body',(4,20),(4,40),(44,40),(44,20))
        self.add_bezier('shoulder-right',(44,20),((44,12),(40,8),(32,8)))
        self.add_line('neck',(32,8),(16,8))
        self.relate('connect','shoulder-left','body');self.relate('connect','shoulder-right','body');self.relate('connect','neck','shoulder-left');self.relate('connect','neck','shoulder-right')
        self.add_polyline('collar',(16,8),(24,16),(32,8));self.relate('connect','neck','collar')
        for x in (16,32):self.add_polyline(f'pocket-{x}',(x-3,26),(x,30),(x+3,26))
