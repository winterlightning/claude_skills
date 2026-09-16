"""A clipped square with three genuinely parallel diagonal divisions and exact boundary joins. Broad bands preserve the striped mark at native size.
References: Supplied original; shared geometric construction principles.
Authored directly on SOLO48; original retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ca67be63-3b5a-4b74-800b-f1df0601b64c'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_01/affinity publisher logo_ca67be63-3b5a-4b74-800b-f1df0601b64c.svg'
AUTHOR = 'gpt-6'

class AffinityPublisherLogo(Solo48):
    icon_id = 'affinity-publisher-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'Uncategorized'
    aliases = ()
    keywords = ('affinity', 'publisher', 'logo')

    def build(self):
        # Symbol plan: A clipped square with three genuinely parallel diagonal divisions and exact boundary joins. Broad bands preserve the striped mark at native size.

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
        poly('outline',(6,30),(12,18),(18,6),(30,6),(42,6),(42,24),(42,42),(28,42),(6,42),closed=True)
        for j,(a,b) in enumerate([((12,18),(28,42)),((18,6),(42,42)),((30,6),(42,24))]):
         line(f'band-{j}',a,b);join('outline',f'band-{j}')
