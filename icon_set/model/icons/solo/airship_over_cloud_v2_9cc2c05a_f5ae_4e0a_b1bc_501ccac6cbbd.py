"""A tapered airship with tail fin and attached gondola above a cloud. Keep a flat underside for an exact physical gondola join.
References: Lucide cloud: broad lobes; supplied airship silhouette.
Authored directly on SOLO48; original retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9cc2c05a-f5ae-4e0a-b1bc-501ccac6cbbd'
SOURCE_PATH = 'pictographic-primitives/transportation/hotair balloon_9cc2c05a-f5ae-4e0a-b1bc-501ccac6cbbd.svg'
AUTHOR = 'gpt-6'

class AirshipOverCloudVariant2(Solo48):
    icon_id = 'airship-over-cloud-v2'
    variant_of = 'airship-over-cloud'
    variant_label = 'Reconstructed solo drawing after rejection'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('airship', 'over', 'cloud')

    def build(self):
        # Symbol plan: A tapered airship with tail fin and attached gondola above a cloud. Keep a flat underside for an exact physical gondola join.

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
        path('airship',(12,8),[('L',(32,8)),('A',(32,18),12,5,True),('L',(12,18)),('L',(12,8))],True)
        poly('tail',(12,8),(4,8),(8,13),(4,18),(12,18));join('tail','airship')
        poly('gondola',(20,18),(22,26),(30,26),(32,18));join('gondola','airship')
        path('cloud',(12,40),[('A',(20,35),8,5,True),('A',(28,40),8,5,True),('L',(12,40))],True)
