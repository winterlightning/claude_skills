# Final repair: Reduce cap/loop to a simple suspension stem to remove narrow internal channel.
'Round Hanging Bauble\nPlan: Round bauble below single rounded hanging cap; shared vertical axis.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: Combine cap and loop into one hanger; preserve round ornament.\nKeyshape: VRECT_L; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '13e6b40e-9c4d-4e82-bb53-695d9e065fca'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_29/ornament_13e6b40e-9c4d-4e82-bb53-695d9e065fca.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'round-hanging-bauble'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    keywords = ('round', 'hanging', 'bauble')

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

        circle('ball',24,28,16)
        self.add_line('hanger',(24,4),(24,12));self.relate('connect','hanger','ball')
