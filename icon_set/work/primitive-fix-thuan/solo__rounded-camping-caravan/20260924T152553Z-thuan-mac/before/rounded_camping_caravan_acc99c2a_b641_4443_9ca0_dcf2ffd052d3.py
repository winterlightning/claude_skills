'Rounded Camping Caravan\nPlan: Rounded caravan body, single wheel, window and tall door; attached tow bar.\nReference: Lucide caravan: outline broken at wheel and right-hand tow bar.\nReduction: Window simplified to one line; door remains a tall opening.\nKeyshape: HRECT_L; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'acc99c2a-b641-4443-9ca0-dcf2ffd052d3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_10/caravan_acc99c2a-b641-4443-9ca0-dcf2ffd052d3.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'rounded-camping-caravan'
    keyshape = Keyshape.HRECT_L
    category = "objects"
    keywords = ('rounded', 'camping', 'caravan')

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

        path('body',(13,37),[(4,35),(4,18),((14,8),10,10,True),(30,8),((38,16),8,8,True),(38,35),(19,37)])
        circle('wheel',16,37,3);self.relate('connect','wheel','body')
        self.add_polyline('door',(27,35),(27,19),(38,19));self.relate('connect','door','body')
        self.add_line('window',(13,19),(18,19))
        self.add_polyline('tow',(38,35),(44,35));self.relate('connect','tow','body')
