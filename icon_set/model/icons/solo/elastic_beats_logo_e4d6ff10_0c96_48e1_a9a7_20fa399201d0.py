"""A capital B with two rounded bowls sharing a waist, the lower bowl wider; omit the redundant narrow middle ribbon; extremes (6,6)-(42,42)."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e4d6ff10-0c96-48e1-a9a7-20fa399201d0'
SOURCE_PATH = 'pictographic-primitives/logos/elastic beats logo_e4d6ff10-0c96-48e1-a9a7-20fa399201d0.svg'
AUTHOR = 'gpt-6'

class ElasticBeatsLogo(Solo48):
    icon_id = 'elastic-beats-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('elastic', 'beats', 'letter-b', 'logo', 'brand', 'data', 'shipper')

    def build(self):
        # Plan: A capital B with two rounded bowls sharing a waist, the lower bowl wider; omit the redundant narrow middle ribbon; extremes (6,6)-(42,42).
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

        path('outline',(6,6),[('L',(26,6)),('A',(26,24),12,9,True),('A',(26,42),16,9,True),('L',(6,42)),('L',(6,24)),('L',(6,6))],True)
        line('waist',(6,24),(26,24));join('waist','outline')
