"""The rejected side-parted woman had helmet-like hair and a tiny face. Restore fuller circular cheeks, extended hair and an asymmetric swept fringe over broad curved shoulders.
Symbol plan: human_ref/user.svg circular jaw and broad shoulders; asymmetric hair part follows the source. Jaw30, shoulders34 give touching ink.
Keyshape SQUARE: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'a3c34b6d-1a30-4e33-b102-7a97738a51db'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__woman-bust-with-side-parted-hair/20260929T124732Z-thuan-mac/reference/ex wife_a3c34b6d-1a30-4e33-b102-7a97738a51db.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'woman-bust-with-side-parted-hair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('woman', 'bust', 'with', 'side', 'parted', 'hair')
    human_construction = "bust"
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

        path('hair',(6,30),[('L',(6,24)),('A',(42,24),18,18,True),('L',(42,30))])
        self.add_arc('jaw',(14,20),(34,20),radius_x=10,sweep=False)
        path('fringe',(14,20),[('C',(27,16),(20,20),(24,18)),('C',(34,20),(29,19),(31,20))]);join('fringe','jaw')
        line('temple-left',(6,24),(14,20));line('temple-right',(34,20),(42,24))
        for n in ('temple-left','temple-right'):
         join(n,'hair');join(n,'jaw');join(n,'fringe')
        path('body',(6,42),[('A',(24,34),18,8,True),('A',(42,42),18,8,True)]);join('body','jaw')
