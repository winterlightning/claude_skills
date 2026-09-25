'A central circular head sits above rounded shoulders, with three smaller circular nodes fanning out above it. Short stems point inward from the upper and diagonal nodes toward the central person.\nPlan: Three workflow nodes fan above circular head with touching curved shoulders. Head cy29 r5, shoulder top38 means zero ink gap. Extrema8,4,40,44.\nConstruction reference: human_ref/user.svg: circular head and touching curved shoulders; connected-node diagram retained as one scene.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a28f5661-8e5c-4ffc-a1ac-67855b123cbd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/work/workflow manager male_a28f5661-8e5c-4ffc-a1ac-67855b123cbd.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'person-with-branching-workflow-nodes'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'work'
    categories = ('work', 'primitives')
    aliases = ()
    keywords = ('person', 'with', 'branching', 'workflow', 'nodes')

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
            if name in ('face','head'):
                self.add_arc('head-top',(x-r,y),(x+r,y),radius_x=r,radius_y=r,sweep=True)
                self.add_arc('head-bottom',(x+r,y),(x-r,y),radius_x=r,radius_y=r,sweep=True)
                self.add_contour(name,'head-top','head-bottom',closed=True)
            else:
                path(name,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def line(name,a,b):self.add_line(name,a,b)
        def poly(name,*points):self.add_polyline(name,*points,closed=points[0]==points[-1])
        def join(a,b):self.relate('connect',a,b)
        def box(name,l,t,r,b,rad=4):
            path(name,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        def oval(name,x,y,rx,ry):
            path(name,(x-rx,y),[('A',(x,y-ry),rx,ry,True),('A',(x+rx,y),rx,ry,True),('A',(x,y+ry),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)

        circle('head',24,29,5)
        self.add_arc('body-top',(8,44),(40,44),radius_x=16,radius_y=6,sweep=True);self.add_contour('body','body-top');join('head','body')
        circle('top-node',24,7,3);line('top-stem',(24,10),(24,16));join('top-node','top-stem')
        for k in range(2):
         x=11 if k==0 else 37;end=(15,19) if k==0 else (33,19)
         circle(f'node-{k}',x,18,3);line(f'stem-{k}',(14 if k==0 else 34,18),end);join(f'node-{k}',f'stem-{k}')
