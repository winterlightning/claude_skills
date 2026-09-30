'Made the inward-raised brows consistent and broadened the shallow frown.\nOriginal/current comparison: The rejected tiny mouth and uneven brows weaken the worried, confused expression in the original.\nPlan: CIRCLE, bounds (2, 2, 46, 46); shared circles, mirrored pairs and explicit joined nodes.\nReference: No useful subject-specific Lucide match; geometric arcs and smooth coherent contours.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '23110766-a392-579a-844c-0825b0fac7bc'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__confused-face/20260929T104354Z-thuan-mac/reference/confuse_23110766-a392-579a-844c-0825b0fac7bc.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'confused-face'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('confused', 'face')

    def build(self):

        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def bez(n,a,*segments): self.add_bezier(n,a,*segments)
        def poly(n,*points,closed=False): self.add_polyline(n,*points,closed=closed)
        def con(n,*members,closed=False): self.add_contour(n,*members,closed=closed)
        def join(a,b): self.relate('connect',a,b)
        def circle(n,x,y,r):
            pts=[(x,y-r),(x+r,y),(x,y+r),(x-r,y),(x,y-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])):arc(n+str(j),a,b,r)
            con(n,*(n+str(j) for j in range(4)),closed=True)
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

        circle('face',24,24,20)
        line('brow-left',(16,16),(20,14));line('brow-right',(28,14),(32,16))
        for x in (16,32):self.add_dot('eye-'+str(x),(x,24))
        bez('frown',(19,34),((22,31),(26,31),(29,34)))
