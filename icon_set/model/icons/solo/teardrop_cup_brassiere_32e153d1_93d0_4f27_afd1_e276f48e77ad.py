'A brassiere has two deep teardrop shaped cups joined by a short central bridge. Thin vertical shoulder straps rise from the outer tops, framing the open space between them.\nPlan: Mirrored teardrop cups with shared bridge and outer straps. Extrema4,8,44,40.\nConstruction reference: No direct Lucide match; coherent contours, shared attachments and integer extrema.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '32e153d1-93d0-4f27-afd1-e276f48e77ad'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_08/brassiere_32e153d1-93d0-4f27-afd1-e276f48e77ad.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'teardrop-cup-brassiere'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('teardrop', 'cup', 'brassiere')

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

        for k in range(2):
         def p(x,y):return (x if k==0 else 48-x,y)
         path(f'cup-{k}',p(4,20),[('C',p(20,30),p(4,23),p(20,22)),('A',p(12,40),8,10,k==0),('A',p(4,30),8,10,k==0),('L',p(4,20))],True)
         line(f'strap-{k}',p(4,8),p(4,20));join(f'cup-{k}',f'strap-{k}')
        line('bridge',(20,30),(28,30));join('bridge','cup-0');join('bridge','cup-1')
