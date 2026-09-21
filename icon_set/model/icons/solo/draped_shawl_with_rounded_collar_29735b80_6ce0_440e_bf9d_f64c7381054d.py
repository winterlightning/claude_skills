'A shawl wraps around a rounded neck opening with a broad curved collar across the front. Two long side panels hang below the collar, separated by an open central space.\nPlan: Rounded collar nested over two long open shawl panels.\nConstruction reference: No useful direct Lucide match; reconstructed from the inspected original silhouette.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '29735b80-6ce0-440e-bf9d-f64c7381054d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_34/shawl_29735b80-6ce0-440e-bf9d-f64c7381054d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'draped-shawl-with-rounded-collar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('draped', 'shawl', 'with', 'rounded', 'collar')

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

        path('collar',(12,12),[('A',(36,12),12,8,True),('C',(24,28),(36,24),(30,28)),('C',(12,12),(18,28),(12,24))],True)
        poly('left',(12,20),(8,40),(18,44),(18,36));poly('right',(36,20),(40,40),(30,44),(30,36));join('left','collar');join('right','collar')
