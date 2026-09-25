"""Two parallel rising bars with a ring at the left foot; simplify the capsule outlines into strokes; extremes (6,6)-(42,42)."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'cb4a347a-90c5-4a94-9367-96c25f1dd78e'
SOURCE_PATH = 'pictographic-primitives/logos/google adsense logo_cb4a347a-90c5-4a94-9367-96c25f1dd78e.svg'
AUTHOR = 'gpt-6'

class GoogleAdsenseLogo(Solo48):
    icon_id = 'google-adsense-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('google-adsense', 'google', 'ads', 'logo', 'brand', 'publisher', 'revenue')

    def build(self):
        # Plan: Two parallel rising bars with a ring at the left foot; simplify the capsule outlines into strokes; extremes (6,6)-(42,42).
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

        circle('foot',10,38,4)
        line('left',(14,38),(30,6));join('foot','left')
        line('right',(28,42),(42,14))
