"""A serif E with bracket-like outer terminals and a short vertical middle tick; filled letter ribbons reduced to a clear skeleton; extremes (8,4)-(40,44)."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd72379e2-f45e-4d46-b1b7-ff40702bd423'
SOURCE_PATH = 'pictographic-primitives/logos/etsy logo_d72379e2-f45e-4d46-b1b7-ff40702bd423.svg'
AUTHOR = 'gpt-6'

class EtsyLogo(Solo48):
    icon_id = 'etsy-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'brands/logos'
    aliases = ()
    keywords = ('etsy', 'marketplace', 'letter-e', 'logo', 'brand', 'handmade', 'shop')

    def build(self):
        # Plan: A serif E with bracket-like outer terminals and a short vertical middle tick; filled letter ribbons reduced to a clear skeleton; extremes (8,4)-(40,44).
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

        poly('spine',(16,4),(16,24),(16,44))
        poly('top',(8,4),(16,4),(38,4),(38,12))
        poly('bottom',(8,44),(16,44),(40,44),(40,36))
        line('middle',(16,24),(30,24));poly('tick',(30,20),(30,24),(30,28))
        for a,b in (('spine','top'),('spine','bottom'),('spine','middle'),('middle','tick')):join(a,b)
