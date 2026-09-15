"""A rectangular form with an angular F and two detached right bars; reduce the inner zigzag to a clear F skeleton; extremes (4,8)-(44,40)."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd7a1207e-6e7d-41d0-951a-f68222d66b48'
SOURCE_PATH = 'pictographic-primitives/logos/formstack logo_d7a1207e-6e7d-41d0-951a-f68222d66b48.svg'
AUTHOR = 'gpt-6'

class FormstackLogo(Solo48):
    icon_id = 'formstack-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'brands/logos'
    aliases = ()
    keywords = ('formstack', 'forms', 'letter-f', 'logo', 'brand', 'workflow', 'data')

    def build(self):
        # Plan: A rectangular form with an angular F and two detached right bars; reduce the inner zigzag to a clear F skeleton; extremes (4,8)-(44,40).
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

        poly('form',(4,8),(28,8),(28,40),(4,40),closed=True)
        poly('f',(13,31),(13,25),(13,17),(20,17));line('arm',(13,25),(20,25));join('f','arm')
        for i,x in enumerate((36,44)):line(f'stack-{i}',(x,12),(x,36))
