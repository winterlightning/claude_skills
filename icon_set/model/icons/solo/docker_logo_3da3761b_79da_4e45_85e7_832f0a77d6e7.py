"""A whale hull carrying a stepped four-container stack and a two-lobed raised tail; fewer containers and no tiny eye; grid cells share 8-unit edges; extremes (4,8)-(44,40)."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3da3761b-79da-4e45-85e7-832f0a77d6e7'
SOURCE_PATH = 'pictographic-primitives/logos/docker logo_3da3761b-79da-4e45-85e7-832f0a77d6e7.svg'
AUTHOR = 'gpt-6'

class DockerLogo(Solo48):
    icon_id = 'docker-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'brands/logos'
    aliases = ()
    keywords = ('docker', 'containers', 'whale', 'logo', 'brand', 'devops', 'developer')

    def build(self):
        # Plan: A whale hull carrying a stepped four-container stack and a two-lobed raised tail; fewer containers and no tiny eye; grid cells share 8-unit edges; extremes (4,8)-(44,40).
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

        path('hull',(4,24),[('L',(8,24)),('L',(16,24)),('L',(24,24)),('L',(32,24)),('C',(36,16),(35,24),(36,22)),('L',(40,22)),('L',(44,20)),('C',(36,34),(44,30),(40,34)),('C',(18,40),(32,38),(26,40)),('C',(4,24),(9,40),(4,34))],True)
        edges=[('top',(16,8),(24,8)),('upper-left',(16,8),(16,16)),('upper-right',(24,8),(24,16))]
        for i,x in enumerate((8,16,24)):
            edges.append((f'row-{i}',(x,16),(x+8,16)))
        for i,x in enumerate((8,16,24,32)):
            edges.append((f'column-{i}',(x,16),(x,24)))
        graph(edges)
        for name,a,b in edges:
            if b[1]==24:join(name,'hull')
