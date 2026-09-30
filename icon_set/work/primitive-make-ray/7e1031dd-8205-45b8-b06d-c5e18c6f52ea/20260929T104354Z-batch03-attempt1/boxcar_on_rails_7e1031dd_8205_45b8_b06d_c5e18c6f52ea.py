'Made the freight-door marks longer and rebuilt a clean rounded box above two readable wheel bogies and a rail.\nOriginal/current comparison: The rejected wagon has stubby dot-like panel marks and protruding chassis bumps absent from the clean original.\nPlan: HRECT_L, bounds (2, 6, 46, 42); shared circles, mirrored pairs and explicit joined nodes.\nReference: No useful subject-specific Lucide match; geometric arcs and smooth coherent contours.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '7e1031dd-8205-45b8-b06d-c5e18c6f52ea'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__boxcar-on-rails/20260929T104354Z-thuan-mac/reference/railroad locomotive cargo_7e1031dd-8205-45b8-b06d-c5e18c6f52ea.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'boxcar-on-rails'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('boxcar', 'on', 'rails')

    def build(self):

        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def bez(n,a,*segments): self.add_bezier(n,a,*segments)
        def poly(n,*points,closed=False): self.add_polyline(n,*points,closed=closed)
        def con(n,*members,closed=False): self.add_contour(n,*members,closed=closed)
        def join(a,b): self.relate('connect',a,b)
        def circle(n,x,y,r):
            arc(n+'a',(x-r,y),(x+r,y),r)
            arc(n+'b',(x+r,y),(x-r,y),r)
            con(n,n+'a',n+'b',closed=True)
        def path(n,start,steps,closed=False):
            here=start; members=[]
            for i,(kind,end,*args) in enumerate(steps):
                m=f'{n}-{i}';members.append(m)
                if kind=='L': line(m,here,end)
                elif kind=='A': arc(m,here,end,*args)
                elif kind=='C': bez(m,here,(args[0],args[1],end))
                here=end
            con(n,*members,closed=closed)
        def rect(n,l,t,r,b,rad=4):
            path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad),('L',(r,b-rad)),('A',(r-rad,b),rad),('L',(l+rad,b)),('A',(l,b-rad),rad),('L',(l,t+rad)),('A',(l+rad,t),rad)],True)

        path('body',(10,8),[('L',(38,8)),('A',(42,12),4),('L',(42,24)),('A',(38,28),4),('L',(36,28)),('L',(12,28)),('L',(10,28)),('A',(6,24),4),('L',(6,12)),('A',(10,8),4)],True)
        for x in (18,30): line('panel-'+str(x),(x,16),(x,20))
        poly('rail',(4,40),(12,40),(36,40),(44,40))
        for x in (12,36):
            n='wheel-'+str(x);circle(n,x,34,6);join(n,'body');join(n,'rail')
