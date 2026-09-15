"""A circular face with a short bob and a readable apron within open rounded shoulders; preserve the source hair and apron.
References: Human user.svg, Lucide shirt and supplied bob/apron.
Authored directly on SOLO48; original retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1a6bb88a-8366-58c0-b6a2-58ed57586fb3'
SOURCE_PATH = 'pictographic-primitives/avatars/avatar woman store clerk_1a6bb88a-8366-58c0-b6a2-58ed57586fb3.svg'
AUTHOR = 'gpt-6'

class AvatarWomanStoreClerkVariant2(Solo48):
    icon_id = 'avatar-woman-store-clerk-v2'
    variant_of = 'avatar-woman-store-clerk'
    variant_label = 'Reconstructed solo drawing after rejection'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('avatar', 'woman', 'store', 'clerk')

    def build(self):
        # Symbol plan: A circular face with a short bob and a readable apron within open rounded shoulders; preserve the source hair and apron.

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
        path('hair',(8,26),[('L',(8,16)),('A',(24,4),16,12,True),('A',(40,16),16,12,True),('L',(40,26))])
        path('fringe',(14,16),[('C',(24,8),(20,16),(24,12)),('C',(34,16),(24,12),(28,16))])
        self.add_arc('face',(34,16),(14,16),radius_x=10);join('face','fringe')
        # Fringe meets the crown at an actual common point through this short part line.
        line('part',(24,4),(24,8));join('part','hair');join('part','fringe')
        bottom=26

        top=bottom+4
        path('body',(8,44),[('L',(8,42)),('A',(18,top),10,42-top,True),('L',(24,top)),('L',(30,top)),('A',(40,42),10,42-top,True),('L',(40,44))])
        join('face','body')
        poly('apron',(18,top),(18,44),(30,44),(30,top));join('apron','body')
