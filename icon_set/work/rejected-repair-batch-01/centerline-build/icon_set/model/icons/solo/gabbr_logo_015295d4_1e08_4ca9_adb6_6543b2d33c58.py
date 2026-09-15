"""A curved diagonal telephone receiver with one signal arc; omit the two inner signal arcs and widen the receiver opening; extremes (6,6)-(42,42)."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '015295d4-1e08-4ca9-adb6-6543b2d33c58'
SOURCE_PATH = 'pictographic-primitives/logos/gabbr logo_015295d4-1e08-4ca9-adb6-6543b2d33c58.svg'
AUTHOR = 'gpt-6'

class GabbrLogo(Solo48):
    icon_id = 'gabbr-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'brands/logos'
    aliases = ()
    keywords = ('gabbr', 'phone', 'call', 'logo', 'brand', 'chat', 'signal')

    def build(self):
        # Plan: A curved diagonal telephone receiver with one signal arc; omit the two inner signal arcs and widen the receiver opening; extremes (6,6)-(42,42).
        # Construction reference: Lucide phone-call original and atomic-debug: coherent receiver and concentric signal arcs.

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

        path('receiver',(6,16),[('L',(12,12)),('L',(20,20)),('L',(18,24)),('C',(28,34),(21,28),(25,32)),('L',(32,30)),('L',(40,36)),('C',(32,42),(40,40),(36,42)),('C',(6,16),(14,42),(6,34))],True)
        self.add_arc('signal',(22,6),(42,26),radius_x=20,sweep=True)
