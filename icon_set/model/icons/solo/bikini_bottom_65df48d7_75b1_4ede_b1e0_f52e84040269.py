'Women Bikini Bottom Underwear.\nPlan: Broad bikini waistband and high inward-curving leg cutouts. Bounds4,8..44,40.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Omit extra waistband seam; preserve high-cut silhouette.\nKeyshape: HRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '65df48d7-75b1-4ede-b1e0-f52e84040269'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_37/thong_65df48d7-75b1-4ede-b1e0-f52e84040269.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'bikini-bottom'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('bikini', 'bottom')

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

        self.add_line('waist',(4,8),(44,8))
        self.add_bezier('right',(44,8),((44,20),(28,20),(28,40)))
        self.add_line('crotch',(28,40),(20,40))
        self.add_bezier('left',(20,40),((20,20),(4,20),(4,8)))
        self.add_contour('briefs','waist','right','crotch','left',closed=True)
