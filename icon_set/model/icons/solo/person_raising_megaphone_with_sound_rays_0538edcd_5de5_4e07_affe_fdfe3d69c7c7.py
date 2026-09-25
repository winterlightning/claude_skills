"""Person raises curved megaphone with two sound rays. Human full_body_ref.png: head(11,26), r5; torso(11,39) exact 4 ink gap. Lucide megaphone informs curved flared horn. Smooth raised arm replaces angular elbow.
Keyshape SQUARE; clean centerlines revision. Shared symbol parameters own paired geometry."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0538edcd-5de5-4e07-affe-fdfe3d69c7c7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_16/election campaign 3_0538edcd-5de5-4e07-affe-fdfe3d69c7c7.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='person-raising-megaphone-with-sound-rays'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    aliases=()
    keywords=('person', 'raising', 'megaphone', 'with', 'sound', 'rays')
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

        path('head',(6,26),[('A',(16,26),5,5,True),('A',(6,26),5,5,True)],True)
        line('torso',(11,39),(11,42));line('base',(6,42),(11,42))
        path('arm',(11,39),[('L',(18,39)),('C',(28,24),(28,39),(28,31))])
        path('horn',(28,24),[('C',(24,20),(25,24),(24,23)),('C',(28,14),(24,17),(25,16)),('C',(34,6),(30,12),(32,9)),('L',(34,26)),('C',(28,24),(31,24),(29,24))],True)
        line('ray-top',(42,9),(42,11));line('ray-bottom',(42,23),(42,25))
        join('arm','torso');join('torso','base');join('arm','horn')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
