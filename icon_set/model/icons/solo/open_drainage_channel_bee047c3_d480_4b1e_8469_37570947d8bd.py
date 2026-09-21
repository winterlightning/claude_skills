'A short drainage channel has two thick raised sidewalls and a recessed center. Its rounded front cross-section forms a broad U, with a straight rear edge across the opening.\nPlan: Recessed U-channel and thick raised walls; back edge spans the channel. Exact centerline extremes follow the declared SOLO48 keyshape.\nConstruction reference: No useful direct Lucide match; coherent contours reconstructed from the inspected original.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bee047c3-d480-4b1e-8469-37570947d8bd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_09/canal_bee047c3-d480-4b1e-8469-37570947d8bd.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'open-drainage-channel'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('open', 'drainage', 'channel')

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

        path('outer',(4,28),[('L',(8,8)),('L',(16,8)),('L',(16,24)),('A',(20,28),4,4,False),('L',(28,28)),('A',(32,24),4,4,False),('L',(32,8)),('L',(40,8)),('L',(44,28)),('A',(32,40),12,12,True),('L',(16,40)),('A',(4,28),12,12,True)],True)
        line('back',(16,16),(32,16));join('back','outer')
