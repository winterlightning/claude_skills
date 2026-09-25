"""One large ring at upper left with three smaller marks trailing down and right; preserve the unequal hierarchy and open gaps; the smallest ring becomes a dot; extremes (6,6)-(42,42)."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9bb2f039-3eaa-4462-836f-2ecb877e1a0e'
SOURCE_PATH = 'pictographic-primitives/logos/google assistant logo_9bb2f039-3eaa-4462-836f-2ecb877e1a0e.svg'
AUTHOR = 'gpt-6'

class GoogleAssistantLogo(Solo48):
    icon_id = 'google-assistant-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('google-assistant', 'google', 'assistant', 'voice', 'logo', 'brand', 'ai')

    def build(self):
        # Plan: One large ring at upper left with three smaller marks trailing down and right; preserve the unequal hierarchy and open gaps; the smallest ring becomes a dot; extremes (6,6)-(42,42).
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

        circle('large',16,16,10)
        circle('right',39,20,3)
        self.add_dot('middle',(30,29))
        circle('bottom',30,40,2)
