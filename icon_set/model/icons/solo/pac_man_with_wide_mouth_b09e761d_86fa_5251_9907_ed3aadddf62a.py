'A round Pac-Man silhouette faces right with a broad open wedge forming its mouth. The remaining outer edge is a smooth continuous circular arc, with no visible eye detail.\nPlan: Circular silhouette with wide open right wedge. Radius20 centered24,24; no eye invented.\nConstruction reference: No direct Lucide match; coherent contours, shared attachments and integer extrema.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b09e761d-86fa-5251-9907-ed3aadddf62a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/video-games/batch-08/pacman enemy_b09e761d-86fa-5251-9907-ed3aadddf62a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'pac-man-with-wide-mouth'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    aliases = ()
    keywords = ('pac', 'man', 'with', 'wide', 'mouth')

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

        path('outline',(40,12),[('A',(24,4),20,20,False),('A',(4,24),20,20,False),('A',(24,44),20,20,False),('A',(40,36),20,20,False),('L',(24,24)),('L',(40,12))],True)
