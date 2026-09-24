'Winged Monument on a Pedestal\nPlan: Statue head over curved body, one upright wing and rectangular pedestal. Detached head uses an eight-unit centerline gap.\nReference: Human full_body_ref: round detached head; supplied wing and pedestal silhouette.\nReduction: Omit wing inner accent and doubled pedestal band.\nKeyshape: VRECT_L; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b8975bc1-4fe4-47c7-82bd-a46a322d6fc6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_03/angel of independence mexico_b8975bc1-4fe4-47c7-82bd-a46a322d6fc6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'winged-monument-on-a-pedestal'
    keyshape = Keyshape.VRECT_L
    category = "objects"
    keywords = ('winged', 'monument', 'on', 'a', 'pedestal')

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

        circle('head',16,9,5)
        path('body',(8,34),[(8,28),((14,22),6,6,True),(20,22),(20,34)])
        self.add_bezier('wing',(20,22),((32,22),(28,4),(40,4)),((40,15),(34,20),(28,22)))
        self.relate('connect','body','wing')
        self.add_polyline('pedestal',(8,34),(30,34),(30,44),(8,44),(8,34));self.relate('connect','body','pedestal')
