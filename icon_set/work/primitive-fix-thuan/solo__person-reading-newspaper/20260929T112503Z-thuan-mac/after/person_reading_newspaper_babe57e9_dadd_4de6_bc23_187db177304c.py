"""Rejected reader had a tiny book and artificial shoulder loop. Enlarge the open newspaper and replace the loop with a short central torso behind the fold. Text omitted for clean spacing.
Symbol plan: human_ref/full_body_ref.png and Lucide newspaper original/atoms; head bottom16 to torso24 exact4 ink gap; shared central paper fold.
Keyshape VRECT_L: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'babe57e9-dadd-4de6-bc23-187db177304c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-reading-newspaper/20260929T112503Z-thuan-mac/reference/newspaper read_babe57e9-dadd-4de6-bc23-187db177304c.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'person-reading-newspaper'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('person', 'reading', 'newspaper')

    def build(self):

        def path(n,start,steps,closed=False):
            point=start; members=[]
            for j,(kind,end,*args) in enumerate(steps):
                m=f'{n}-{j}'
                if kind=='L': self.add_line(m,point,end)
                elif kind=='A': self.add_arc(m,point,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(m,point,(args[0],args[1],end))
                point=end; members.append(m)
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def join(a,b): self.relate('connect',a,b)
        def box(n,l,t,r,b,rad=3):
            path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)

        circle('head',24,10,6)
        line('torso',(24,24),(24,28))
        poly('paper',(8,24),(24,28),(40,24),(40,40),(24,44),(8,40),closed=True)
        line('fold',(24,28),(24,44));join('fold','paper');join('torso','paper');join('torso','fold')
        self.mark_human_figure('reader',head='head',torso='torso',torso_junction='start')
