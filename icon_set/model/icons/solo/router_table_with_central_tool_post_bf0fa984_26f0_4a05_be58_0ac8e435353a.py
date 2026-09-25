'A worktable has a broad rounded top, two outward-slanting legs, and a horizontal cross brace. A short narrow tool post rises vertically from the center of the tabletop.\nPlan: Capsule tabletop, central cutter, splayed legs and shared crossbrace. Extrema4,8,44,40.\nConstruction reference: No direct Lucide match; coherent contours, shared attachments and integer extrema.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bf0fa984-26f0-4a05-be58-0ac8e435353a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_33/router table_bf0fa984-26f0-4a05-be58-0ac8e435353a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'router-table-with-central-tool-post'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('router', 'table', 'with', 'central', 'tool', 'post')

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

        path('top',(8,16),[('L',(24,16)),('L',(40,16)),('A',(44,20),4,4,True),('A',(40,24),4,4,True),('L',(36,24)),('L',(12,24)),('L',(8,24)),('A',(4,20),4,4,True),('A',(8,16),4,4,True)],True)
        line('tool',(24,8),(24,16));join('tool','top')
        poly('left-leg',(12,24),(10,32),(8,40));poly('right-leg',(36,24),(38,32),(40,40));line('brace',(10,32),(38,32))
        for leg in ('left-leg','right-leg'):join(leg,'top');join(leg,'brace')
