"""Four card suits in a two-by-two grid: diamond, club, spade and heart. Extrema 6,6,42,42.
Construction: club, spade and heart: continuous outlines with explicit stems
Reduction: Fine lobe curvature simplified to circular/elliptical arcs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6c01ed88-1571-4e62-904d-509e18f64c7d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_10/card game symbols_6c01ed88-1571-4e62-904d-509e18f64c7d.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='four-playing-card-suits'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases=()
    keywords=('four', 'playing', 'card', 'suits')
    def build(self):

        def path(name,start,steps,closed=False):
            here=start;members=[]
            for j,(kind,end,*args) in enumerate(steps):
                m=f'{name}-{j}'
                if kind=='L': self.add_line(m,here,end)
                elif kind=='C': self.add_bezier(m,here,(args[0],args[1],end))
                else:self.add_arc(m,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2],large_arc=args[3] if len(args)>3 else False)
                members.append(m);here=end
            self.add_contour(name,*members,closed=closed)
        def line(n,a,b):self.add_line(n,a,b)
        def poly(n,*pts,closed=False):self.add_polyline(n,*pts,closed=closed)
        def join(a,b):self.relate('connect',a,b)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)

        poly('diamond',(13,6),(20,13),(13,20),(6,13),closed=True)
        path('club',(32,10),[('A',(38,10),3,4,True),('A',(42,15),4,5,True),('A',(35,17),4,4,True),('A',(28,15),4,4,True),('A',(32,10),4,5,True)],True)
        line('club-stem',(35,17),(35,21));join('club-stem','club')
        path('spade',(13,29),[('L',(7,35)),('A',(13,38),4,4,False),('A',(19,35),4,4,False),('L',(13,29))],True)
        line('spade-stem',(13,38),(13,42));join('spade-stem','spade')
        path('heart',(35,32),[('A',(28,33),4,4,False),('L',(35,42)),('L',(42,33)),('A',(35,32),4,4,False)],True)
