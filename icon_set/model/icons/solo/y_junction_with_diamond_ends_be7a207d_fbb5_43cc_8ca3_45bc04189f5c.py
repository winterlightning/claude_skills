'A Y-shaped connector branches upward into two diagonal arms ending in outlined diamonds. Its short vertical lower stem terminates in a larger circle, with all three shapes left empty.\nPlan: Mirrored upper diamond terminals joined to circular lower terminal. Extrema4,8,44,40.\nConstruction reference: No direct Lucide match; coherent contours, shared attachments and integer extrema.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'be7a207d-fbb5-43cc-8ca3-45bc04189f5c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_09/cable split_be7a207d-fbb5-43cc-8ca3-45bc04189f5c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'y-junction-with-diamond-ends'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('y', 'junction', 'with', 'diamond', 'ends')

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

        for k,x in enumerate((12,36)):poly(f'diamond-{k}',(x,8),(x+8,16),(x,24),(x-8,16),(x,8))
        poly('branch-left',(12,24),(24,28));poly('branch-right',(36,24),(24,28));line('stem',(24,28),(24,30));circle('terminal',24,35,5)
        join('branch-left','diamond-0');join('branch-right','diamond-1');join('branch-left','branch-right');join('branch-left','stem');join('branch-right','stem');join('stem','terminal')
