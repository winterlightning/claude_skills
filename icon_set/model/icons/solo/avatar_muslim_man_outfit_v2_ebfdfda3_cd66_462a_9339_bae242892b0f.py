"""A simple flat kufi cap above a circular jaw and a buttoned tunic. Clothing carries the identity; no facial attributes are invented.
References: Human user.svg, Lucide user-round and supplied cap/tunic.
Authored directly on SOLO48; original retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ebfdfda3-cd66-462a-9339-bae242892b0f'
SOURCE_PATH = 'pictographic-primitives/avatars/muslim man outfit_ebfdfda3-cd66-462a-9339-bae242892b0f.svg'
AUTHOR = 'gpt-6'

class AvatarMuslimManOutfitVariant2(Solo48):
    icon_id = 'avatar-muslim-man-outfit-v2'
    variant_of = 'avatar-muslim-man-outfit'
    variant_label = 'Reconstructed solo drawing after rejection'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('avatar', 'muslim', 'man', 'outfit')

    def build(self):
        # Symbol plan: A simple flat kufi cap above a circular jaw and a buttoned tunic. Clothing carries the identity; no facial attributes are invented.

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
        poly('cap',(14,14),(14,4),(34,4),(34,14),closed=True)
        self.add_arc('face',(34,14),(14,14),radius_x=10);join('face','cap');bottom=24

        top=bottom+4
        path('body',(8,44),[('L',(8,42)),('A',(18,top),10,42-top,True),('L',(24,top)),('L',(30,top)),('A',(40,42),10,42-top,True),('L',(40,44))])
        join('face','body')
        dot('button',(24,39))
