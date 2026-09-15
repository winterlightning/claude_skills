"""A recognizable horizontal rifle with a long muzzle, rear stock, magazine and grip. Reduce mechanical detail to preserve silhouette.
References: Supplied original; shared geometric construction principles.
Authored directly on SOLO48; original retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '835277d4-590e-5008-a9cb-07213ea668e9'
SOURCE_PATH = 'pictographic-primitives/war/modern weapon machine gun_835277d4-590e-5008-a9cb-07213ea668e9.svg'
AUTHOR = 'gpt-6'

class AutomaticRifleVariant2(Solo48):
    icon_id = 'automatic-rifle-v2'
    variant_of = 'automatic-rifle'
    variant_label = 'Reconstructed solo drawing after rejection'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'war'
    aliases = ()
    keywords = ('automatic', 'rifle')

    def build(self):
        # Symbol plan: A recognizable horizontal rifle with a long muzzle, rear stock, magazine and grip. Reduce mechanical detail to preserve silhouette.

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
        poly('rifle',(4,22),(12,22),(18,16),(32,16),(32,24),(44,24),(44,32),(32,32),(34,40),(24,40),(22,32),(16,32),(8,38),(4,38),closed=True)
        line('sight',(32,16),(32,8));join('rifle','sight')
