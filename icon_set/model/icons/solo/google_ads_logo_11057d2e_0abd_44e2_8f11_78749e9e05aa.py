"""Two slanted strokes form an open A with a circular node at the left foot; simplify outlined bars to a forked stroke; extremes (6,6)-(42,42)."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '11057d2e-0abd-44e2-8f11-78749e9e05aa'
SOURCE_PATH = 'pictographic-primitives/logos/google ads logo_11057d2e-0abd-44e2-8f11-78749e9e05aa.svg'
AUTHOR = 'gpt-6'

class GoogleAdsLogo(Solo48):
    icon_id = 'google-ads-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('google-ads', 'google', 'advertising', 'letter-a', 'logo', 'brand', 'marketing')

    def build(self):
        # Plan: Two slanted strokes form an open A with a circular node at the left foot; simplify outlined bars to a forked stroke; extremes (6,6)-(42,42).
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

        circle('foot',10,38,4)
        poly('a',(14,38),(24,6),(42,42));join('foot','a')
