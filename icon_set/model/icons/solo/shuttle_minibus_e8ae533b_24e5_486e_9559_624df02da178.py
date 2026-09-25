"""Side View Public Shuttle Minibus.

Plan: Long shuttle cabin, two window divisions and equal wheel pair retained. Reduced pane count and omitted the close door seam. Keyshape HRECT_L uses its exact SOLO48 bounds; mirrored geometry only where the source supports it.
Construction reference: Lucide bus: shared window band and interrupted chassis; fewer wider panes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e8ae533b-24e5-486e-9559-624df02da178'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_27/minibus_e8ae533b-24e5-486e-9559-624df02da178.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'shuttle-minibus'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('shuttle', 'minibus')

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
            path(name,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def rect(name,x,y,w,h,r=4):
            path(name,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points,closed=False): self.add_polyline(name,*points,closed=closed)
        def join(a,b): self.relate('connect',a,b)

        path('body',(12,36),[('L',(4,36)),('L',(4,16)),('A',(12,8),8,8,True),('L',(34,8)),('C',(40,14),(38,8),(39,10)),('L',(44,26)),('L',(44,32)),('A',(40,36),4,4,True),('L',(36,36))])
        line('windows',(4,22),(43,22));join('windows','body')
        for x in [16,28]:
         line(f'pane{x}',(x,8),(x,22));join(f'pane{x}','body');join(f'pane{x}','windows')
        for x in [16,32]:
         circle(f'wheel{x}',x,36,4);join(f'wheel{x}','body')
        line('under',(20,36),(28,36));join('under','wheel16');join('under','wheel32')
