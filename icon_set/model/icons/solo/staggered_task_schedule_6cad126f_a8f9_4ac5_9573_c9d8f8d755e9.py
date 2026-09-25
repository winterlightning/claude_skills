"""Project Schedule Gantt Chart.

Plan: Schedule diagram bounds6,6,42,42. Six task boxes in three/two/one sequences; each task minimum8 high. Shared corner contacts reflect source.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6cad126f-a8f9-4ac5-9573-c9d8f8d755e9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_40/workflow gantt chart 2_6cad126f-a8f9-4ac5-9573-c9d8f8d755e9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'staggered-task-schedule'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'Uncategorized'
    aliases = ()
    keywords = ('staggered', 'task', 'schedule')

    def build(self):

        def path(name, start, commands, closed=False):
            here=start; members=[]
            for index,(kind,end,*args) in enumerate(commands):
                member=f"{name}-{index}"
                if kind=='L': self.add_line(member,here,end)
                elif kind=='A': self.add_arc(member,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(member,here,(args[0],args[1],end))
                here=end; members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def rect(name,x,y,w,h,r=4):
            path(name,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points,closed=False): self.add_polyline(name,*points,closed=closed)
        def join(a,b): self.relate('connect',a,b)

        # Six task bars retain the source's 3 / 2 / 1 arrangement. Stroke bars replace small outlined boxes.
        for name,x,y,w in [('a',6,6,12),('b',18,14,12),('c',30,22,12),('d',6,22,12),('e',18,30,12),('f',6,42,8)]:
         line(name,(x,y),(x+w,y))
