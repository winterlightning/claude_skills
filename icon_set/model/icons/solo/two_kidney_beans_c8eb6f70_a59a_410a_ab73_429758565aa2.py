"""Two Kidney Beans.

Two smooth kidney outlines staggered diagonally. Lucide bean informs concave inner edge and coherent convex outside. Centerline extremes (4,8)-(44,40); omit inner seams.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c8eb6f70-a59a-410a-ab73-429758565aa2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/kidney bean_c8eb6f70-a59a-410a-ab73-429758565aa2.svg'
AUTHOR = 'gpt-6'

class TwoKidneyBeans(Solo48):
    icon_id = 'two-kidney-beans'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('two', 'kidney', 'beans')

    def build(self):
        # Symbol plan: Two smooth kidney outlines staggered diagonally. Lucide bean informs concave inner edge and coherent convex outside. Centerline extremes (4,8)-(44,40); omit inner seams.

        def path(name, start, commands, closed=False):
            members=[]
            for i, command in enumerate(commands):
                kind,end,*args=command
                member=f'{name}-{i}'
                if kind=='L': self.add_line(member,start,end)
                elif kind=='A': self.add_arc(member,start,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(member,start,(args[0],args[1],end))
                members.append(member)
                start=end
            self.add_contour(name,*members,closed=closed)
        def oval(name,x,y,rx,ry):
            path(name,(x-rx,y),[('A',(x+rx,y),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
        def box(name,l,t,r,b,rad=4):
            path(name,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line=self.add_line
        dot=self.add_dot
        join=lambda a,b:self.relate('connect',a,b)

        path('upper-bean',(18,10),[('C',(38,8),(24,13),(33,8)),('C',(44,14),(42,8),(44,10)),('C',(22,20),(44,19),(32,20)),('C',(16,16),(18,20),(16,19)),('C',(18,10),(16,13),(16,11))],True)
        path('lower-bean',(10,30),[('C',(30,30),(16,32),(25,30)),('C',(36,35),(34,30),(36,32)),('C',(10,40),(36,40),(18,40)),('C',(4,35),(6,40),(4,38)),('C',(10,30),(4,31),(6,29))],True)
