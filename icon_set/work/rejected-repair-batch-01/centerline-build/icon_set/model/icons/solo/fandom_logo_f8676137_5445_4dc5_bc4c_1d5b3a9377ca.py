"""A faceted heart with mirrored peaks and one broad diagonal fold; remove the narrow lower band; extremes (6,6)-(42,42)."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f8676137-5445-4dc5-bc4c-1d5b3a9377ca'
SOURCE_PATH = 'pictographic-primitives/logos/fandom logo_f8676137-5445-4dc5-bc4c-1d5b3a9377ca.svg'
AUTHOR = 'gpt-6'

class FandomLogo(Solo48):
    icon_id = 'fandom-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'brands/logos'
    aliases = ()
    keywords = ('fandom', 'wiki', 'heart', 'logo', 'brand', 'community', 'fans')

    def build(self):
        # Plan: A faceted heart with mirrored peaks and one broad diagonal fold; remove the narrow lower band; extremes (6,6)-(42,42).
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

        poly('heart',(6,18),(15,6),(24,16),(33,6),(42,18),(42,32),(24,42),(6,32),closed=True)
        poly('fold',(6,18),(24,28),(42,18));join('heart','fold')
