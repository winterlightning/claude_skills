"""One exact radius-20 circular rim. Six blades share opposed integer geometry; all diagonal runs have slope 2, without kinks at former inner vertices.
References: Lucide aperture original and atomic-debug: exact circular rim and repeated blades.
Authored directly on SOLO48; original retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0cb953cf-9714-40a8-af67-7ea79c576259'
SOURCE_PATH = 'pictographic-primitives/symbol/lens shutter_0cb953cf-9714-40a8-af67-7ea79c576259.svg'
AUTHOR = 'gpt-6'

class ApertureShutterVariant2(Solo48):
    icon_id = 'aperture-shutter-v2'
    variant_of = 'aperture-shutter'
    variant_label = 'Reconstructed solo drawing after rejection'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('aperture', 'shutter')

    def build(self):
        # Symbol plan: One exact radius-20 circular rim. Six blades share opposed integer geometry; all diagonal runs have slope 2, without kinks at former inner vertices.

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
        rim=[(40,12),(40,36),(24,44),(8,36),(8,12),(24,4)]
        for j in range(6):self.add_arc(f'rim-{j}',rim[j],rim[(j+1)%6],radius_x=20)
        self.add_contour('rim',*(f'rim-{j}' for j in range(6)),closed=True)
        blades=[[(40,12),(28,12),(20,12)],[(40,36),(34,24),(28,12)],[(24,44),(28,36),(34,24)],[(8,36),(20,36),(28,36)],[(8,12),(14,24),(20,36)],[(24,4),(20,12),(14,24)]]
        for j,p in enumerate(blades):poly(f'blade-{j}',*p);join('rim',f'blade-{j}')
        for j in range(6):join(f'blade-{j}',f'blade-{(j+1)%6}')
