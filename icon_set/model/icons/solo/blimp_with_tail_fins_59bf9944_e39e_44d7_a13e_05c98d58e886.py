"""Horizontal elliptical airship hull, separate upper/lower tail fins and hanging cabin; extremes 4,8,44,40.
Construction: No useful direct Lucide match
Reduction: No omissions; cabin and two fins retained.
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

        def path(name, start, steps, closed=False):
            here=start; members=[]
            for j,(kind,end,*args) in enumerate(steps):
                m=f'{name}-{j}'
                if kind=='L': self.add_line(m,here,end)
                else: self.add_arc(m,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2],large_arc=args[3] if len(args)>3 else False)
                members.append(m); here=end
            self.add_contour(name,*members,closed=closed)
        def poly(name,*pts,closed=False): self.add_polyline(name,*pts,closed=closed)
        def line(name,a,b): self.add_line(name,a,b)
        def join(a,b): self.relate('connect',a,b)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)

        path('hull',(4,22),[('A',(20,12),16,10,True),('A',(36,16),20,10,True),('L',(40,8)),('L',(44,8)),('L',(44,36)),('L',(40,36)),('L',(36,28)),('A',(28,32),12,8,True),('L',(16,32)),('A',(4,22),12,10,True)],True)
        poly('cabin',(16,32),(16,40),(28,40),(28,32));join('cabin','hull')
