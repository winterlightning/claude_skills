'Car Viewed from the Rear\nPlan: Rear-view car with broad body, sloping rear window and paired tires.\nReference: Lucide car: simplified continuous body and equal wheels.\nReduction: Rear light curls omitted; wide rear window and tires retained.\nKeyshape: HRECT_L; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2ae26408-156c-43de-9e16-97f3b148035f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_32/rear_2ae26408-156c-43de-9e16-97f3b148035f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'car-viewed-from-the-rear'
    keyshape = Keyshape.HRECT_L
    category = "objects"
    keywords = ('car', 'viewed', 'from', 'the', 'rear')

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

        path('body',(4,22),[(10,8),(38,8),(44,22),(44,32),(4,32),(4,22)],True)
        self.add_line('window',(4,22),(44,22));self.relate('connect','window','body')
        for i,x in enumerate([12,36]):self.add_line(f'tire-{i}',(x,32),(x,40));self.relate('connect',f'tire-{i}','body')
