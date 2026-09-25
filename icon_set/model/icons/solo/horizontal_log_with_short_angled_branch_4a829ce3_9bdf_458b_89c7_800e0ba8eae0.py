'A horizontal log has an oval cut face on the left and a long rounded body extending right. A short squared branch stub rises diagonally from the upper middle of the trunk.\nPlan: Oval cut end with shared trunk attachments and diagonal branch stub. Extrema4,8,44,40.\nConstruction reference: No direct Lucide match; coherent contours, shared attachments and integer extrema.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4a829ce3-9bdf-458b-89c7-800e0ba8eae0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_26/log_4a829ce3-9bdf-458b-89c7-800e0ba8eae0.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'horizontal-log-with-short-angled-branch'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('horizontal', 'log', 'with', 'short', 'angled', 'branch')

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

        oval('cut',10,28,6,12)
        path('trunk',(10,16),[('L',(22,16)),('L',(28,8)),('L',(36,12)),('L',(32,20)),('L',(38,20)),('C',(44,30),(42,20),(44,24)),('C',(38,40),(44,36),(42,40)),('L',(10,40))]);join('cut','trunk')
