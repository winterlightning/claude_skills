"""An oval conversation bubble with a right tail, smiling curve and one signal arc; drop the second signal arc to keep open bands; extremes (6,6)-(42,42)."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b487014a-f989-4b16-9553-bd6f31c178b7'
SOURCE_PATH = 'pictographic-primitives/logos/formspring logo_b487014a-f989-4b16-9553-bd6f31c178b7.svg'
AUTHOR = 'gpt-6'

class FormspringLogo(Solo48):
    icon_id = 'formspring-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('formspring', 'questions', 'chat', 'logo', 'brand', 'social', 'speech-bubble')

    def build(self):
        # Plan: An oval conversation bubble with a right tail, smiling curve and one signal arc; drop the second signal arc to keep open bands; extremes (6,6)-(42,42).
        # Construction reference: Lucide message-circle original and atomic-debug: coherent bubble contour with a tail.

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

        path('bubble',(38,25),[('C',(22,16),(36,18),(30,16)),('C',(6,29),(12,16),(6,22)),('C',(30,39),(6,40),(22,42)),('L',(42,42)),('L',(38,33)),('C',(38,25),(40,30),(40,28))],True)
        path('smile',(16,26),[('C',(38,25),(24,33),(32,32))]);join('smile','bubble')
        path('signal',(24,6),[('C',(42,12),(30,6),(38,7))])
