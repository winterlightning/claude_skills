"""Mirrored wings and antennae share an elongated striped body; extremes 6,6,42,42.
Construction: bug: paired appendages and coherent body outline
Reduction: Tiny legs omitted to retain open wing/body spacing.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd887ebc5-e028-4b29-95eb-d108a07e35c2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_36/sting_d887ebc5-e028-4b29-95eb-d108a07e35c2.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'bee-with-spread-wings-and-striped-abdomen'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('bee', 'with', 'spread', 'wings', 'and', 'striped', 'abdomen')
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

        path('body',(18,14),[('A',(30,14),6,6,True),('L',(30,18)),('L',(30,26)),('L',(30,30)),('L',(30,34)),('A',(24,42),6,8,True),('A',(18,34),6,8,True),('L',(18,30)),('L',(18,26)),('L',(18,18)),('L',(18,14))],True)
        for side,x in [('left',18),('right',30)]:
            path('wing-'+side,(x,18),[('A',(x,30),12,6,side=='right')]);join('wing-'+side,'body')
            line('antenna-'+side,(x,14),(14 if side=='left' else 34,6));join('antenna-'+side,'body')
        for y in (26,34):
            line('band-'+str(y),(18,y),(30,y));join('band-'+str(y),'body')
