"""Child cycle with two full wheels, a rounded high-back seat, connecting frame and small front basket below a raised handlebar.
Keyshape SQUARE: exact SOLO48 contract envelope.
Construction: bike: paired full circular wheels; source governs child seat and basket
Omissions: Wheel hubs omitted.
Feedback: Bad stroke drawn. Fresh reference-based revision."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='5ff4ebdd-5754-482c-9fb2-040f1c9eaa90'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/kids/tricycle_5ff4ebdd-5754-482c-9fb2-040f1c9eaa90.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='child-cycle-with-front-basket-solo-b016'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'kids'
    aliases=()
    keywords=('child', 'cycle', 'with', 'front', 'basket', 'solo', 'b016')
    def build(self):

        def path(name, start, steps, closed=False):
            members=[]; here=start
            for i,step in enumerate(steps):
                tag=f'{name}-{i}'; kind,end,*args=step
                if kind=='L': self.add_line(tag,here,end)
                elif kind=='A': self.add_arc(tag,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(tag,here,(args[0],args[1],end))
                here=end;members.append(tag)
            self.add_contour(name,*members,closed=closed)
        def ellipse(name,x,y,rx,ry):
            path(name,(x-rx,y),[('A',(x+rx,y),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
        def box(name,l,t,r,b,rad):
            path(name,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        for name,x in [('rear',13),('front',35)]:ellipse(name,x,35,7,7)
        path('seat',(8,28),[('L',(8,10)),('A',(12,6),4,4,True),('A',(16,10),4,4,True),('L',(16,20)),('L',(21,20)),('A',(24,23),3,3,True),('L',(24,25)),('A',(21,28),3,3,True),('L',(8,28))],True);join('seat','rear')
        poly('frame',(24,25),(34,24),(35,28));join('frame','seat');join('frame','front')
        poly('handlebar',(28,6),(34,6),(34,24));join('handlebar','frame')
        poly('basket',(34,14),(42,14),(40,22),(34,22));join('basket','handlebar')
