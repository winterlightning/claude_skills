'A large balloon has a rounded upper body narrowing to a pointed lower neck. A short vertical tether joins the balloon to a small square instrument box hanging directly beneath it.\nPlan: Balloon narrows into neck then tether and box. Exact centerline extremes follow the declared SOLO48 keyshape.\nConstruction reference: Lucide balloon original and atomic-debug: coherent rounded body narrows to tether; source instrument box retained.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd34f9e05-1d1c-4193-a52e-0ad65fcf7005'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_32/radiosonde_d34f9e05-1d1c-4193-a52e-0ad65fcf7005.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'weather-balloon-with-instrument-box'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('weather', 'balloon', 'with', 'instrument', 'box')

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

        path('balloon',(24,4),[('C',(40,16),(34,4),(40,8)),('C',(24,28),(40,24),(28,24)),('C',(8,16),(20,24),(8,24)),('C',(24,4),(8,8),(14,4))],True)
        line('tether',(24,28),(24,36));poly('sensor',(18,36),(24,36),(30,36),(30,44),(18,44),(18,36));join('tether','balloon');join('tether','sensor')
