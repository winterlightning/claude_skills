"""The rounded Fedora outline with squared lower-left corner and a looped lowercase f; retain the loop and hooked top; extremes (6,6)-(42,42)."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b0937801-63f0-487f-bc62-cfd9e407dfc9'
SOURCE_PATH = 'pictographic-primitives/logos/fedora logo_b0937801-63f0-487f-bc62-cfd9e407dfc9.svg'
AUTHOR = 'gpt-6'

class FedoraLogo(Solo48):
    icon_id = 'fedora-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'brands/logos'
    aliases = ()
    keywords = ('fedora', 'linux', 'letter-f', 'logo', 'brand', 'operating-system', 'open-source')

    def build(self):
        # Plan: The rounded Fedora outline with squared lower-left corner and a looped lowercase f; retain the loop and hooked top; extremes (6,6)-(42,42).
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

        path('envelope',(6,24),[('A',(24,6),18,18,True),('A',(42,24),18,18,True),('A',(24,42),18,18,True),('L',(6,42)),('L',(6,24))],True)
        path('f',(30,20),[('A',(24,20),3,3,False),('L',(24,26)),('L',(24,29)),('A',(16,29),4,4,True),('C',(24,26),(16,26),(20,26)),('L',(32,26))])
