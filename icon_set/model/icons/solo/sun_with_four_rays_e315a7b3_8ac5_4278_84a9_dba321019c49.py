'Sun with Four Rays\nPlan: Circle with four equal cardinal rays; shared center and ray lengths.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: Four cardinal rays retained; central disk reduced to preserve curved clearance.\nKeyshape: CIRCLE; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e315a7b3-8ac5-4278-84a9-dba321019c49'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_07/blue_e315a7b3-8ac5-4278-84a9-dba321019c49.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'sun-with-four-rays'
    keyshape = Keyshape.CIRCLE
    category = "primitives-generate"
    keywords = ('sun', 'with', 'four', 'rays')

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

        circle('sun',24,24,7)
        for name,a,b in [('top',(24,4),(24,8)),('bottom',(24,40),(24,44)),('left',(4,24),(8,24)),('right',(40,24),(44,24))]: self.add_line(name,a,b)
