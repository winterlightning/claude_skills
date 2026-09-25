'Car on Inclined Ramp\nPlan: Car on diagonal slope; two equal wheels and broad cabin above sloped sill.\nReference: Lucide car: matched wheels and body broken around the wheel contacts.\nReduction: Omit window division; preserve inclined car and ramp direction.\nKeyshape: SQUARE; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '400b299b-3d6d-4ea5-900a-c45553cdafda'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_09/car descending control_400b299b-3d6d-4ea5-900a-c45553cdafda.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'car-on-inclined-ramp'
    keyshape = Keyshape.SQUARE
    category = "primitives-generate"
    keywords = ('car', 'on', 'inclined', 'ramp')

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

        self.add_line('ramp',(6,42),(42,34))
        self.add_polyline('body',(6,17),(13,9),(24,6),(31,11),(40,11))
        circle('rear-wheel',13,28,3);circle('front-wheel',33,23,3)
        self.add_line('sill',(16,28),(30,23))
        for wheel in ['rear-wheel','front-wheel']:self.relate('connect',wheel,'sill')
