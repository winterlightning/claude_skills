"""Three upright arrows share one narrow head definition and bottom baseline; heights preserve the source order; outlined arrows reduced to open strokes; extremes (6,6)-(42,42)."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'bdb31740-6817-41b2-aec1-b0a6123aa1f7'
SOURCE_PATH = 'pictographic-primitives/logos/design bump logo_bdb31740-6817-41b2-aec1-b0a6123aa1f7.svg'
AUTHOR = 'gpt-6'

class DesignBumpLogo(Solo48):
    icon_id = 'design-bump-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('design-bump', 'arrows', 'upvote', 'logo', 'brand', 'design', 'community')

    def build(self):
        # Plan: Three upright arrows share one narrow head definition and bottom baseline; heights preserve the source order; outlined arrows reduced to open strokes; extremes (6,6)-(42,42).
        # Construction reference: Lucide arrow-up: shared head/shaft tip and open stroke construction.

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

        for i,(x,top) in enumerate(((10,18),(24,6),(38,30))):
            tip=(x,top)
            poly(f'head-{i}',(x-4,top+4),tip,(x+4,top+4))
            line(f'shaft-{i}',tip,(x,42));join(f'head-{i}',f'shaft-{i}')
