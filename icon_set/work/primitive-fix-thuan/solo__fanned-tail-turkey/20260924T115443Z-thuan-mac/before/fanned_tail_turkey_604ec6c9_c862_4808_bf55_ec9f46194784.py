'Thanksgiving Turkey Bird.\nPlan: Right-facing turkey with scalloped tail fan, upright neck, rounded body and two legs.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Wattle and inner feather seams omitted; fan, beak, neck and two legs retained.\nKeyshape: HRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '604ec6c9-c862-4808-bf55-ec9f46194784'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_21/gobbler_604ec6c9-c862-4808-bf55-ec9f46194784.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'fanned-tail-turkey'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('fanned', 'tail', 'turkey')

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

        path('body',(16,30),[((22,18),6,12,True),(30,18),(30,12),((38,12),4,4,True),(44,18),(38,18),(38,28),((30,36),8,8,True),(22,36),(16,30)],True)
        path('tail',(16,30),[(10,30),((4,24),6,6,True),((8,16),4,8,True),(8,14),((14,8),6,6,True),(18,8),((22,12),4,4,True),(22,18)])
        self.relate('connect','body','tail')
        for x in (22,30):self.add_line(f'leg-{x}',(x,36),(x,40));self.relate('connect',f'leg-{x}','body')
