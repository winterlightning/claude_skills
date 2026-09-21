'A broad rounded rectangle is divided by one vertical wavy line running from its top edge to its bottom. The alternating curves leave two blank compartments on either side of the membrane.\nPlan: Broad rounded rectangle and a vertical wavy partition. Exact centerline extremes follow the declared SOLO48 keyshape.\nConstruction reference: No useful direct Lucide match; coherent contours reconstructed from the inspected original.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a1962559-d93e-43c5-98ad-a88a258bda65'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_27/membrane_a1962559-d93e-43c5-98ad-a88a258bda65.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'wavy-membrane-partition'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('wavy', 'membrane', 'partition')

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

        path('case',(24,8),[('L',(38,8)),('A',(44,14),6,6,True),('L',(44,34)),('A',(38,40),6,6,True),('L',(24,40)),('L',(10,40)),('A',(4,34),6,6,True),('L',(4,14)),('A',(10,8),6,6,True),('L',(24,8))],True)
        path('membrane',(24,8),[('C',(24,24),(12,16),(36,16)),('C',(24,40),(12,32),(36,32))]);join('membrane','case')
