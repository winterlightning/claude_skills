'A rounded capsule microphone stands upright on a thin vertical stem and short horizontal foot. Three pairs of grille lines extend inward from the sides, leaving an open strip through the center.\nPlan: Microphone capsule with paired grille slots reduced to two rows; central stand and foot. Exact centerline extremes follow the declared SOLO48 keyshape.\nConstruction reference: Lucide mic original and atomic-debug: capsule and central stem; source paired side grilles retained.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '40a82f8e-607c-4a5c-9bd8-2c7172dbb654'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_27/microphone podcast on air_40a82f8e-607c-4a5c-9bd8-2c7172dbb654.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'standing-studio-microphone'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('standing', 'studio', 'microphone')

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

        path('mic',(12,12),[('A',(20,4),8,8,True),('L',(28,4)),('A',(36,12),8,8,True),('L',(36,20)),('A',(28,28),8,8,True),('L',(24,28)),('L',(20,28)),('A',(12,20),8,8,True),('L',(12,12))],True)
        for y in (12,20):
         line('left'+str(y),(12,y),(18,y));line('right'+str(y),(30,y),(36,y));join('left'+str(y),'mic');join('right'+str(y),'mic')
        line('stand',(24,28),(24,44));poly('foot',(8,44),(24,44),(40,44));join('stand','mic');join('stand','foot')
