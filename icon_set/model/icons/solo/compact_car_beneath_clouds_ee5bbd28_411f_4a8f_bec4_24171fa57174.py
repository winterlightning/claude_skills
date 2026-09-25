'Compact Car beneath Clouds\nPlan: Compact car under two clouds; shared car wheels and compact weather puffs.\nReference: Lucide car: equal wheels and uninterrupted roof silhouette.\nReduction: Clouds simplified to dome outlines; exhaust dot omitted.\nKeyshape: SQUARE; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ee5bbd28-411f-4a8f-bec4-24171fa57174'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_09/car clouds_ee5bbd28-411f-4a8f-bec4-24171fa57174.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'compact-car-beneath-clouds'
    keyshape = Keyshape.SQUARE
    category = "primitives-generate"
    keywords = ('compact', 'car', 'beneath', 'clouds')

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

        self.add_polyline('body',(6,23),(13,23),(24,23),(33,23),(42,23))
        circle('rear-wheel',14,37,5);circle('front-wheel',34,37,5)
        self.add_line('sill',(19,37),(29,37))
        for wheel in ['rear-wheel','front-wheel']:self.relate('connect',wheel,'sill')

        path('cloud',(12,14),[((20,6),8,8,True),((28,14),8,8,True),(35,14)])
