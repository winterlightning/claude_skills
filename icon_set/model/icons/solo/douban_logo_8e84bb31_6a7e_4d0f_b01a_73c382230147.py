"""The 豆 character uses a top rule, a single rectangular mouth, two angled legs and a baseline; filled ribbons reduced to strokes; extremes (8,4)-(40,44)."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8e84bb31-6a7e-4d0f-b01a-73c382230147'
SOURCE_PATH = 'pictographic-primitives/logos/douban logo_8e84bb31-6a7e-4d0f-b01a-73c382230147.svg'
AUTHOR = 'gpt-6'

class DoubanLogo(Solo48):
    icon_id = 'douban-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('douban', 'chinese', 'social', 'logo', 'brand', 'character', 'reviews')

    def build(self):
        # Plan: The 豆 character uses a top rule, a single rectangular mouth, two angled legs and a baseline; filled ribbons reduced to strokes; extremes (8,4)-(40,44).
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

        line('top',(8,4),(40,4))
        poly('mouth',(12,14),(36,14),(36,26),(12,26),closed=True)
        poly('base',(8,44),(18,44),(30,44),(40,44))
        for name,a,b in [('left-leg',(14,34),(18,44)),('right-leg',(34,34),(30,44))]:
            line(name,a,b);join(name,'base')
