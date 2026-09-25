"""Three broad rounded lobes meet at a Y-shaped section junction; omit the two small rear loops to preserve clear regions; extremes (6,6)-(42,42)."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c63a152d-a2d5-4ecd-84d2-6c3b857329b7'
SOURCE_PATH = 'pictographic-primitives/logos/elastic logo_c63a152d-a2d5-4ecd-84d2-6c3b857329b7.svg'
AUTHOR = 'gpt-6'

class ElasticLogo(Solo48):
    icon_id = 'elastic-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('elastic', 'elasticsearch', 'logo', 'brand', 'search', 'data', 'knot')

    def build(self):
        # Plan: Three broad rounded lobes meet at a Y-shaped section junction; omit the two small rear loops to preserve clear regions; extremes (6,6)-(42,42).
        # Construction reference: No useful subject-specific Lucide match; construction follows the supplied brand render.

        def path(name, start, commands, closed=False):
            members=[]
            here=start
            for i, command in enumerate(commands):
                kind, end, *args=command
                part=f"{name}-{i}"
                if kind=='L': self.add_line(part,here,end)
                elif kind=='A':
                    rx,ry,sweep=args
                    self.add_arc(part,here,end,radius_x=rx,radius_y=ry,sweep=sweep)
                elif kind=='C': self.add_bezier(part,here,(args[0],args[1],end))
                members.append(part); here=end
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def c_ring(name):
            # Exact radius-20 points on the circle about (24,24).
            self.add_arc(name,(36,8),(36,40),radius_x=20,large_arc=True,sweep=False)
        poly=self.add_polyline
        line=self.add_line
        join=lambda a,b:self.relate('connect',a,b)

        def graph(edges):
            for name,a,b in edges: line(name,a,b)
            for i,(name,a,b) in enumerate(edges):
                for other,c,d in edges[:i]:
                    if {a,b}&{c,d}: join(name,other)

        path('lobes',(26,6),[('A',(38,18),12,12,True),('C',(42,26),(42,18),(42,22)),('C',(34,34),(42,32),(38,34)),('C',(20,42),(32,40),(27,42)),('C',(6,28),(12,42),(6,36)),('C',(14,18),(6,22),(10,18)),('C',(26,6),(14,11),(19,6))],True)
        for i,p in enumerate(((14,18),(38,18),(34,34))):
            line(f'section-{i}',p,(26,26));join('lobes',f'section-{i}')
            for j in range(i):join(f'section-{i}',f'section-{j}')
