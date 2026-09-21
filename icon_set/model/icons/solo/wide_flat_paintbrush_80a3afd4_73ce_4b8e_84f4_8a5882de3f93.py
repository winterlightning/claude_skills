'A broad flat paintbrush has a slightly tapered bristle block above a horizontal ferrule seam. The lower body curves inward into a narrow handle with a rounded end beneath the brush.\nPlan: Broad brush block and ferrule over narrow rounded handle. Exact centerline extremes follow the declared SOLO48 keyshape.\nConstruction reference: Lucide paintbrush original and atomic-debug: ferrule, broad bristles, rounded handle re-authored upright.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '80a3afd4-73ce-4b8e-84f4-8a5882de3f93'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_29/paint brush_80a3afd4-73ce-4b8e-84f4-8a5882de3f93.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'wide-flat-paintbrush'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('wide', 'flat', 'paintbrush')

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

        path('brush',(8,4),[('L',(40,4)),('L',(38,20)),('L',(38,26)),('C',(30,32),(38,30),(32,30)),('L',(30,38)),('A',(24,44),6,6,True),('A',(18,38),6,6,True),('L',(18,32)),('C',(10,26),(16,30),(10,30)),('L',(10,20)),('L',(8,4))],True)
        line('ferrule',(10,20),(38,20));join('ferrule','brush')
