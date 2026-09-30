"""The rejected schedule uses short solid dashes instead of outlined task bars. Restore rounded outlined tasks in a staggered layout.
Plan: HRECT_L exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: Lucide list-todo: distinct outlined task enclosures and repeated rows.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='9b62564b-146e-40a6-b154-9dc3b0f68747'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__rounded-staggered-task-bars/20260929T141751Z-thuan-mac/reference/workflow gantt chart_9b62564b-146e-40a6-b154-9dc3b0f68747.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='rounded-staggered-task-bars'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('rounded', 'staggered', 'task', 'bars')
    def build(self):

        def path(n,start,steps,closed=False):
            members=[];here=start
            for j,(kind,end,*args) in enumerate(steps):
                m=f'{n}-{j}'
                if kind=='L':self.add_line(m,here,end)
                elif kind=='A':self.add_arc(m,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C':self.add_bezier(m,here,(args[0],args[1],end))
                members.append(m);here=end
            self.add_contour(n,*members,closed=closed)
        def oval(n,x,y,rx,ry):path(n,(x-rx,y),[('A',(x+rx,y),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
        def box(n,l,t,r,b,rad=0):
            if not rad:self.add_polyline(n,(l,t),(r,t),(r,b),(l,b),closed=True);return
            path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        box('task-top',4,8,20,16,3)
        box('task-middle',28,20,44,28,3)
        box('task-bottom',4,32,20,40,3)
