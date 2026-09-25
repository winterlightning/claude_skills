"""Craftsman holds an upright hammer. Human full_body_ref.png owns r7 head(15,13) and torso junction(15,28), exact 4 ink gap. Lucide hammer informs square striking face. Smooth arm bends; body cropped as source.
Keyshape SQUARE; clean centerlines revision. Shared symbol parameters own paired geometry."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '04ebbce5-fdd2-4c6c-bc45-d497a7339082'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_21/greek god hephaestus_04ebbce5-fdd2-4c6c-bc45-d497a7339082.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='craftsman-holding-a-hammer'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('craftsman', 'holding', 'a', 'hammer')
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

        circle('head',15,13,7)
        line('torso',(15,28),(15,42))
        path('left-arm',(15,28),[('C',(6,37),(10,28),(6,32)),('L',(6,42))])
        path('right-arm',(15,28),[('C',(29,36),(21,28),(23,36)),('L',(36,36))])
        box('hammer',30,14,42,24,2)
        poly('handle',(36,24),(36,36),(36,42))
        for a,b in [('torso','left-arm'),('torso','right-arm'),('left-arm','right-arm'),('hammer','handle'),('right-arm','handle')]:join(a,b)
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
