'A front-facing camera has a broad rounded rectangular body and a raised central top housing. A large circular lens fills the middle, with a short curved reflection inside its upper-left area.\nPlan: Rounded camera body with raised top and circular lens. Omit tiny lens reflection. Extrema4,8,44,40.\nConstruction reference: Lucide camera original/atomic-debug: raised camera housing and centered circular lens.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '95d8e371-24a9-5895-a4f6-2dbac73081e4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/video/camera_95d8e371-24a9-5895-a4f6-2dbac73081e4.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'digital-camera'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video'
    categories = ('video', 'primitives')
    aliases = ()
    keywords = ('digital', 'camera')

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

        path('body',(8,16),[('L',(12,16)),('L',(16,8)),('L',(32,8)),('L',(36,16)),('L',(40,16)),('A',(44,20),4,4,True),('L',(44,36)),('A',(40,40),4,4,True),('L',(8,40)),('A',(4,36),4,4,True),('L',(4,20)),('A',(8,16),4,4,True)],True)
        circle('lens',24,25,6)
