"""Fourfold stepped star and a shared central cross; retain cardinal tips and square corners, omitting tight diagonal subdivisions."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0ed3165d-d4b8-4299-93eb-daf71defa869'
SOURCE_PATH = 'pictographic-primitives/logos/centos logo_0ed3165d-d4b8-4299-93eb-daf71defa869.svg'
AUTHOR = 'gpt-6'

class CentosLogo(Solo48):
    icon_id = 'centos-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'brands/logos'
    aliases = ()
    keywords = ('centos', 'linux', 'logo', 'brand', 'operating-system', 'server', 'star')

    def build(self):
        # Plan: Fourfold stepped star and a shared central cross; retain cardinal tips and square corners, omitting tight diagonal subdivisions.
        # Construction reference: No useful subject match found; source brand render informs the geometry.

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

        axis=24
        # Four repeated quadrants define the stepped star silhouette.
        quarter=[(24,6),(30,12),(36,12),(36,18)]
        points=[]
        for i in range(4):
            for px,py in quarter:
                x,y=px-axis,py-axis
                for _ in range(i): x,y=-y,x
                points.append((axis+x,axis+y))
        poly('star',*points,closed=True)
        for i,p in enumerate(((24,6),(42,24),(24,42),(6,24))):
            line(f'spoke-{i}',(axis,axis),p)
            join('star',f'spoke-{i}')
            for j in range(i):join(f'spoke-{i}',f'spoke-{j}')
