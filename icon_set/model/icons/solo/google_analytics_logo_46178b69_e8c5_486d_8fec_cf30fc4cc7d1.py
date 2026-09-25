"""Three equally spaced bars increase in height from left to right; reduce the narrow capsule outlines to clear strokes; extremes (4,8)-(44,40)."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '46178b69-e8c5-486d-8fec-cf30fc4cc7d1'
SOURCE_PATH = 'pictographic-primitives/logos/google analytics logo_46178b69-e8c5-486d-8fec-cf30fc4cc7d1.svg'
AUTHOR = 'gpt-6'

class GoogleAnalyticsLogo(Solo48):
    icon_id = 'google-analytics-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('google-analytics', 'google', 'analytics', 'chart', 'logo', 'brand', 'data')

    def build(self):
        # Plan: Three equally spaced bars increase in height from left to right; reduce the narrow capsule outlines to clear strokes; extremes (4,8)-(44,40).
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

        for i,(x,top) in enumerate(((4,34),(24,22),(44,8))):line(f'bar-{i}',(x,top),(x,40))
