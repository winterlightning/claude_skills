'Three upright fence pickets have pointed tops and straight sides standing on a common baseline. Two horizontal rails run behind the posts, extending slightly beyond the outer pickets at both ends.\nPlan: Three equal pickets width8 on16-unit pitch, with two rails and baseline. Extrema4,8,44,40.\nConstruction reference: Lucide fence original and atomic-debug: repeated pickets and occluded rail spans.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e2030a38-a176-4af8-9e84-4f002fbb7769'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_30/pigpen_e2030a38-a176-4af8-9e84-4f002fbb7769.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-post-picket-fence'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('three', 'post', 'picket', 'fence')

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

        for k in range(3):
         x=4+16*k
         poly(f'post-{k}',(x+4,8),(x+8,14),(x+8,24),(x+8,32),(x+8,40),(x,40),(x,32),(x,24),(x,14),(x+4,8))
        for k in range(2):
         for y in (24,32,40):
          name=f'rail-{k}-{y}';line(name,(12+16*k,y),(20+16*k,y));join(name,f'post-{k}');join(name,f'post-{k+1}')
