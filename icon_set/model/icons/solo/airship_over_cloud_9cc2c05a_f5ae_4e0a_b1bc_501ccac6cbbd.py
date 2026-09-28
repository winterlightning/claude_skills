"""An elongated airship with a tail fin and a clear gondola above a compact lobed cloud. The staggered sky scene gives both subjects room at 48 pixels.
References: Lucide cloud original and atomic-debug; supplied airship/gondola scene.
Authored directly on SOLO48; original retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9cc2c05a-f5ae-4e0a-b1bc-501ccac6cbbd'
SOURCE_PATH = 'pictographic-primitives/transportation/hotair balloon_9cc2c05a-f5ae-4e0a-b1bc-501ccac6cbbd.svg'
AUTHOR = 'gpt-6'

class AirshipOverCloud(Solo48):
    icon_id = 'airship-over-cloud'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    categories = ('transportation', 'primitives')
    aliases = ()
    keywords = ('airship', 'over', 'cloud')

    def build(self):
        # Symbol plan: An elongated airship with a tail fin and a clear gondola above a compact lobed cloud. The staggered sky scene gives both subjects room at 48 pixels.

        def path(n, start, commands, closed=False):
            here=start; members=[]
            for j,c in enumerate(commands):
                kind,end,*args=c; ident=('body-top' if j==2 else 'body-top-right') if n=='body' and j in (2,3) else f'{n}-{j}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                members.append(ident);here=end
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y), [('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def box(n,l,t,r,b,rad=3):
            path(n,(l+rad,t), [('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line=self.add_line;poly=self.add_polyline;dot=self.add_dot
        join=lambda a,b:self.relate('connect',a,b)
        path('airship',(12,8),[('L',(36,8)),('A',(36,20),8,6,True),('L',(12,20)),('L',(12,8))],True)
        poly('tail',(4,8),(12,14),(4,20));join('tail','airship')
        poly('gondola',(28,20),(28,28),(36,28),(36,20));join('gondola','airship')
        path('cloud',(8,32),[('A',(4,36),4,4,False),('A',(8,40),4,4,False),('L',(16,40)),('A',(20,36),4,4,False),('C',(8,32),(20,28),(10,28))],True)
