'A low modem has a long horizontal body with rounded ends and no visible controls. One slim vertical antenna rises from its top near the right side, extending well above the base.\nPlan: Rounded low body and offset mast. Extrema 4,8,44,40; no controls invented.\nConstruction reference: Lucide router original and atomic-debug: rounded base and attached antenna.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ae933efb-f4dd-4755-a5e4-e574a37972ca'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_27/modem_ae933efb-f4dd-4755-a5e4-e574a37972ca.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'single-antenna-modem'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('single', 'antenna', 'modem')

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

        path('base',(10,28),[('L',(34,28)),('L',(38,28)),('A',(44,34),6,6,True),('A',(38,40),6,6,True),('L',(10,40)),('A',(4,34),6,6,True),('A',(10,28),6,6,True)],True)
        line('antenna',(34,8),(34,28));join('base','antenna')
