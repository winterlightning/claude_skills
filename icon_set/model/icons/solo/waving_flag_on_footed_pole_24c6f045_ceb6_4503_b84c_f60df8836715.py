'A broad flag hangs from a tall straight pole and curves in a rolling wave along its upper and lower edges. The pole extends below the cloth to a short horizontal foot.\nPlan: Flag on upright pole; matching rolling cloth edges and right free edge. Flat foot retained. Exact centerline extremes follow the declared SOLO48 keyshape.\nConstruction reference: Lucide flag original and atomic-debug: matching wave curves joined to pole; intentional rightward asymmetry.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '24c6f045-ceb6-4503-b84c-f60df8836715'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_13/country_24c6f045-ceb6-4503-b84c-f60df8836715.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'waving-flag-on-footed-pole'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('waving', 'flag', 'on', 'footed', 'pole')

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

        poly('pole',(8,4),(8,8),(8,28),(8,44))
        path('flag',(8,8),[('C',(24,8),(14,0),(18,8)),('C',(40,8),(30,16),(34,8)),('L',(40,28)),('C',(24,28),(34,36),(30,28)),('C',(8,28),(18,20),(14,28))]);join('flag','pole')
        line('foot',(8,44),(20,44));join('foot','pole')
