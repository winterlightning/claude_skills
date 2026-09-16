"""A broad draped headcloth frames a circular jaw; the robe has smooth open shoulders and one central seam.
References: Shared human user.svg and Lucide user-round; supplied headcloth and robe.
Authored directly on SOLO48; original retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'dd92cb2d-e66d-53d1-835f-92be92e0873e'
SOURCE_PATH = 'pictographic-primitives/avatars/arabian man_dd92cb2d-e66d-53d1-835f-92be92e0873e.svg'
AUTHOR = 'gpt-6'

class ArabianMan(Solo48):
    icon_id = 'arabian-man'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('arabian', 'man')

    def build(self):
        # Symbol plan: A broad draped headcloth frames a circular jaw; the robe has smooth open shoulders and one central seam.

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
        path('cloth',(8,26),[('L',(8,16)),('A',(40,16),16,12,True),('L',(40,26))])
        poly('band',(8,16),(16,16),(32,16),(40,16));join('cloth','band')
        self.add_arc('face',(32,16),(16,16),radius_x=8);join('face','band');bottom=24

        top=bottom+4
        path('body',(8,44),[('L',(8,42)),('A',(18,top),10,42-top,True),('L',(24,top)),('L',(30,top)),('A',(40,42),10,42-top,True),('L',(40,44))])
        join('face','body')
        line('robe-front',(24,top),(24,44));join('robe-front','body')
