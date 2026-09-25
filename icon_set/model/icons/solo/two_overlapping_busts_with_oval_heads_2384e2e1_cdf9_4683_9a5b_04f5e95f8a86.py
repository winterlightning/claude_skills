"""Two overlapping busts with equal circular heads and shared baseline. Human user.svg owns round heads and broad shoulders; Lucide users informs overlap. Source oval heads normalized to circular human vocabulary. Head bottoms18 and shoulders26 leave exact4 ink gap.
Keyshape SQUARE; clean centerlines revision. Shared symbol parameters own paired geometry."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2384e2e1-cdf9-4683-9a5b-04f5e95f8a86'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_35/spouse_2384e2e1-cdf9-4683-9a5b-04f5e95f8a86.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='two-overlapping-busts-with-oval-heads'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases=()
    keywords=('two', 'overlapping', 'busts', 'with', 'oval', 'heads')
    def build(self):

        def path(n, start, commands, closed=False):
            here=start; members=[]
            for j,(kind,end,*args) in enumerate(commands):
                ident=f'{n}-{j}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                members.append(ident); here=end
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def box(n,l,t,r,b,k=2):
            path(n,(l+k,t),[('L',(r-k,t)),('A',(r,t+k),k,k,True),('L',(r,b-k)),('A',(r-k,b),k,k,True),('L',(l+k,b)),('A',(l,b-k),k,k,True),('L',(l,t+k)),('A',(l+k,t),k,k,True)],True)
        line=self.add_line
        poly=self.add_polyline
        def join(a,b): self.relate('connect',a,b)

        for side,x in [('left',14),('right',34)]:circle('head-'+side,x,12,6)
        path('body-left',(6,42),[('L',(6,34)),('A',(14,26),8,8,True),('C',(24,36),(20,26),(24,30)),('L',(24,42)),('L',(6,42))],True)
        path('body-right',(24,36),[('C',(34,26),(24,30),(28,26)),('A',(42,34),8,8,True),('L',(42,42)),('L',(24,42))]);join('body-left','body-right')
