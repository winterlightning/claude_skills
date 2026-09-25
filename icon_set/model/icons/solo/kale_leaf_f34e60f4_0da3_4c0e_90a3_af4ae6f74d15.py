'Wavy Kale Leaf.\nPlan: Scalloped kale leaf with diagonal stem and broad lobes. Exact6..42.\nConstruction reference: Lucide leaf coherent silhouette and attached midrib; source scalloped lobes retained.\nReduction: Omit tiny side veins.\nKeyshape: SQUARE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f34e60f4-0da3-4c0e-90a3-af4ae6f74d15'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_24/kale_f34e60f4-0da3-4c0e-90a3-af4ae6f74d15.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'kale-leaf'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('kale', 'leaf')

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

        self.add_bezier('edge',(10,38),((6,34),(6,30),(6,26)),((6,18),(12,20),(12,14)),((12,8),(20,12),(24,8)),((28,6),(32,6),(36,6)),((42,6),(42,12),(42,16)),((42,20),(38,22),(40,26)),((42,32),(34,34),(32,36)),((30,42),(18,40),(10,38)))
        self.add_line('stem',(6,42),(32,16));self.relate('connect','edge','stem')
