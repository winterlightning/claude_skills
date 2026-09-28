"""Conductor with circular head, coherent curved shoulders and an angled raised baton. Human full_body_ref.png; head(24,12), r6, torso starts(24,26): exact 4 ink gap. Source action retained, outlined torso simplified.
Keyshape SQUARE; clean centerlines revision. Shared symbol parameters own paired geometry."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6659250b-ef9d-4624-8030-348af08008eb'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_12/conductor_6659250b-ef9d-4624-8030-348af08008eb.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='conductor-with-raised-baton'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases=()
    keywords=('conductor', 'with', 'raised', 'baton')
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

        circle('head',24,12,6)
        line('torso',(24,26),(24,42))
        path('left-arm',(24,26),[('L',(19,26)),('C',(9,32),(14,26),(14,32))])
        path('right-arm',(24,26),[('L',(29,26)),('C',(42,32),(34,26),(36,32))])
        line('baton',(9,32),(6,16))
        join('torso','left-arm');join('torso','right-arm');join('left-arm','right-arm');join('left-arm','baton')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
