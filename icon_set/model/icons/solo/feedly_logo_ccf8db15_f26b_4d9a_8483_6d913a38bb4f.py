"""A rounded diamond with two descending diagonal bars; remove the smallest square and collapse outlined bars to strokes for clearance; extremes (6,6)-(42,42)."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ccf8db15-f26b-4d9a-8483-6d913a38bb4f'
SOURCE_PATH = 'pictographic-primitives/logos/feedly logo_ccf8db15-f26b-4d9a-8483-6d913a38bb4f.svg'
AUTHOR = 'gpt-6'

class FeedlyLogo(Solo48):
    icon_id = 'feedly-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('feedly', 'rss', 'news-reader', 'logo', 'brand', 'feed', 'reading')

    def build(self):
        # Plan: A rounded diamond with two descending diagonal bars; remove the smallest square and collapse outlined bars to strokes for clearance; extremes (6,6)-(42,42).
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

        path('diamond',(24,6),[('C',(42,24),(28,6),(42,20)),('C',(24,42),(42,28),(28,42)),('C',(6,24),(20,42),(6,28)),('C',(24,6),(6,20),(20,6))],True)
        line('long',(16,24),(24,16));line('short',(25,30),(30,25))
