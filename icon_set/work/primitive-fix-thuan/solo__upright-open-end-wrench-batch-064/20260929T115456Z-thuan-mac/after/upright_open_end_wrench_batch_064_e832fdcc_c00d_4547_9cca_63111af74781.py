"""Wrench: rejected head has angular shoulders and handle is too short. Restore round head-to-handle transitions and a longer slim grip. Round the head shoulders and lengthen the handle below the wide open jaw.
Symbol plan: Lucide wrench original/atoms: rounded jaw shoulders and long grip; preserve upright original.
Keyshape VRECT_L: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'e832fdcc-c00d-4547-9cca-63111af74781'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__upright-open-end-wrench-batch-064/20260929T115456Z-thuan-mac/reference/hardware_e832fdcc-c00d-4547-9cca-63111af74781.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'upright-open-end-wrench-batch-064'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('upright', 'open', 'end', 'wrench', 'batch', '064')

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

        path('wrench',(16,4),[('L',(16,12)),('A',(32,12),8,8,False),('L',(32,4)),('A',(40,16),8,12,True),('L',(40,20)),('C',(30,29),(40,23),(33,27)),('L',(30,38)),('A',(18,38),6,6,True),('L',(18,29)),('C',(8,20),(15,27),(8,23)),('L',(8,16)),('A',(16,4),8,12,True)],True)
