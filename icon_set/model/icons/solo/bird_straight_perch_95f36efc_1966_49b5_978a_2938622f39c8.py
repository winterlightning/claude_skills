"""Perched bird has round head, swept breast and long tail; extremes 8,4,40,44.
Construction: bird: circular head flowing into breast
Reduction: Tiny eye and inner wing omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '95f36efc-1966-49b5-978a-2938622f39c8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_30/perch_95f36efc-1966-49b5-978a-2938622f39c8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'bird-straight-perch'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ()
    keywords = ('bird', 'straight', 'perch')
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

        path('bird',(8,36),[('L',(20,16)),('L',(20,12)),('A',(36,12),8,8,True),('L',(40,14)),('L',(36,18)),('A',(22,32),14,14,True),('L',(16,32)),('L',(8,36))],True)
        poly('leg',(22,32),(27,44),(40,44));line('perch',(14,44),(27,44));join('leg','bird');join('leg','perch')
