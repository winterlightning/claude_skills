"""A roundel with two parallel horizontal bands; shorten band ends to preserve their separation from the ring and use 8-unit vertical spacing."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f15b9962-ff98-47e5-aadc-880f23be6224'
SOURCE_PATH = 'pictographic-primitives/logos/eclipe ide logo_f15b9962-ff98-47e5-aadc-880f23be6224.svg'
AUTHOR = 'gpt-6'

class EclipseIdeLogo(Solo48):
    icon_id = 'eclipse-ide-logo'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('eclipse', 'ide', 'java', 'logo', 'brand', 'developer', 'editor')

    def build(self):
        # Plan: A roundel with two parallel horizontal bands; shorten band ends to preserve their separation from the ring and use 8-unit vertical spacing.
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

        circle('ring',24,24,20)
        for i,y in enumerate((20,28)):line(f'band-{i}',(14,y),(34,y))
