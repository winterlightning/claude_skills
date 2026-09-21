'Overhead Car with Sensor Waves\nPlan: Overhead car with two windows and paired side sensing arcs.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: Windows reduced to short central marks; single sensing arc per side.\nKeyshape: SQUARE; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '470a18bd-b01c-429e-96d1-77178c4d935a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_09/car sensor 1_470a18bd-b01c-429e-96d1-77178c4d935a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'overhead-car-with-sensor-waves'
    keyshape = Keyshape.SQUARE
    category = "objects"
    keywords = ('overhead', 'car', 'with', 'sensor', 'waves')

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

        box('car',16,6,32,42,7)
        self.add_line('window-top',(16,17),(32,17));self.add_line('window-bottom',(16,31),(32,31))
        self.relate('connect','window-top','car');self.relate('connect','window-bottom','car')
        self.add_arc('wave-left',(7,16),(7,32),radius_x=1,radius_y=8,sweep=False)
        self.add_arc('wave-right',(41,16),(41,32),radius_x=1,radius_y=8,sweep=True)
