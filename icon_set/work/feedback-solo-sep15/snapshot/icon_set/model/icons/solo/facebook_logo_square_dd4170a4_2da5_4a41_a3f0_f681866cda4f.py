"""A rounded square with a lowercase f, hooked top and attached crossbar; the stem shares the bottom border node; extremes (6,6)-(42,42)."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'dd4170a4-2da5-4a41-a3f0-f681866cda4f'
SOURCE_PATH = 'pictographic-primitives/logos/facebook logo 1_dd4170a4-2da5-4a41-a3f0-f681866cda4f.svg'
AUTHOR = 'gpt-6'

class FacebookLogoSquare(Solo48):
    icon_id = 'facebook-logo-square'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'brands/logos'
    aliases = ()
    keywords = ('facebook', 'social', 'letter-f', 'logo', 'brand', 'meta', 'square')

    def build(self):
        # Plan: A rounded square with a lowercase f, hooked top and attached crossbar; the stem shares the bottom border node; extremes (6,6)-(42,42).
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

        path('frame',(10,6),[('L',(38,6)),('A',(42,10),4,4,True),('L',(42,38)),('A',(38,42),4,4,True),('L',(24,42)),('L',(10,42)),('A',(6,38),4,4,True),('L',(6,10)),('A',(10,6),4,4,True)],True)
        path('stem',(24,42),[('L',(24,26)),('L',(24,23)),('A',(32,15),8,8,True)])
        poly('bar',(16,26),(24,26),(32,26));join('frame','stem');join('stem','bar')
