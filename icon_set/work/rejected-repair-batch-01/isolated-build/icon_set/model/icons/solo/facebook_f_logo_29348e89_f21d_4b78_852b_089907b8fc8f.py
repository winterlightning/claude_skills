"""A tall lowercase f with a rounded upper hook and a short crossbar; reduce the outlined letter to its skeleton; extremes (8,4)-(40,44)."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '29348e89-f21d-4b78-852b-089907b8fc8f'
SOURCE_PATH = 'pictographic-primitives/logos/facebook logo_29348e89-f21d-4b78-852b-089907b8fc8f.svg'
AUTHOR = 'gpt-6'

class FacebookFLogo(Solo48):
    icon_id = 'facebook-f-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'brands/logos'
    aliases = ()
    keywords = ('facebook', 'social', 'letter-f', 'logo', 'brand', 'meta', 'network')

    def build(self):
        # Plan: A tall lowercase f with a rounded upper hook and a short crossbar; reduce the outlined letter to its skeleton; extremes (8,4)-(40,44).
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

        path('stem',(24,44),[('L',(24,24)),('L',(24,16)),('A',(36,4),12,12,True),('L',(40,4))])
        poly('crossbar',(8,24),(24,24),(36,24));join('stem','crossbar')
