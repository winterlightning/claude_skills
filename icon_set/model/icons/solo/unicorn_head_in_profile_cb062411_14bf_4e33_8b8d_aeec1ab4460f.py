'A unicorn faces left with a rounded muzzle, pointed ear and a long conical horn divided by a diagonal band. A segmented mane follows the back of its head and long neck.\nPlan: Left-facing unicorn with long horn, raised ear, stepped mane and neck. Extrema8,4,40,44; omit tiny horn bands.\nConstruction reference: No direct Lucide match; coherent contours, shared attachments and integer extrema.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cb062411-14bf-4e33-8b8d-aeec1ab4460f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/video-games/batch-04/fantasy unicorn_cb062411-14bf-4e33-8b8d-aeec1ab4460f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'unicorn-head-in-profile'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('unicorn', 'head', 'in', 'profile')

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

        path('unicorn',(16,18),[('L',(12,4)),('L',(28,16)),('C',(32,8),(28,12),(30,8)),('C',(36,20),(36,8),(36,16)),('C',(40,28),(38,22),(40,24)),('L',(36,32)),('C',(40,40),(36,36),(38,38)),('C',(32,44),(40,42),(36,44)),('L',(16,44)),('C',(20,30),(16,38),(18,34)),('C',(12,32),(18,33),(15,34)),('L',(8,26)),('C',(16,18),(10,22),(12,18))],True)
