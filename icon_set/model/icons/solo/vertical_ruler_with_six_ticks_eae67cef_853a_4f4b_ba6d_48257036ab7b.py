'A tall narrow ruler has a rectangular body and six short horizontal ticks extending inward from its left edge. Its right side remains plain, and no measurement numbers are visible.\nPlan: Upright ruler with four ticks; reduce six divisions to four so spacing survives at48. Exact centerline extremes follow the declared SOLO48 keyshape.\nConstruction reference: Lucide ruler original and atomic-debug: attached ticks and coherent rectangular outline.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'eae67cef-853a-4f4b-ba6d-48257036ab7b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_33/ruler vertical_eae67cef-853a-4f4b-ba6d-48257036ab7b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'vertical-ruler-with-six-ticks'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('vertical', 'ruler', 'with', 'six', 'ticks')

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
        def box(name,l,t,r,b,rad=4):
            path(name,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        def oval(name,x,y,rx,ry):
            path(name,(x-rx,y),[('A',(x,y-ry),rx,ry,True),('A',(x+rx,y),rx,ry,True),('A',(x,y+ry),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)

        poly('body',(10,4),(38,4),(38,44),(10,44),(10,36),(10,28),(10,20),(10,12),(10,4))
        for j,y in enumerate((12,20,28,36)):
         line('tick-'+str(j),(10,y),(24 if j%2==0 else 20,y));join('body','tick-'+str(j))
