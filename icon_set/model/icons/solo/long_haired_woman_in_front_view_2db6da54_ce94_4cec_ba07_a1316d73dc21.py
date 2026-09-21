'A woman faces forward with a blank face framed by shoulder-length hair and a swept side part. Her neck descends into a V-shaped neckline between two broad curved shoulders.\nPlan: Front portrait with circular jaw, swept fringe and long hair, curved shoulders. Jaw bottom28 and body top32 touch in ink. Extrema8,4,40,44.\nConstruction reference: human_ref/user.svg: circular face and curved shoulders; hair from supplied original.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2db6da54-ce94-4cec-ba07-a1316d73dc21'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_34/sister in law_2db6da54-ce94-4cec-ba07-a1316d73dc21.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'long-haired-woman-in-front-view'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('long', 'haired', 'woman', 'in', 'front', 'view')

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

        path('hair',(8,44),[('L',(8,20)),('A',(24,4),16,16,True),('A',(40,20),16,16,True),('L',(40,44))])
        self.add_arc('jaw',(16,18),(32,18),radius_x=8,radius_y=8,sweep=False)
        path('fringe',(16,18),[('C',(27,13),(22,18),(24,16)),('C',(32,18),(28,16),(30,18))]);join('jaw','fringe')
        self.add_arc('body-top',(8,44),(40,44),radius_x=16,radius_y=14,sweep=True);self.add_contour('body','body-top');join('jaw','body');join('hair','body')
