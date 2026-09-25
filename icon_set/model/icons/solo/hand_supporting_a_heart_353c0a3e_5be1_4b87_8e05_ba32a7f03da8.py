"""Hand supports a symmetric heart. Lucide heart and hand-heart inform smooth lobes and curved thumb; reference keeps heart dominant. Shared heart axis and mirrored curves; palm has coherent rounded return.
Keyshape SQUARE; clean centerlines revision. Shared symbol parameters own paired geometry."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '353c0a3e-5be1-4b87-8e05-ba32a7f03da8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_33/romance pride lgbt heart hand holding_353c0a3e-5be1-4b87-8e05-ba32a7f03da8.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='hand-supporting-a-heart'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    aliases=()
    keywords=('hand', 'supporting', 'a', 'heart')
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

        path('thumb',(6,30),[('L',(12,26)),('C',(18,24),(14,24),(16,24)),('L',(20,24)),('L',(24,24)),('A',(24,32),4,4,True),('L',(18,32))])
        path('palm',(6,42),[('L',(24,42)),('C',(30,40),(27,42),(28,42)),('L',(36,35)),('C',(42,29),(40,35),(42,33)),('C',(36,23),(42,26),(39,23)),('L',(24,32))]);join('thumb','palm')
        path('heart',(20,24),[('C',(8,12),(15,19),(8,17)),('A',(14,6),6,6,True),('C',(20,9),(17,6),(19,7)),('C',(26,6),(21,7),(23,6)),('A',(32,12),6,6,True),('C',(20,24),(32,17),(25,19))],True);join('heart','thumb')
