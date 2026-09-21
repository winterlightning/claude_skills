"""Flying Blimp Airship.

Plan: Long airship hull with rear fins and hanging cabin. Bounds4,8,44,40. Asymmetry preserves right tail.
Construction reference: No useful local Lucide match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '59bf9944-e39e-44d7-a13e-05c98d58e886'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_07/blimp_59bf9944-e39e-44d7-a13e-05c98d58e886.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'blimp-with-tail-fins'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('blimp', 'with', 'tail', 'fins')

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

        path('hull',(4,24),[('C',(24,8),(4,14),(16,8)),('C',(32,16),(28,8),(30,12)),('C',(36,24),(34,19),(36,22)),('C',(32,30),(36,27),(34,29)),('C',(24,32),(30,32),(28,32)),('L',(16,32)),('C',(4,24),(8,32),(4,28))],True)
        poly('tail',(32,16),(44,8),(44,40),(32,30));join('tail','hull')
        poly('cabin',(16,32),(16,40),(24,40),(24,32));join('cabin','hull')
