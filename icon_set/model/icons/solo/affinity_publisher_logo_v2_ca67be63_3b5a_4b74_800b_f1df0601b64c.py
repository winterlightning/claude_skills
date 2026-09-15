"""One clipped square boundary and a series of truly parallel bands, all with rise/run 2. Reuse exact attachment nodes.
References: Supplied original; shared geometric construction principles.
Authored directly on SOLO48; original retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ca67be63-3b5a-4b74-800b-f1df0601b64c'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_01/affinity publisher logo_ca67be63-3b5a-4b74-800b-f1df0601b64c.svg'
AUTHOR = 'gpt-6'

class AffinityPublisherLogoVariant2(Solo48):
    icon_id = 'affinity-publisher-logo-v2'
    variant_of = 'affinity-publisher-logo'
    variant_label = 'Reconstructed solo drawing after rejection'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'Uncategorized'
    aliases = ()
    keywords = ('affinity', 'publisher', 'logo')

    def build(self):
        # Symbol plan: One clipped square boundary and a series of truly parallel bands, all with rise/run 2. Reuse exact attachment nodes.

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
        poly('outline',(6,34),(10,26),(15,16),(20,6),(30,6),(42,6),(42,30),(42,42),(32,42),(18,42),(6,42),closed=True)
        for j,(a,b) in enumerate([((10,26),(18,42)),((15,16),(28,42)),((20,6),(38,42)),((30,6),(42,30))]):
         line(f'band-{j}',a,b);join('outline',f'band-{j}')
