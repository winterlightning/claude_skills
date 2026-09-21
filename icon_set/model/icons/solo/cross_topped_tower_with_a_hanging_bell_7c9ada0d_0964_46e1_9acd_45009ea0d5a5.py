# Final repair: Use a smaller flared bell and flatter tower roof to preserve8+ spacing.
'Cross-Topped Tower with a Hanging Bell\nPlan: Cross above open gabled tower; hanging bell centered beneath roof.\nReference: Lucide church original and atomic-debug: gable outline and central details.\nReduction: Drop bell clapper and stem to retain open tower spacing.\nKeyshape: VRECT_L; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7c9ada0d-0964-46e1-9acd-45009ea0d5a5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_06/belfry_7c9ada0d-0964-46e1-9acd-45009ea0d5a5.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'cross-topped-tower-with-a-hanging-bell'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    keywords = ('cross', 'topped', 'tower', 'with', 'a', 'hanging', 'bell')

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
        def ellipse(name,x,y,rx,ry):
            path(name,(x-rx,y),[((x+rx,y),rx,ry,True),((x-rx,y),rx,ry,True)],True)
        def circle(name,x,y,r):
            ellipse(name,x,y,r,r)
        def box(name,l,t,r,b,rad=4):
            path(name,(l+rad,t),[(r-rad,t),((r,t+rad),rad,rad,True),(r,b-rad),((r-rad,b),rad,rad,True),(l+rad,b),((l,b-rad),rad,rad,True),(l,t+rad),((l+rad,t),rad,rad,True)],True)

        self.add_polyline('tower',(8,44),(8,20),(24,16),(40,20),(40,44),(8,44))
        self.add_line('cross-v',(24,4),(24,16));self.add_line('cross-h',(20,8),(28,8));self.relate('connect','cross-h','cross-v');self.relate('connect','cross-v','tower')
        path('bell',(18,35),[(20,29),((28,29),4,4,True),(30,35),(18,35)],True)
