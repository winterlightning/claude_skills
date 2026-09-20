'Hormonal Intrauterine Device.\nPlan: Open-ended T arms meet a narrow central IUD body; trailing string ends in a small loop.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Short inward extensions of the arms omitted; arm interiors remain open as in the original.\nKeyshape: VRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '069fa03e-6e47-43fe-b60e-0057a83a2627'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_22/hormonal iud_069fa03e-6e47-43fe-b60e-0057a83a2627.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 't-shaped-intrauterine-device'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('t', 'shaped', 'intrauterine', 'device')

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

        path('left-arm',(12,12),[((12,4),4,4,True),(16,4),((24,16),8,12,True)])
        path('right-arm',(36,12),[((36,4),4,4,False),(32,4),((24,16),8,12,False)])
        box('body',20,16,28,34,4)
        self.relate('connect','left-arm','right-arm');self.relate('connect','body','left-arm');self.relate('connect','body','right-arm')
        self.add_line('string',(24,34),(24,38));self.relate('connect','body','string')
        circle('end-loop',24,41,3);self.relate('connect','string','end-loop')
