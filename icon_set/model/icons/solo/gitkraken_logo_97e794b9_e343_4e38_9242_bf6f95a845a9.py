"""A pointed squid with two long outer tentacles and two shorter inner tentacles; omit the tiny eye rings and merge lower repeated limbs; extremes (6,6)-(42,42)."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '97e794b9-e343-4e38-9242-bf6f95a845a9'
SOURCE_PATH = 'pictographic-primitives/logos/gitkraken logo_97e794b9-e343-4e38-9242-bf6f95a845a9.svg'
AUTHOR = 'gpt-6'

class GitkrakenLogo(Solo48):
    icon_id = 'gitkraken-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('gitkraken', 'kraken', 'git', 'logo', 'brand', 'developer', 'squid')

    def build(self):
        # Plan: A pointed squid with two long outer tentacles and two shorter inner tentacles; omit the tiny eye rings and merge lower repeated limbs; extremes (6,6)-(42,42).
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

        poly('head',(16,24),(14,16),(24,6),(34,16),(32,24))
        path('left',(6,18),[('C',(16,42),(6,30),(6,38)),('L',(16,24))]);join('head','left')
        path('right',(42,18),[('C',(32,42),(42,30),(42,38)),('L',(32,24))]);join('head','right')
        poly('base',(16,24),(24,24),(32,24));join('head','base');join('left','base');join('right','base')
        line('middle',(24,24),(24,42));join('base','middle')
