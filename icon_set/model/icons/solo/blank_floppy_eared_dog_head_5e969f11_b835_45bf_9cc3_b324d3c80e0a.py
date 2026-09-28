"""Simple Dog Head.

Plan: Blank rounded dog face and two mirrored floppy ears retained without inventing facial details. Keyshape HRECT_L uses its exact SOLO48 bounds; mirrored geometry only where the source supports it.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5e969f11-b835-45bf-9cc3-b324d3c80e0a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_28/mutt_5e969f11-b835-45bf-9cc3-b324d3c80e0a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'blank-floppy-eared-dog-head'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('blank', 'floppy', 'eared', 'dog', 'head')

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

        path('face',(14,10),[('C',(24,8),(17,8),(20,8)),('C',(34,10),(28,8),(31,8)),('L',(36,26)),('C',(24,40),(35,35),(32,40)),('C',(12,26),(16,40),(13,35)),('L',(14,10))],True)
        path('left-ear',(14,10),[('C',(4,18),(8,8),(4,12)),('C',(12,26),(4,24),(8,30))]);join('left-ear','face')
        path('right-ear',(34,10),[('C',(44,18),(40,8),(44,12)),('C',(36,26),(44,24),(40,30))]);join('right-ear','face')
