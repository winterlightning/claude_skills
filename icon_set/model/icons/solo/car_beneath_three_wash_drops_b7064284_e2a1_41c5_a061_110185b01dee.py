'Car beneath Three Wash Drops\nPlan: Side-view car under overhead spray source; two water drops.\nReference: Lucide car: round wheels and roof silhouette.\nReduction: Two water marks replace three teardrops; overhead bar retained.\nKeyshape: SQUARE; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b7064284-e2a1-41c5-a061-110185b01dee'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_10/car wash_b7064284-e2a1-41c5-a061-110185b01dee.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'car-beneath-three-wash-drops'
    keyshape = Keyshape.SQUARE
    category = "objects"
    keywords = ('car', 'beneath', 'three', 'wash', 'drops')

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
        for wheel in ['rear-wheel','front-wheel']:self.relate('connect',wheel,'sill')

        self.add_line('sprayer',(16,6),(32,6));self.add_line('feed',(21,6),(21,6));self.relate('connect','feed','sprayer')
        self.add_dot('drop-left',(6,12));self.add_dot('drop-right',(40,12))
