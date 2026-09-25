"""Polar Bear Side View.

Plan: Right-facing bear, bounds4,10,44,38. Broad shoulder, projecting muzzle, two blocky legs and belly opening; intentional profile asymmetry.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6097bc2c-3f1b-42e6-8c59-9537b60a8f18'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_06/bear body 1_6097bc2c-3f1b-42e6-8c59-9537b60a8f18.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'low-bear-silhouette-facing-right'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('low', 'bear', 'silhouette', 'facing', 'right')

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

        path('bear',(4,22),[('C',(14,10),(4,14),(7,10)),('C',(26,14),(19,10),(20,14)),('L',(34,14)),('L',(44,20)),('C',(36,26),(44,24),(40,26)),('C',(34,38),(34,28),(34,32)),('L',(26,38)),('L',(26,28)),('L',(16,28)),('L',(14,38)),('L',(6,38)),('L',(4,22))],True)
