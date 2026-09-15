"""Three stacked rows, the lowest split into two equal bars; outlined capsules reduced to open strokes; extremes (4,8)-(44,40)."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f4a222e3-ab2c-4c2e-9890-5f82e7505981'
SOURCE_PATH = 'pictographic-primitives/logos/elastic stack logo_f4a222e3-ab2c-4c2e-9890-5f82e7505981.svg'
AUTHOR = 'gpt-6'

class ElasticStackLogo(Solo48):
    icon_id = 'elastic-stack-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'brands/logos'
    aliases = ()
    keywords = ('elastic-stack', 'elk', 'elastic', 'logo', 'brand', 'stack', 'data')

    def build(self):
        # Plan: Three stacked rows, the lowest split into two equal bars; outlined capsules reduced to open strokes; extremes (4,8)-(44,40).
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

        for i,y in enumerate((8,24)):line(f'full-row-{i}',(4,y),(44,y))
        for i,(left,right) in enumerate(((4,18),(30,44))):line(f'bottom-{i}',(left,40),(right,40))
