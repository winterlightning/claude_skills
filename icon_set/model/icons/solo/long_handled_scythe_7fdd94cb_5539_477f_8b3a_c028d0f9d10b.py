'A long narrow handle leans slightly right as it rises into a broad curved blade. The blade sweeps downward to a sharp right-facing tip, with a second curve marking its lower cutting edge.\nPlan: Long handle supports crescent scythe blade; blade deliberately asymmetric.\nConstruction reference: No useful direct Lucide match; reconstructed from the inspected original silhouette.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7fdd94cb-5539-477f-8b3a-c028d0f9d10b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_33/scythe_7fdd94cb-5539-477f-8b3a-c028d0f9d10b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'long-handled-scythe'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('long', 'handled', 'scythe')

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

        path('blade',(10,6),[('C',(42,24),(24,6),(38,10)),('C',(10,14),(32,16),(22,14)),('L',(10,6))],True)
        line('handle',(10,14),(6,42));join('blade','handle')
