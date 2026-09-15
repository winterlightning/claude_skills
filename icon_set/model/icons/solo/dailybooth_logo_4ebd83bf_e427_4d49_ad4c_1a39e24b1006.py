"""Speech-bubble roundel enclosing a reduced camera and lens; rounded camera shoulder owns the lens spacing; extremes (6,6)-(42,42)."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4ebd83bf-e427-4d49-ad4c-1a39e24b1006'
SOURCE_PATH = 'pictographic-primitives/logos/dailybooth logo_4ebd83bf-e427-4d49-ad4c-1a39e24b1006.svg'
AUTHOR = 'gpt-6'

class DailyboothLogo(Solo48):
    icon_id = 'dailybooth-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'brands/logos'
    aliases = ()
    keywords = ('dailybooth', 'camera', 'photo', 'logo', 'brand', 'social', 'speech-bubble')

    def build(self):
        # Plan: Speech-bubble roundel enclosing a reduced camera and lens; rounded camera shoulder owns the lens spacing; extremes (6,6)-(42,42).
        # Construction reference: No useful subject match found; source brand render informs the geometry.

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

        path('bubble',(36,34),[('L',(42,42)),('L',(31,38)),('C',(6,24),(17,46),(6,36)),('A',(42,24),18,18,True),('C',(36,34),(42,28),(40,32))],True)
        poly('camera',(14,19),(20,19),(20,16),(28,16),(28,19),(34,19),(34,31),(14,31),closed=True)
        circle('lens',24,25,3)
