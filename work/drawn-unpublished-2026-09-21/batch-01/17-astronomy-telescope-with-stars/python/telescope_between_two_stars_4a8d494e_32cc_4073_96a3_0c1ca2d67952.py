'Telescope Between Two Stars\nPlan: Tilted telescope on tripod between two stars; stars remain scene objects.\nReference: Lucide telescope: coherent barrel and shared tripod attachment.\nReduction: Four-point stars replace five-point stars; step in barrel omitted.\nKeyshape: SQUARE; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4a8d494e-32cc-4073-96a3-0c1ca2d67952'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_04/astronomy telescope stars_4a8d494e-32cc-4073-96a3-0c1ca2d67952.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'telescope-between-two-stars'
    keyshape = Keyshape.SQUARE
    category = "objects"
    keywords = ('telescope', 'between', 'two', 'stars')

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

        self.add_polyline('barrel',(15,20),(35,12),(42,28),(22,36),(15,20))
        self.add_polyline('eyepiece',(15,20),(6,24),(10,32),(19,28));self.relate('connect','barrel','eyepiece')
        self.add_polyline('tripod',(16,42),(26,34),(34,42));self.relate('connect','tripod','barrel')
        self.add_line('tripod-center',(26,34),(26,42));self.relate('connect','tripod-center','tripod');self.relate('connect','tripod-center','barrel')
        for k,(x,y) in enumerate([(10,10),(40,38)]):
            self.add_polyline(f'star-{k}',(x,y-4),(x+1,y-1),(x+4,y),(x+1,y+1),(x,y+4),(x-1,y+1),(x-4,y),(x-1,y-1),(x,y-4))
