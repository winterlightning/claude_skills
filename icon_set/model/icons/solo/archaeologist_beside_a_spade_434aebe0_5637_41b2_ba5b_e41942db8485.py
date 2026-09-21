'Archaeologist Beside a Spade\nPlan: Hat-wearing circular face with smooth shoulders beside an upright spade.\nReference: Human user.svg: circular face with curved shoulders; supplied brimmed hat and spade.\nReduction: Drop sleeve lines and spade lower handle outline.\nKeyshape: SQUARE; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '434aebe0-5637-41b2-ba5b-e41942db8485'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_04/archaeologist_434aebe0-5637-41b2-ba5b-e41942db8485.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'archaeologist-beside-a-spade'
    keyshape = Keyshape.SQUARE
    human_construction = "bust"
    category = "objects"
    keywords = ('archaeologist', 'beside', 'a', 'spade')

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

        path('hat',(10,16),[((26,16),8,10,True)])
        self.add_line('brim',(6,16),(27,16));self.relate('connect','hat','brim')
        self.add_arc('jaw',(10,16),(26,16),radius_x=8,sweep=False);self.relate('connect','jaw','brim');self.relate('connect','jaw','hat')
        self.add_bezier('shoulders',(6,42),((6,34),(10,28),(18,28)),((22,28),(25,31),(27,36)))
        self.relate('connect','jaw','shoulders')
        self.add_polyline('spade',(34,28),(34,20),(38,16),(42,20),(42,28),(34,28))
        self.add_line('shaft',(38,28),(38,42));self.relate('connect','shaft','spade')
