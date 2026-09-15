"""An asymmetric smiling face with two upright eyes at the upper right; simplify oval eye outlines to paired strokes; extremes (6,6)-(42,42)."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '36bf3822-ed4c-4244-b8c9-ba07bcdae2f1'
SOURCE_PATH = 'pictographic-primitives/logos/friend star logo_36bf3822-ed4c-4244-b8c9-ba07bcdae2f1.svg'
AUTHOR = 'gpt-6'

class FriendstarLogo(Solo48):
    icon_id = 'friendstar-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'brands/logos'
    aliases = ()
    keywords = ('friendstar', 'smile', 'face', 'logo', 'brand', 'social', 'network')

    def build(self):
        # Plan: An asymmetric smiling face with two upright eyes at the upper right; simplify oval eye outlines to paired strokes; extremes (6,6)-(42,42).
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

        path('smile',(6,29),[('C',(24,42),(9,38),(16,42)),('C',(42,25),(34,42),(40,32))])
        for i,(x,y) in enumerate(((24,10),(36,6))):line(f'eye-{i}',(x,y),(x,y+8))
