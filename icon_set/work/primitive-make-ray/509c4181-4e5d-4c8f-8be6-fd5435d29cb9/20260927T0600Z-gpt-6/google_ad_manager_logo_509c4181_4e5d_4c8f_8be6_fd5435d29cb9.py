"""Three diagonal bars join at alternating ends in a continuous zigzag; collapse outlined capsules to one stroke; extremes (6,6)-(42,42)."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '509c4181-4e5d-4c8f-8be6-fd5435d29cb9'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__google-ad-manager-logo/20260927T055558Z-thuan-mac-1/reference/google ad manager logo_509c4181-4e5d-4c8f-8be6-fd5435d29cb9.svg'
AUTHOR = "gpt-6"

class GoogleAdManagerLogo(Solo48):
    icon_id = 'google-ad-manager-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('google-ad-manager', 'google', 'ads', 'logo', 'brand', 'advertising', 'publisher')

    def build(self):
        # Plan: Three diagonal bars join at alternating ends in a continuous zigzag; collapse outlined capsules to one stroke; extremes (6,6)-(42,42).
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

        for j,(a,b) in enumerate((((6,28),(28,6)),((13,35),(35,13)),((20,42),(42,20)))):
            line(f'bar-{j}',a,b)
