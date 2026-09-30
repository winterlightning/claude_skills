"""The rejected masked woman had a vertical center bar and circular medallion-like face. Restore a swept hair part and a larger jaw with a face-mask upper edge.
Symbol plan: Original side-parted hair and mask; circular jaw follows human_ref/user.svg.
Keyshape SQUARE: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'e1f5e900-261d-4886-9c63-8beef0eb6820'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__woman-wearing-a-face-mask/20260929T124732Z-thuan-mac/reference/air purifier 5_e1f5e900-261d-4886-9c63-8beef0eb6820.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'woman-wearing-a-face-mask'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('woman', 'wearing', 'a', 'face', 'mask')

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

        path('hair',(6,42),[('C',(6,22),(10,37),(6,30)),('A',(42,22),18,16,True),('C',(42,42),(42,30),(38,37))])
        path('fringe',(14,22),[('C',(27,14),(21,22),(25,17)),('C',(34,22),(29,19),(31,21))])
        self.add_arc('jaw',(14,22),(34,22),radius_x=10,sweep=False);join('jaw','fringe')
        path('mask',(14,22),[('C',(24,21),(18,23),(21,21)),('C',(34,22),(27,21),(30,23))]);join('mask','jaw');join('mask','fringe')
