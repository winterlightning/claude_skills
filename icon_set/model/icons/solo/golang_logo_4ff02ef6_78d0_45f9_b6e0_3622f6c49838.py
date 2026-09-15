"""The rounded letters GO with a short speed line attached to the G; simplify bold ribbons to open strokes; extremes (4,8)-(44,40)."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4ff02ef6-78d0-45f9-b6e0-3622f6c49838'
SOURCE_PATH = 'pictographic-primitives/logos/golang logo_4ff02ef6-78d0-45f9-b6e0-3622f6c49838.svg'
AUTHOR = 'gpt-6'

class GolangLogo(Solo48):
    icon_id = 'golang-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'brands/logos'
    aliases = ()
    keywords = ('go', 'golang', 'programming', 'language', 'logo', 'brand', 'developer')

    def build(self):
        # Plan: The rounded letters GO with a short speed line attached to the G; simplify bold ribbons to open strokes; extremes (4,8)-(44,40).
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

        path('g',(22,12),[('C',(10,24),(10,2),(10,16)),('C',(22,36),(10,32),(10,42)),('L',(22,26)),('L',(17,26))])
        path('o',(38,8),[('A',(44,14),6,6,True),('L',(44,34)),('A',(38,40),6,6,True),('A',(32,34),6,6,True),('L',(32,14)),('A',(38,8),6,6,True)],True)
        line('speed',(4,24),(10,24));join('speed','g')
