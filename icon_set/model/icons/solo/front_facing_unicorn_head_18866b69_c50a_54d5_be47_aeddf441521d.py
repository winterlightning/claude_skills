"""Frontal unicorn: long curved muzzle, two symmetric ears, eyes and central horn. Lucide dog informs continuous animal face contour; pointed horn/ears intentionally angular. Outlined central horn and diagonal ears preserve the defining unicorn identity.
Keyshape VRECT_L; clean centerlines revision. Shared symbol parameters own paired geometry."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '18866b69-c50a-54d5-be47-aeddf441521d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-022/references/06-18866b69-c50a-54d5-be47-aeddf441521d.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='front-facing-unicorn-head'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "video-games"
    categories = ("primitives", "video-games")
    aliases=()
    keywords=('front', 'facing', 'unicorn', 'head')
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

        path('face',(11,24),[('L',(11,31)),('A',(24,44),13,13,False),('A',(37,31),13,13,False),('L',(37,24)),('C',(32,16),(37,20),(34,18)),('L',(24,16)),('L',(16,16)),('C',(11,24),(14,18),(11,20))],True)
        poly('horn',(20,16),(24,4),(28,16));join('face','horn')
        for s in (-1,1):
            line('ear'+str(s),(24+s*8,16),(24+s*16,10));join('face','ear'+str(s))
        for x in(20,28):self.add_dot('eye'+str(x),(x,27))
