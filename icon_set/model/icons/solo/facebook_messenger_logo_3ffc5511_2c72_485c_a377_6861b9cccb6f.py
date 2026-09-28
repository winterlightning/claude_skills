"""A rounded speech bubble with a lower-left tail enclosing a lightning zigzag; collapse the filled bolt to its central stroke; extremes (6,6)-(42,42)."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3ffc5511-2c72-485c-a377-6861b9cccb6f'
SOURCE_PATH = 'pictographic-primitives/logos/facbook messenger logo_3ffc5511-2c72-485c-a377-6861b9cccb6f.svg'
AUTHOR = 'gpt-6'

class FacebookMessengerLogo(Solo48):
    icon_id = 'facebook-messenger-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('messenger', 'facebook', 'chat', 'lightning', 'logo', 'brand', 'messaging')

    def build(self):
        # Plan: A rounded speech bubble with a lower-left tail enclosing a lightning zigzag; collapse the filled bolt to its central stroke; extremes (6,6)-(42,42).
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

        path('bubble',(10,34),[('C',(6,23),(7,31),(6,27)),('C',(24,6),(6,13),(14,6)),('C',(42,23),(34,6),(42,13)),('C',(20,37),(42,34),(32,40)),('L',(10,42)),('L',(10,34))],True)
        poly('bolt',(16,28),(21,22),(27,26),(32,20))
