'Person Wearing Skullcap.\nPlan: Circular head with skullcap seam above broad curved shoulders. Face24,16 r12 bottom28; bodytop32 exact zero ink gap.\nConstruction reference: human_ref/user.svg circular head, curved shoulders and current touching ink rule; source cap seam.\nReduction: Keep the defining silhouette and essential parts.\nKeyshape: VRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9f65fdf9-6ec9-4955-abbe-bcde5675a5a5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/person_9f65fdf9-6ec9-4955-abbe-bcde5675a5a5.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'person-wearing-skullcap'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('person', 'wearing', 'skullcap')

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

        self.add_arc('head-top',(12,16),(36,16),radius_x=12)
        self.add_arc('head-bottom',(36,16),(12,16),radius_x=12)
        self.add_contour('head','head-top','head-bottom',closed=True)
        self.add_line('cap-seam',(12,16),(36,16));self.relate('connect','head','cap-seam')
        self.add_arc('body-left',(8,44),(20,32),radius_x=12)
        self.add_line('body-top',(20,32),(28,32))
        self.add_arc('body-right',(28,32),(40,44),radius_x=12)
        self.add_contour('body','body-left','body-top','body-right');self.relate('connect','head','body')
