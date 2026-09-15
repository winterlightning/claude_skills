"""An open asymmetric five-point star with a long diagonal swoosh; share the lower return with an exact node on the diagonal so its triangular opening stays clear; extremes (6,6)-(42,42)."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'cbb3e91d-261a-447f-af15-2de6db36927d'
SOURCE_PATH = 'pictographic-primitives/logos/esea logo_cbb3e91d-261a-447f-af15-2de6db36927d.svg'
AUTHOR = 'gpt-6'

class EseaLogo(Solo48):
    icon_id = 'esea-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'brands/logos'
    aliases = ()
    keywords = ('esea', 'esports', 'gaming', 'star', 'logo', 'brand', 'league')

    def build(self):
        # Plan: An open asymmetric five-point star with a long diagonal swoosh; share the lower return with an exact node on the diagonal so its triangular opening stays clear; extremes (6,6)-(42,42).
        # Construction reference: Lucide star: coherent angular contour with readable valleys.

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

        poly('star',(14,26),(6,18),(22,18),(32,6),(32,18),(42,18),(30,26),(18,34),(6,42))
        poly('lower-point',(30,26),(30,42),(18,34));join('star','lower-point')
