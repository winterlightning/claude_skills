'Unhappy Person Profile.\nPlan: Circular face center24,16 radius12. Shoulder top32 gives exact four-centerline/zero-ink gap. Broad rounded shoulders reach8,44 and40,44. Small downturned mouth.\nConstruction reference: human_ref/user.svg circular head and broad rounded shoulders; current touching-ink avatar rule.\nReduction: Keep the defining silhouette and essential parts.\nKeyshape: VRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '70365203-077b-47c0-bb1e-f6bb8b4c8754'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_30/patient_70365203-077b-47c0-bb1e-f6bb8b4c8754.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'unhappy-person-profile'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'avatars'
    aliases = ()
    keywords = ('unhappy', 'person', 'profile')

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
        path('mouth',(21,18),[((27,18),3,2,True)])
        self.add_arc('body-left-shoulder',(8,44),(20,32),radius_x=12)
        self.add_line('body-top',(20,32),(28,32))
        self.add_arc('body-right-shoulder',(28,32),(40,44),radius_x=12)
        self.add_contour('body','body-left-shoulder','body-top','body-right-shoulder')
        self.relate('connect','head','body')
