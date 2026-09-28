'Highway Road with Overpass Bridge.\nPlan: Tapering road, two center-line marks and a full-width crossing line; shared crossing nodes.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: No omissions; crossing is structural road geometry.\nKeyshape: HRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bbb084a1-c5b7-4bf6-9ed6-818fa033b0bb'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_22/highway_bbb084a1-c5b7-4bf6-9ed6-818fa033b0bb.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'road-crossing-horizontal-line'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('road', 'crossing', 'horizontal', 'line')

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

        self.add_polyline('left-road',(8,40),(13,24),(14,8))
        self.add_polyline('right-road',(40,40),(35,24),(34,8))
        self.add_polyline('crossing',(4,24),(13,24),(35,24),(44,24))
        self.relate('connect','crossing','left-road');self.relate('connect','crossing','right-road')
        self.add_line('mark-top',(24,8),(24,15));self.add_line('mark-bottom',(24,33),(24,40))
