"""Two Kidney Beans.

Two smooth kidney outlines staggered diagonally. Lucide bean informs concave inner edge and coherent convex outside. Centerline extremes (4,8)-(44,40); omit inner seams.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'c8eb6f70-a59a-410a-ab73-429758565aa2'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__two-kidney-beans/20260927T133645Z-thuan-mac-1/reference/kidney bean_c8eb6f70-a59a-410a-ab73-429758565aa2.svg'
AUTHOR = "gpt-6"

class TwoKidneyBeans(Solo48):
    icon_id = 'two-kidney-beans'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
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

        path('upper-bean',(18,10),[('C',(38,8),(24,8),(33,6)),('C',(44,14),(43,8),(44,11)),('C',(22,21),(44,20),(32,23)),('C',(16,16),(17,21),(14,19)),('C',(18,10),(14,13),(16,10))],True)
        path('lower-bean',(10,30),[('C',(30,29),(15,31),(24,28)),('C',(36,35),(35,29),(38,33)),('C',(10,40),(36,41),(17,42)),('C',(4,35),(6,40),(4,38)),('C',(10,30),(4,31),(6,29))],True)
