'Interlocking Handshake\nPlan: Two opposed wrists and clasping hands; one diagonal grip line instead of tiny fingers.\nReference: Lucide handshake: opposed cuffs and diagonal interlocking grip.\nReduction: Reduced finger divisions to one; shared human reference inspected, no detached head applies.\nKeyshape: SQUARE; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e18ed81a-df3e-442f-9876-54ac0d744866'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_11/clasp_e18ed81a-df3e-442f-9876-54ac0d744866.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'interlocking-handshake'
    keyshape = Keyshape.SQUARE
    category = "objects"
    keywords = ('interlocking', 'handshake')

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

        self.add_polyline('left-arm',(6,20),(18,6),(27,10))
        self.add_bezier('grip',(27,10),((28,6),(32,6),(35,9)),((39,13),(42,17),(42,20)),((42,22),(40,24),(38,26)))
        self.relate('connect','grip','left-arm')
        self.add_polyline('grip-inner',(27,10),(18,18),(24,24),(30,18),(42,30),(30,42),(6,20))
        self.relate('connect','grip-inner','left-arm');self.relate('connect','grip-inner','grip')
        
