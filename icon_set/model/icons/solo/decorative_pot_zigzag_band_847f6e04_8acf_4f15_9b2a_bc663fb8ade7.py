'Traditional Decorative Earthen Pot.\nPlan: Lidded earthen pot with broad belly and zigzag decoration.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Extra neck tiers and parallel band omitted; lid and zigzag belly band retained.\nKeyshape: VRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '847f6e04-8acf-4f15-9b2a-bc663fb8ade7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_01/akshaya tritiya 2_847f6e04-8acf-4f15-9b2a-bc663fb8ade7.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'decorative-pot-zigzag-band'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('decorative', 'pot', 'zigzag', 'band')

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

        path('pot',(16,14),[(32,14),((40,30),8,16,True),((32,44),8,14,True),(16,44),((8,30),8,14,True),((16,14),8,16,True)],True)
        path('lid',(16,14),[(16,8),((20,4),4,4,True),(28,4),((32,8),4,4,True),(32,14)]);self.relate('connect','lid','pot')
        self.add_polyline('zigzag',(8,30),(16,24),(24,30),(32,24),(40,30));self.relate('connect','zigzag','pot')
