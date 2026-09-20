'Water Hovercraft Transport Vehicle.\nPlan: Hovercraft skirt below a low cabin and curved aft fan guard. Bounds4,10..44,38.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Reduce cabin glazing and second hull seam; preserve skirt, central cabin and aft fan housing.\nKeyshape: HRECT_M; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2f516480-e830-48c3-85e6-fd2de22b8bc1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_23/hovercraft_2f516480-e830-48c3-85e6-fd2de22b8bc1.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hovercraft'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('hovercraft',)

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

        path('hull',(4,28),[(44,28),((34,38),10,10,True),(14,38),((4,28),10,10,True)],True)
        path('cabin',(8,28),[(12,16),((18,10),6,6,True),(24,10),((28,14),4,4,True),(28,28)]);self.relate('connect','hull','cabin')
        path('fan',(36,28),[(36,20),((44,12),8,8,True),(44,28)]);self.relate('connect','fan','hull')
