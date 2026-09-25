"""A right-facing profile held above two mirrored cupped hands. Human reference guides simplified anatomy; Lucide hand informs continuous palms. Head is an open anatomical profile, not a detached stick figure, with deliberate nose corner.
Keyshape SQUARE; clean centerlines revision. Shared symbol parameters own paired geometry."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'efd5cbb3-73a1-456c-9d82-fa7470f26ad4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_33/self care 2_efd5cbb3-73a1-456c-9d82-fa7470f26ad4.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='hands-cupping-a-profile-head'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('hands', 'cupping', 'a', 'profile', 'head')
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

        for j,s in enumerate((-1,1)):
            def p(x,y):return(24+s*x,y)
            path(f'hand-{j}',p(7,42),[('C',p(18,34),p(7,38),p(18,40)),('L',p(18,24))])
            path(f'thumb-{j}',p(18,34),[('C',p(10,31),p(14,34),p(12,32))]);join(f'hand-{j}',f'thumb-{j}')
        path('profile',(17,23),[('C',(14,14),(17,19),(14,19)),('A',(22,6),8,8,True),('C',(30,12),(27,6),(29,8)),('L',(34,16)),('L',(30,16)),('L',(30,20)),('A',(27,23),3,3,True)])
