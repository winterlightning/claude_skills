'An upper downward chevron and a lower upward chevron mirror one another around an open central gap. Each consists of two long diagonal arms, with the outer ends spread widely apart.\nPlan: Two mirrored chevrons with 8-unit center gap. Exact centerline extremes follow the declared SOLO48 keyshape.\nConstruction reference: Lucide chevrons-down-up original and atomic-debug: mirrored open strokes.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '995eafab-274a-4060-9dee-e2263c318748'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_27/move shrink vertical_995eafab-274a-4060-9dee-e2263c318748.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'chevron-vertical-collapse'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('chevron', 'vertical', 'collapse')

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

        poly('down',(6,6),(24,20),(42,6));poly('up',(6,42),(24,28),(42,42))
