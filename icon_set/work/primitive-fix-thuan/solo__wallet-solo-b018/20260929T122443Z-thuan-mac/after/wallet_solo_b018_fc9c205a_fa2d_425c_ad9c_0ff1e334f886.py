"""The rejected wallet became a tall bag. Restore a wider rectangular wallet with a folded upper edge and a large inset clasp on the right.
Symbol plan: Lucide wallet original and atoms: rounded wallet body, folded upper edge and side clasp.
Keyshape HRECT_L: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'fc9c205a-fa2d-425c-ad9c-0ff1e334f886'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__wallet-solo-b018/20260929T122443Z-thuan-mac/reference/wallet_fc9c205a-fa2d-425c-ad9c-0ff1e334f886.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'wallet-solo-b018'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('wallet', 'solo', 'b018')

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

        path('body',(8,8),[('L',(36,8)),('A',(40,12),4,4,True),('L',(40,16)),('L',(44,20)),('L',(44,36)),('A',(40,40),4,4,True),('L',(8,40)),('A',(4,36),4,4,True),('L',(4,12)),('A',(8,8),4,4,True)],True)
        line('fold',(4,16),(31,16));join('body','fold')
        path('clasp',(44,24),[('L',(32,24)),('A',(32,32),4,4,False),('L',(44,32))]);join('clasp','body')
