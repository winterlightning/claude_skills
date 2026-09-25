'Car Bumper Emitting Three Sensor Arcs\nPlan: Cropped car front and wheel with three nested sensor arcs.\nReference: Lucide car: wheel and interrupted body line.\nReduction: Two arcs replace three; omit tiny bumper inset.\nKeyshape: HRECT_L; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7a744411-5fc5-4b46-a2ca-fabc0d60942f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_05/auto pilot car sound warning_7a744411-5fc5-4b46-a2ca-fabc0d60942f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'car-bumper-emitting-three-sensor-arcs'
    keyshape = Keyshape.HRECT_L
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    keywords = ('car', 'bumper', 'emitting', 'three', 'sensor', 'arcs')

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

        self.add_polyline('body',(25,21),(33,21),(39,8),(44,8))
        circle('wheel',35,35,5)
        self.add_line('sill',(40,35),(44,35));self.relate('connect','sill','wheel')
        self.add_arc('wave-outer',(10,8),(10,36),radius_x=6,radius_y=14,sweep=False)
        self.add_arc('wave-inner',(16,18),(16,28),radius_x=2,radius_y=5,sweep=False)
