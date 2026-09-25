"""An elephant head with a folded ear and a single inward trunk curl; omit the tiny eye and additional spiral turn; extremes (6,6)-(42,42)."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2bff9346-9a7d-4690-95c7-b73e4b8a3944'
SOURCE_PATH = 'pictographic-primitives/logos/evernote logo_2bff9346-9a7d-4690-95c7-b73e4b8a3944.svg'
AUTHOR = 'gpt-6'

class EvernoteLogo(Solo48):
    icon_id = 'evernote-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('evernote', 'notes', 'elephant', 'logo', 'brand', 'productivity', 'memory')

    def build(self):
        # Plan: An elephant head with a folded ear and a single inward trunk curl; omit the tiny eye and additional spiral turn; extremes (6,6)-(42,42).
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

        path('head',(18,6),[('C',(24,12),(22,6),(24,8)),('L',(34,12)),('C',(42,24),(40,12),(42,18)),('L',(42,32)),('A',(32,42),10,10,True),('A',(32,34),4,4,True)])
        path('ear',(24,12),[('L',(24,22)),('C',(16,30),(24,28),(20,30)),('L',(12,36)),('C',(6,18),(6,36),(6,25)),('L',(8,14)),('C',(18,6),(12,10),(12,6))])
        line('fold',(8,14),(14,14));join('head','ear');join('fold','ear')
