'A long rectangular pier deck rests on three thin vertical supports above a curved wave line. The water rises and falls around the posts, with its ends continuing beyond the outer supports.\nPlan: Three supports meet flowing wave at crests; wide deck and equal support pitch. Extrema4,8,44,40.\nConstruction reference: No direct Lucide match; coherent contours, shared attachments and integer extrema.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8475f3a9-46bc-4be6-b0b4-42ca21b37660'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_30/pier_8475f3a9-46bc-4be6-b0b4-42ca21b37660.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-support-pier-waves'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('three', 'support', 'pier', 'waves')

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

        poly('deck',(4,8),(44,8),(44,18),(40,18),(24,18),(8,18),(4,18),(4,8))
        path('water',(4,36),[('C',(8,40),(4,38),(6,40)),('C',(16,36),(12,40),(12,36)),('C',(24,40),(20,36),(20,40)),('C',(32,36),(28,40),(28,36)),('C',(40,40),(36,36),(36,40)),('C',(44,36),(42,40),(44,38))])
        for k,x in enumerate((8,24,40)):
         line(f'post-{k}',(x,18),(x,40));join(f'post-{k}','deck');join(f'post-{k}','water')
