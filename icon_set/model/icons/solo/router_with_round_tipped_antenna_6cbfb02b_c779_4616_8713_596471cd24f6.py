'A low rounded rectangular router body supports a single thin vertical antenna at its center. The antenna ends in a small circle, and the device body has no visible ports or lights.\nPlan: Central hollow antenna tip, stem and rounded low base; extrema4,8,44,40.\nConstruction reference: Lucide router: capsule base and thin antenna; reference hollow tip preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6cbfb02b-c779-4616-8713-596471cd24f6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_33/router_6cbfb02b-c779-4616-8713-596471cd24f6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'router-with-round-tipped-antenna'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('router', 'with', 'round', 'tipped', 'antenna')

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

        circle('tip',24,14,6);line('antenna',(24,20),(24,30))
        path('base',(9,30),[('L',(24,30)),('L',(39,30)),('A',(44,35),5,5,True),('A',(39,40),5,5,True),('L',(9,40)),('A',(4,35),5,5,True),('A',(9,30),5,5,True)],True)
        join('tip','antenna');join('antenna','base')
