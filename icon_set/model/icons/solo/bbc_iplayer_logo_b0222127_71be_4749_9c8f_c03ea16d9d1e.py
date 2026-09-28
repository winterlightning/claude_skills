"""A smooth outlined play mark with a single rounded right tip. Preserve the supplied triangular logo component and solo family; no missing lettering invented.
References: Supplied original; shared geometric construction principles.
Authored directly on SOLO48; original retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b0222127-71be-4749-9c8f-c03ea16d9d1e'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_06/bbc iplayer logo_b0222127-71be-4749-9c8f-c03ea16d9d1e.svg'
AUTHOR = 'gpt-6'

class BbcIplayerLogo(Solo48):
    icon_id = 'bbc-iplayer-logo'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('bbc', 'iplayer', 'logo')

    def build(self):
        # Symbol plan: A smooth outlined play mark with a single rounded right tip. Preserve the supplied triangular logo component and solo family; no missing lettering invented.

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
        path('play',(12,8),[('L',(40,22)),('A',(40,26),3,3,True),('L',(12,40)),('L',(12,8))],True)
