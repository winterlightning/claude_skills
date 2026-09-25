"""A six-node network, reduced to a five-sided perimeter and five hub connections; round stroke junctions replace oversized node discs and keep the wireframe identity; extremes (4,8)-(44,40)."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '657e8326-5770-4f03-bea9-9f229f7f9497'
SOURCE_PATH = 'pictographic-primitives/logos/dzone logo_657e8326-5770-4f03-bea9-9f229f7f9497.svg'
AUTHOR = 'gpt-6'

class DzoneLogo(Solo48):
    icon_id = 'dzone-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('dzone', 'developer', 'network', 'logo', 'brand', 'community', 'nodes')

    def build(self):
        # Plan: A six-node network, reduced to a five-sided perimeter and five hub connections; round stroke junctions replace oversized node discs and keep the wireframe identity; extremes (4,8)-(44,40).
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

        nodes=[(4,30),(22,8),(44,16),(40,32),(24,40),(26,24)]
        edges=[]
        for i in range(5):
            edges.append((f'rim-{i}',nodes[i],nodes[(i+1)%5]))
            edges.append((f'hub-{i}',nodes[5],nodes[i]))
        graph(edges)
        # Each node is a round stroke junction at one exact shared point.
        for i,p in enumerate(nodes):
            self.add_dot(f'node-{i}',p)
            for name,a,b in edges:
                if p in (a,b):join(name,f'node-{i}')
