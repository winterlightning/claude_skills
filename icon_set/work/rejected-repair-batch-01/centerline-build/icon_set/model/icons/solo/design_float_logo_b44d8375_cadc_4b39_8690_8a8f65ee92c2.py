"""A lifebuoy with two concentric circles and four cardinal seams; omit the redundant third outer rim; radii 20 and 10 leave a broad band."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b44d8375-cadc-4b39-8690-8a8f65ee92c2'
SOURCE_PATH = 'pictographic-primitives/logos/design float logo_b44d8375-cadc-4b39-8690-8a8f65ee92c2.svg'
AUTHOR = 'gpt-6'

class DesignFloatLogo(Solo48):
    icon_id = 'design-float-logo'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'brands/logos'
    aliases = ()
    keywords = ('design-float', 'lifebuoy', 'logo', 'brand', 'design', 'community', 'ring')

    def build(self):
        # Plan: A lifebuoy with two concentric circles and four cardinal seams; omit the redundant third outer rim; radii 20 and 10 leave a broad band.
        # Construction reference: Lucide life-buoy: two concentric rings with shared seam endpoints.

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

        axis=24
        for name,r in (('outer',20),('inner',10)):
            pts=[(axis,axis-r),(axis+r,axis),(axis,axis+r),(axis-r,axis)]
            for i in range(4): self.add_arc(f'{name}-{i}',pts[i],pts[(i+1)%4],radius_x=r)
            self.add_contour(name,*(f'{name}-{i}' for i in range(4)),closed=True)
        for i,(dx,dy) in enumerate(((0,-1),(1,0),(0,1),(-1,0))):
            line(f'seam-{i}',(axis+10*dx,axis+10*dy),(axis+20*dx,axis+20*dy))
            join(f'seam-{i}','outer');join(f'seam-{i}','inner')
