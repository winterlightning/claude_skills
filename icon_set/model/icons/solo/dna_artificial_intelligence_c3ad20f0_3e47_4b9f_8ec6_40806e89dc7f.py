"""Bad-stroke revision. Lucide dna: two continuous S-shaped strands with deliberate crossings.
Omissions: No rungs added: supplied source has only two strands.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c3ad20f0-3e47-4b9f-8ec6-40806e89dc7f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__dna-artificial-intelligence/20260924T093003Z-thuan-mac/reference/dna_c3ad20f0-3e47-4b9f-8ec6-40806e89dc7f.svg'
AUTHOR = 'gpt-6'
class Revision(Solo48):
    icon_id = 'dna-artificial-intelligence-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('dna',)
    def build(self):

        # Typed continuous paths own their junctions. Repeated parts share parameters.
        def path(name, start, commands, closed=False):
            ids=[]; here=start
            for i, (kind,end,*args) in enumerate(commands):
                ident=f'{name}-{i}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                ids.append(ident);here=end
            self.add_contour(name,*ids,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        # The second strand is the exact half-turn of the first; both crossings are shared nodes.
        for i in range(2):
            def p(x,y): return (x,y) if i==0 else (48-x,48-y)
            path('strand-'+str(i),p(32,6),[('C',p(30,16),p(28,8),p(30,12)),('C',p(18,32),p(30,28),p(30,32)),('C',p(6,34),p(14,32),p(10,30))])
        join('strand-0','strand-1')
