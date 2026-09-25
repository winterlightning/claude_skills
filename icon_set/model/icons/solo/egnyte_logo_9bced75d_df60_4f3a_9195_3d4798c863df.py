"""An open Y with three detached rays; outlined Y reduced to one stroke, mirrored lower rays share offsets; extremes (6,6)-(42,42)."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9bced75d-df60-4f3a-9195-3d4798c863df'
SOURCE_PATH = 'pictographic-primitives/logos/egnyte logo_9bced75d-df60-4f3a-9195-3d4798c863df.svg'
AUTHOR = 'gpt-6'

class EgnyteLogo(Solo48):
    icon_id = 'egnyte-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('egnyte', 'file-sharing', 'logo', 'brand', 'cloud', 'enterprise', 'letter-y')

    def build(self):
        # Plan: An open Y with three detached rays; outlined Y reduced to one stroke, mirrored lower rays share offsets; extremes (6,6)-(42,42).
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

        poly('fork',(6,14),(24,26),(42,14));line('stem',(24,26),(24,42));join('fork','stem')
        line('top-ray',(24,6),(24,14))
        for i,sign in enumerate((-1,1)):line(f'lower-ray-{i}',(24+12*sign,30),(24+18*sign,34))
