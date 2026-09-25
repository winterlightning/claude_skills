"""Prehistoric Mammoth with Long Tusks.

Plan: Left-facing mammoth with trunk, tusk and two legs. Bounds4,8,44,40. Omit eye and ear detail to preserve trunk/tusk separation.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a28d0f50-89ab-4114-8acd-5f487e570ca3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_26/mammoth_a28d0f50-89ab-4114-8acd-5f487e570ca3.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'mammoth-with-long-trunk-and-curved-tusk'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('mammoth', 'with', 'long', 'trunk', 'and', 'curved', 'tusk')

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

        path('body',(12,32),[('L',(12,18)),('C',(22,8),(12,10),(16,8)),('C',(28,12),(25,8),(27,10)),('C',(44,24),(38,12),(44,16)),('L',(44,40)),('L',(36,40)),('L',(36,30)),('L',(28,30)),('L',(28,40)),('L',(20,40)),('L',(20,25)),('C',(12,32),(17,25),(16,32))],True)
        path('trunk',(12,32),[('L',(12,36)),('A',(4,36),4,4,True),('L',(4,22))]);join('trunk','body')
        path('tusk',(12,18),[('C',(4,12),(6,18),(4,16))]);join('tusk','body')
