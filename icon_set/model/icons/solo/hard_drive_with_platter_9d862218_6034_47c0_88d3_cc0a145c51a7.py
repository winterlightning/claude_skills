'Hard Disk Storage Drive.\nPlan: Rounded drive case, large round platter and lower band. Single platter circle without tiny hub.\nConstruction reference: Lucide hard-drive: rounded case and transverse lower band; source circular platter retained.\nReduction: Tiny hub and indicator omitted to keep the platter separated from its case.\nKeyshape: VRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9d862218-6034-47c0-88d3-cc0a145c51a7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_22/hard drive_9d862218-6034-47c0-88d3-cc0a145c51a7.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hard-drive-with-platter'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('hard', 'drive', 'with', 'platter')

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

        path('case',(12,4),[(36,4),((40,8),4,4,True),(40,34),(40,40),((36,44),4,4,True),(12,44),((8,40),4,4,True),(8,34),(8,8),((12,4),4,4,True)],True)
        circle('platter',24,20,6)
        self.add_line('band',(8,34),(40,34));self.relate('connect','band','case')
