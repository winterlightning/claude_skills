'A tornado narrows from a broad oval top through a descending series of curved bands. Beneath it, a tilted map panel contains a winding track and two short dashed marks.\nPlan: Tornado bands float above a trapezoidal tracking map; no invented text.\nConstruction reference: Lucide wind original and atomic-debug: separated round-ended wind bands.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8c091acf-5d0d-4887-9ed1-429a36bf8b0a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_28/natural disaster hurricane map_8c091acf-5d0d-4887-9ed1-429a36bf8b0a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'tornado-over-tracking-map'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('tornado', 'over', 'tracking', 'map')

    def build(self):

        def path(name,start,steps,closed=False):
            here=start; members=[]
            for j,(kind,end,*args) in enumerate(steps):
                member=f'{name}-{j}'
                if kind=='L':self.add_line(member,here,end)
                elif kind=='A':self.add_arc(member,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C':self.add_bezier(member,here,(args[0],args[1],end))
                here=end;members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def line(name,a,b):self.add_line(name,a,b)
        def poly(name,*points):self.add_polyline(name,*points,closed=points[0]==points[-1])
        def join(a,b):self.relate('connect',a,b)

        line('wind-1',(10,6),(38,6));line('wind-2',(16,14),(32,14));line('wind-3',(22,22),(26,22))
        poly('map',(14,30),(6,42),(42,42),(34,30))
