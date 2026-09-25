"""Nested speech bubbles with the outer lower-left square corner and an inner short tail; enlarge the clear band and omit no identifying part; extremes (6,6)-(42,42)."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2726c4b1-9add-4579-a65d-2fb65d203a2b'
SOURCE_PATH = 'pictographic-primitives/logos/discourse logo_2726c4b1-9add-4579-a65d-2fb65d203a2b.svg'
AUTHOR = 'gpt-6'

class DiscourseLogo(Solo48):
    icon_id = 'discourse-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('discourse', 'forum', 'chat', 'logo', 'brand', 'community', 'discussion')

    def build(self):
        # Plan: Nested speech bubbles with the outer lower-left square corner and an inner short tail; enlarge the clear band and omit no identifying part; extremes (6,6)-(42,42).
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

        path('outer',(6,42),[('L',(6,24)),('A',(24,6),18,18,True),('A',(42,24),18,18,True),('A',(24,42),18,18,True),('L',(6,42))],True)
        path('inner',(17,29),[('C',(24,15),(13,23),(17,15)),('C',(24,33),(36,15),(36,33)),('C',(19,32),(21,33),(20,32)),('L',(15,33)),('L',(17,29))],True)
