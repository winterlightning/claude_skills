"""Four equal circular flower lobes, a centered ring and two symmetric ribbon tails. The flower owns equal lobe radii and exact repeated joins.
References: Lucide award: medal and paired ribbon; source flower outline reduced to four equal lobes.
Authored directly on SOLO48; original retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '58f87e29-b0b5-42be-b412-f3b9d5882e0e'
SOURCE_PATH = 'pictographic-primitives/symbol/award flower shape_58f87e29-b0b5-42be-b412-f3b9d5882e0e.svg'
AUTHOR = 'gpt-6'

class AwardFlowerRosetteVariant2(Solo48):
    icon_id = 'award-flower-rosette-v2'
    variant_of = 'award-flower-rosette'
    variant_label = 'Reconstructed solo drawing after rejection'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('award', 'flower', 'rosette')

    def build(self):
        # Symbol plan: Four equal circular flower lobes, a centered ring and two symmetric ribbon tails. The flower owns equal lobe radii and exact repeated joins.

        def path(n, start, commands, closed=False):
            here=start; members=[]
            for j,c in enumerate(commands):
                kind,end,*args=c; ident=f'{n}-{j}'
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
        path('flower',(16,12),[('A',(32,12),8,8,True),('A',(32,28),8,8,True),('A',(16,28),8,8,True),('A',(16,12),8,8,True)],True)
        circle('center',24,20,3)
        poly('ribbon',(16,28),(12,44),(24,38),(36,44),(32,28));join('flower','ribbon')
