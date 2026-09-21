'A rounded head covering has a straight forehead band above a wide uncovered face strip. A large curved veil wraps across the lower face and shoulder, with a short internal fold line.\nPlan: Rounded head covering with wide uncovered face strip; preserve veil silhouette, omit tight secondary fold. Extrema8,4,40,44.\nConstruction reference: human_ref/user.svg as head proportion reference; covering and exposed strip from supplied original.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4f15286f-0f07-429b-991b-cb705d4c651c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_05/avatar islamic women niqab 2_4f15286f-0f07-429b-991b-cb705d4c651c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'head-wrapped-in-a-face-veil'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('head', 'wrapped', 'in', 'a', 'face', 'veil')

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

        path('cover',(8,32),[('L',(8,12)),('A',(16,4),8,8,True),('L',(32,4)),('A',(40,12),8,8,True),('L',(40,36)),('L',(40,44)),('C',(8,32),(24,44),(8,42))],True)
        poly('opening',(17,16),(31,16),(31,24),(17,24),(17,16))
        path('wrap',(8,32),[('C',(40,36),(16,36),(28,36))]);join('cover','wrap')
