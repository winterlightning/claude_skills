"""Sharp Kitchen Knife.

Plan: Diagonal blade with a curved cutting edge and rounded lower-right handle. Centerline bounds6,6,42,42. Diagonal placement preserves a recognizable long knife within SOLO48.
Construction reference: No useful local Lucide match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1dc2167f-9221-4801-9aa7-1f646f10bc31'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/knife edge_1dc2167f-9221-4801-9aa7-1f646f10bc31.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'kitchen-knife'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('kitchen', 'knife')

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

        path('outline',(6,6),[('L',(28,22)),('L',(36,30)),('A',(42,36),6,6,True),('A',(36,42),6,6,True),('L',(22,28)),('C',(6,6),(8,28),(6,18))],True)
        line('seam',(28,22),(22,28));join('seam','outline')
