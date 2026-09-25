'Front View Car with Sensor Waves\nPlan: Front car with sensing wave on each side, mirrored body and wheels.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: One arc per side replaces two; lamps removed from small car front.\nKeyshape: HRECT_L; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3c675853-e649-4029-b679-cef625fb977e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_09/car sensor 3_3c675853-e649-4029-b679-cef625fb977e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'front-view-car-with-sensor-waves'
    keyshape = Keyshape.HRECT_L
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    keywords = ('front', 'view', 'car', 'with', 'sensor', 'waves')

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

        self.add_polyline('roof',(14,20),(18,8),(30,8),(34,20))
        box('body',14,20,34,32,3);self.relate('connect','roof','body')
        for i,x in enumerate([18,30]):
         self.add_line(f'wheel-{i}',(x,32),(x,40));self.relate('connect',f'wheel-{i}','body')
        self.add_arc('wave-left',(6,12),(6,32),radius_x=2,radius_y=10,sweep=False)
        self.add_arc('wave-right',(42,12),(42,32),radius_x=2,radius_y=10,sweep=True)
