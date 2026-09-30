"""The current nightingale loses its folded wing and broad tail. No written feedback. Restored a short outlined tail, visible eye, curved wing seam and two bent legs around a rounded breast.
Construction: Lucide bird: eye, folded wing and coherent silhouette; source supplies short broad tail and two feet.
Plan: SQUARE SOLO48; shared shape parameters and scoped real joins.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '24f05ce6-133d-478e-9ef6-3d75b8bacf70'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__standing-nightingale/20260929T115249Z-thuan-mac/reference/nightingale_24f05ce6-133d-478e-9ef6-3d75b8bacf70.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'standing-nightingale'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('standing', 'nightingale')
    
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

        path('bird',(6,36),[('L',(22,18)),('L',(22,15)),('A',(31,6),9),('A',(40,15),9),('L',(42,17)),('L',(38,20)),('C',(32,32),(39,27),(36,30)),('C',(22,34),(28,34),(25,34)),('C',(20,33),(20,34),(18,33)),('L',(12,42)),('L',(6,36))],True)
        self.add_dot('eye',(31,15))
        bez('wing',(22,18),((23,21),(25,23),(24,25)));join('wing','bird')
        poly('leg-left',(22,34),(24,42),(28,42));poly('leg-right',(32,32),(36,42),(40,42));join('leg-left','bird');join('leg-right','bird')
