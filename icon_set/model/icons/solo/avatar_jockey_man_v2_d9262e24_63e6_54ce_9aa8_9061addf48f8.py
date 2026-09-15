"""A round riding helmet with a short forward peak and circular jaw, above a smooth jersey with a diagonal racing stripe.
References: Human user.svg and Lucide user-round; original riding cap.
Authored directly on SOLO48; original retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd9262e24-63e6-54ce-9aa8-9061addf48f8'
SOURCE_PATH = 'pictographic-primitives/avatars/avatar jockey man_d9262e24-63e6-54ce-9aa8-9061addf48f8.svg'
AUTHOR = 'gpt-6'

class AvatarJockeyManVariant2(Solo48):
    icon_id = 'avatar-jockey-man-v2'
    variant_of = 'avatar-jockey-man'
    variant_label = 'Reconstructed solo drawing after rejection'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('avatar', 'jockey', 'man')

    def build(self):
        # Symbol plan: A round riding helmet with a short forward peak and circular jaw, above a smooth jersey with a diagonal racing stripe.

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
        path('helmet',(14,14),[('A',(34,14),10,10,True),('L',(40,14))])
        self.add_arc('face',(34,14),(14,14),radius_x=10);line('brim',(14,14),(34,14));join('face','brim');join('helmet','brim');join('helmet','face');bottom=24

        top=bottom+4
        path('body',(8,44),[('L',(8,42)),('A',(18,top),10,42-top,True),('L',(24,top)),('L',(30,top)),('A',(40,42),10,42-top,True),('L',(40,44))])
        join('face','body')
        line('jersey',(18,top),(32,44));join('jersey','body')
