"""The rejected boy has a square lower face and a rigid symmetric fringe. No written feedback. Restored a circular lower jaw and an asymmetric swept hairline with clear eyes and smile; ears and eyebrows are omitted.
Construction: Shared human_ref/user.svg: circular lower jaw; source supplies the swept fringe and smile.
Plan: SQUARE SOLO48; shared shape parameters and scoped real joins.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '41efa512-77c6-49b9-9e5d-7406a2d96367'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__smiling-boy-face-reference-41efa512/20260929T115249Z-thuan-mac/reference/cute male boy charactor_41efa512-77c6-49b9-9e5d-7406a2d96367.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'smiling-boy-face-reference-41efa512'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('smiling', 'boy', 'face', 'reference', '41efa512')
    
    def build(self):

        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*ps,closed=False): self.add_polyline(n,*ps,closed=closed)
        def bez(n,a,*ss): self.add_bezier(n,a,*ss)
        def arc(n,a,b,rx,ry=None,s=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry,sweep=s)
        def circle(n,x,y,r):
            arc(n+'a',(x-r,y),(x+r,y),r);arc(n+'b',(x+r,y),(x-r,y),r)
            self.add_contour(n,n+'a',n+'b',closed=True)
        def path(n,a,commands,closed=False):
            members=[]
            for j,c in enumerate(commands):
                k,b,*args=c; name=n+str(j)
                if k=='L': line(name,a,b)
                elif k=='A': arc(name,a,b,*args)
                elif k=='C': bez(name,a,(args[0],args[1],b))
                members.append(name);a=b
            self.add_contour(n,*members,closed=closed)
        def rect(n,x,y,w,h,r=0):
            if not r: poly(n,(x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True);return
            path(n,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r),('L',(x+r,y+h)),('A',(x,y+h-r),r),('L',(x,y+r)),('A',(x+r,y),r)],True)
        def join(*ns): self.relate('connect',*ns)

        path('head',(6,24),[('L',(6,18)),('A',(18,6),12),('L',(30,6)),('A',(42,18),12),('L',(42,24)),('A',(6,24),18)],True)
        bez('fringe',(6,18),((14,18),(23,14),(28,14)),((33,14),(34,18),(42,18)));join('head','fringe')
        for x in (18,30):self.add_dot('eye'+str(x),(x,25))
        bez('smile',(22,32),((23,34),(25,34),(26,32)))
