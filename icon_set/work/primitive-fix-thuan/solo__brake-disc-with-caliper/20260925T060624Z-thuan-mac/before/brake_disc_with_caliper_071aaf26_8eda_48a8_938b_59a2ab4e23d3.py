'Brake Disc with Caliper\nPlan: Brake rotor with center bore and upper-left quarter caliper.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: Remove intermediate hub ring and bolt dots; keep rotor and broad quarter caliper.\nKeyshape: CIRCLE; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '071aaf26-8eda-48a8-938b-59a2ab4e23d3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_07/brake_071aaf26-8eda-48a8-938b-59a2ab4e23d3.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'brake-disc-with-caliper'
    keyshape = Keyshape.CIRCLE
    category = "objects"
    keywords = ('brake', 'disc', 'with', 'caliper')

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

        path('rotor',(24,4),[((44,24),20,20,True),((24,44),20,20,True),((4,24),20,20,True)])
        path('caliper',(4,24),[((24,4),20,20,True),(24,13),((13,24),11,11,False),(4,24)],True)
        self.relate('connect','rotor','caliper')
        circle('bore',26,26,3)
