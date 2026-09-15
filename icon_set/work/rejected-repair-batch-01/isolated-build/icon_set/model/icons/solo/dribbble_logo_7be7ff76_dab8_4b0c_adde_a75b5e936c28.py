"""A basketball with three sweeping seams and exact shared crossing nodes; retain asymmetric spherical flow and all three seams."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7be7ff76-dab8-4b0c-adde-a75b5e936c28'
SOURCE_PATH = 'pictographic-primitives/logos/dribbble logo_7be7ff76-dab8-4b0c-adde-a75b5e936c28.svg'
AUTHOR = 'gpt-6'

class DribbbleLogo(Solo48):
    icon_id = 'dribbble-logo'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'brands/logos'
    aliases = ()
    keywords = ('dribbble', 'basketball', 'design', 'logo', 'brand', 'portfolio', 'creative')

    def build(self):
        # Plan: A basketball with three sweeping seams and exact shared crossing nodes; retain asymmetric spherical flow and all three seams.
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

        pts=[(24,4),(40,12),(44,24),(36,40),(24,44),(8,36),(4,24),(12,8)]
        for i in range(len(pts)):self.add_arc(f'rim-{i}',pts[i],pts[(i+1)%len(pts)],radius_x=20)
        self.add_contour('rim',*(f'rim-{i}' for i in range(len(pts))),closed=True)
        path('vertical',(12,8),[('C',(24,18),(17,10),(21,14)),('C',(32,28),(28,22),(30,25)),('C',(36,40),(34,32),(36,36))])
        path('upper',(4,24),[('C',(24,18),(11,25),(18,22)),('C',(40,12),(31,16),(36,14))])
        path('lower',(8,36),[('C',(32,28),(15,34),(23,28)),('C',(44,24),(36,28),(41,25))])
        for n in ('vertical','upper','lower'):join('rim',n)
        join('vertical','upper');join('vertical','lower')
