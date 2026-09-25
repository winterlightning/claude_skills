"""Fairy with circular head, dress and mirrored butterfly wings. Human full_body_ref.png owns head(24,10),r4 and torso(24,22):4 ink gap. Paired upper lobes and lower lobes use shared axis and continuous curves. No useful local Lucide fairy match.
Keyshape SQUARE; clean centerlines revision. Shared symbol parameters own paired geometry."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9f2464f7-258f-5a66-a48b-a08297ea0c92'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-022/references/01-9f2464f7-258f-5a66-a48b-a08297ea0c92.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='fairy-with-butterfly-wings'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "video-games"
    categories = ("primitives", "video-games")
    aliases=()
    keywords=('fairy', 'with', 'butterfly', 'wings')
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

        circle('head',24,10,4)
        poly('torso',(24,22),(24,27),(24,32))
        poly('skirt',(16,42),(24,32),(32,42),closed=True);join('torso','skirt')
        for j,s in enumerate((-1,1)):
            def p(x,y):return(24+s*x,y)
            path(f'wing-{j}',(24,27),[('C',p(18,16),p(7,21),p(13,16)),('L',p(18,21)),('C',p(14,26),p(18,24),p(17,26)),('C',p(18,34),p(18,28),p(18,31))])
            join('torso',f'wing-{j}')
        join('wing-0','wing-1')
        self.mark_human_figure('person',head='head',torso='torso-1',torso_junction='start')
