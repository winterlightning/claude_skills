"""A center-parted bob frames a circular jaw. The crossed garment neckline keeps the supplied hanbok-style clothing readable.
References: Human user.svg and supplied hairstyle/crossover garment; no facial ethnicity inference.
Authored directly on SOLO48; original retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd16f1f81-7844-565c-b3b8-1b41d8de6f51'
SOURCE_PATH = 'pictographic-primitives/avatars/avatar korean woman_d16f1f81-7844-565c-b3b8-1b41d8de6f51.svg'
AUTHOR = 'gpt-6'

class AvatarKoreanWomanVariant2(Solo48):
    icon_id = 'avatar-korean-woman-v2'
    variant_of = 'avatar-korean-woman'
    variant_label = 'Reconstructed solo drawing after rejection'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('avatar', 'korean', 'woman')

    def build(self):
        # Symbol plan: A center-parted bob frames a circular jaw. The crossed garment neckline keeps the supplied hanbok-style clothing readable.

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
        path('hair',(8,26),[('L',(8,16)),('A',(24,4),16,12,True),('A',(40,16),16,12,True),('L',(40,26))])
        path('fringe',(16,16),[('C',(24,8),(20,16),(24,12)),('C',(32,16),(24,12),(28,16))])
        self.add_arc('face',(32,16),(16,16),radius_x=8);join('face','fringe')
        # Fringe meets the crown at an actual common point through this short part line.
        line('part',(24,4),(24,8));join('part','hair');join('part','fringe')
        bottom=24

        top=bottom+4
        path('body',(8,44),[('L',(8,42)),('A',(18,top),10,42-top,True),('L',(24,top)),('L',(30,top)),('A',(40,42),10,42-top,True),('L',(40,44))])
        join('face','body')
        poly('collar',(18,top),(28,42),(34,36));join('collar','body')
