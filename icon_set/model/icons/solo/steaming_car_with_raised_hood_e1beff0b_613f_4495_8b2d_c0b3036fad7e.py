'Steaming Car with Raised Hood\nPlan: Car body with open raised hood, equal wheels and one rising steam stroke.\nReference: Lucide car: broken sill at round wheels, continuous roof/body contour.\nReduction: Omit inset side window and second steam wisp to retain raised hood and steam.\nKeyshape: SQUARE; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e1beff0b-613f-4495-8b2d-c0b3036fad7e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_09/car repair engine_e1beff0b-613f-4495-8b2d-c0b3036fad7e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'steaming-car-with-raised-hood'
    keyshape = Keyshape.SQUARE
    category = "objects"
    keywords = ('steaming', 'car', 'with', 'raised', 'hood')

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

        self.add_polyline('body',(6,23),(13,18),(24,18),(33,23),(42,23))
        circle('rear-wheel',14,37,5);circle('front-wheel',34,37,5)
        self.add_line('sill',(19,37),(29,37))
        for wheel in ['rear-wheel','front-wheel']: self.relate('connect',wheel,'sill')
        self.add_line('hood',(33,23),(41,20));self.relate('connect','hood','body')
        self.add_bezier('steam',(34,14),((38,11),(32,9),(36,6)))
