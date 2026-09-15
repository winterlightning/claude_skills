"""A consistent bead loop and a heart turned toward its attachment. Smooth lobes and a coherent pointed lower-right tip preserve the requested charm angle.
References: Supplied original; shared geometric construction principles.
Authored directly on SOLO48; original retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8956c423-cf27-57a5-a230-a97f31d05f44'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-04/necklace pendant_8956c423-cf27-57a5-a230-a97f31d05f44.svg'
AUTHOR = 'gpt-6'

class BeadedLoopWithHeartCharmVariant2(Solo48):
    icon_id = 'beaded-loop-with-heart-charm-v2'
    variant_of = 'beaded-loop-with-heart-charm'
    variant_label = 'Reconstructed solo drawing after rejection'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('beaded', 'loop', 'with', 'heart', 'charm')

    def build(self):
        # Symbol plan: A consistent bead loop and a heart turned toward its attachment. Smooth lobes and a coherent pointed lower-right tip preserve the requested charm angle.

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
        for j,p in enumerate([(18,6),(10,10),(6,18),(10,26),(18,30),(26,26),(30,18),(26,10)]):dot(f'bead-{j}',p)
        path('heart',(32,30),[('C',(40,30),(32,24),(40,24)),('C',(42,42),(40,33),(42,38)),('C',(30,40),(38,42),(33,40)),('C',(32,30),(24,40),(24,32))],True)
        line('link',(26,26),(32,30));join('link','heart');join('link','bead-5')
