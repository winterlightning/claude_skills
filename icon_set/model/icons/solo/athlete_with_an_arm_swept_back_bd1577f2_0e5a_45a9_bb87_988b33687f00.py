'Athlete with an Arm Swept Back\nPlan: Thrower leans right with long swept-back arm; round head on torso continuation and braced legs.\nReference: Human full_body_ref.png: round detached head, coherent torso and limbs.\nReduction: Use stroke limbs in place of thick outlined limbs; preserve throwing pose. Exact head-to-neck centerline gap sqrt(5²+12²)-5=8.\nKeyshape: SQUARE; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bd1577f2-0e5a-45a9-bb87-988b33687f00'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_04/athletics discus throwing_bd1577f2-0e5a-45a9-bb87-988b33687f00.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'athlete-with-an-arm-swept-back'
    keyshape = Keyshape.SQUARE
    category = "objects"
    keywords = ('athlete', 'with', 'an', 'arm', 'swept', 'back')

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

        circle('head',34,11,5)
        self.add_line('torso',(29,23),(24,35))
        self.add_polyline('back-arm',(29,23),(14,17),(6,19))
        self.add_polyline('front-arm',(29,23),(42,29),(39,35))
        self.add_polyline('left-leg',(24,35),(20,42),(14,42))
        self.add_polyline('right-leg',(24,35),(32,36),(34,42))
        for part in ['back-arm','front-arm','left-leg','right-leg']:self.relate('connect','torso',part)
        self.relate('connect','back-arm','front-arm');self.relate('connect','left-leg','right-leg')
        self.mark_human_figure('athlete',head='head',torso='torso',torso_junction='start')
