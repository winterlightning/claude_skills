"""Two lowercase f letters share a continuous crossbar; mirrored hook construction uses a common radius and height; extremes (6,6)-(42,42)."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '79d295a8-2157-4f52-9b06-68c96f5a3f64'
SOURCE_PATH = 'pictographic-primitives/logos/friends feed logo_79d295a8-2157-4f52-9b06-68c96f5a3f64.svg'
AUTHOR = 'gpt-6'

class FriendfeedLogo(Solo48):
    icon_id = 'friendfeed-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'brands/logos'
    aliases = ()
    keywords = ('friendfeed', 'letters', 'ff', 'logo', 'brand', 'social', 'feed')

    def build(self):
        # Plan: Two lowercase f letters share a continuous crossbar; mirrored hook construction uses a common radius and height; extremes (6,6)-(42,42).
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

        for i,x in enumerate((14,32)):
         path(f'f-{i}',(x,42),[('L',(x,24)),('L',(x,14)),('A',(x+8,6),8,8,True),('L',(x+10,6))])
        poly('bar',(6,24),(14,24),(32,24),(42,24));join('bar','f-0');join('bar','f-1')
