"""Envelope with symmetric flap, rounded rectangle and a true shared diagonal seam junction; extremes 4,8,44,40.
Construction: mail: rounded enclosure with shallow symmetric flap
Reduction: No omissions; single lower-right back seam retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1562f98c-4790-44ea-971c-d68ba4454109'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_14/dart logo_1562f98c-4790-44ea-971c-d68ba4454109.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'closed-envelope-with-diagonal-back-seam'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('closed', 'envelope', 'with', 'diagonal', 'back', 'seam')
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

        path('outline',(8,8),[('L',(40,8)),('A',(44,12),4,4,True),('L',(44,36)),('A',(40,40),4,4,True),('L',(8,40)),('A',(4,36),4,4,True),('L',(4,12)),('A',(8,8),4,4,True)],True)
        poly('flap',(4,12),(24,28),(34,20),(44,12));join('flap','outline')
        line('seam',(34,20),(44,36));join('seam','flap');join('seam','outline')
