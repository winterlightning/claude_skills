"""Two circular cuffs linked by smooth flexible chain, separate key at lower right. Lucide key-round informs circular bow and straight toothed shaft. Source asymmetric diagonal composition retained; cuff rings equal radius.
Keyshape SQUARE; clean centerlines revision. Shared symbol parameters own paired geometry."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4a54478b-4849-4373-b597-046376cb8fb9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_13/crime tools shackle key_4a54478b-4849-4373-b597-046376cb8fb9.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='handcuff-pair-with-separate-key'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    aliases=()
    keywords=('handcuff', 'pair', 'with', 'separate', 'key')
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

        circle('cuff-left',14,34,8);circle('cuff-right',34,14,8)
        path('chain',(14,26),[('C',(8,12),(11,21),(8,17)),('C',(15,6),(8,7),(10,6)),('C',(26,14),(21,6),(26,8))]);join('chain','cuff-left');join('chain','cuff-right')
        circle('key-head',33,39,3)
        poly('key-shaft',(33,36),(42,30),(42,34));join('key-head','key-shaft')
