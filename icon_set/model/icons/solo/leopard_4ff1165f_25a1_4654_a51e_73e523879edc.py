'Wild Leopard Standing Profile.\nPlan: Unspotted right-facing cat with long back, muzzle and two visible legs. Exact4,10..44,38.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Omit absent spots; preserve long unmarked cat silhouette and two legs.\nKeyshape: HRECT_M; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4ff1165f-25a1-4654-a51e-73e523879edc'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_25/leopard 1_4ff1165f-25a1-4654-a51e-73e523879edc.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'leopard'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'Uncategorized'
    aliases = ()
    keywords = ('leopard',)

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

        path('cat',(4,22),[((12,14),8,8,True),(28,14),(34,10),(36,14),(44,16),(44,26),(36,26),(36,38),(26,38),(26,28),(14,28),(14,38),(4,38),(4,22)],True)
