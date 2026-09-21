# Final repair: Narrow the band perspective to reserve8 centerline units before pendant.
'Wide Choker with Round Pendant\nPlan: Perspective choker ellipse; connected pendant below with centerline attachment.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: Drop band thickness; preserve perspective loop and suspended circular pendant.\nKeyshape: HRECT_L; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '79bd7e9d-6e3c-4efa-bd6c-23024b1cfad9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_11/choker_79bd7e9d-6e3c-4efa-bd6c-23024b1cfad9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'wide-choker-with-round-pendant'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    keywords = ('wide', 'choker', 'with', 'round', 'pendant')

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

        ellipse('band',24,16,20,8)
        circle('pendant',24,36,4)
        self.add_line('link',(24,24),(24,32))
        self.relate('connect','link','band');self.relate('connect','link','pendant')
