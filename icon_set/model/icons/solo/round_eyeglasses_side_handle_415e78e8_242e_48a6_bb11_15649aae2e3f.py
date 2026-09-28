'Two large circular eyeglass lenses are joined by a small arched bridge. A slim handle begins at the right lens edge, curves outward, and descends vertically below the round frames.\nPlan: Equal circular glasses joined by arch; side handle descends to lower edge. Exact centerline extremes follow the declared SOLO48 keyshape.\nConstruction reference: Lucide glasses original and atomic-debug: equal paired circles and joined bridge; preserve source side handle.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '415e78e8-242e-48a6-bb11-15649aae2e3f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_30/pince nez_415e78e8-242e-48a6-bb11-15649aae2e3f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'round-eyeglasses-side-handle'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('round', 'eyeglasses', 'side', 'handle')

    # Repair: Raise equal lenses to the exact top envelope; keep the side handle descending to40.
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

        circle('left',12,16,8);circle('right',36,16,8)
        path('bridge',(20,16),[('A',(28,16),4,4,True)]);join('bridge','left');join('bridge','right')
        path('handle',(44,16),[('L',(44,40))]);join('handle','right')
