"""The current cougar has a dog-like angular head and almost no tail. No written feedback. Restored a long curved tail, a small rounded ear, softer muzzle and horizontal back above two clear legs.
Construction: Lucide cat: small rounded facial vocabulary; source defines the long-tailed full-body cougar.
Plan: HRECT_L SOLO48; shared shape parameters and scoped real joins.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '22e27c10-01b3-4e0b-9a9f-8c3e35390cda'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__standing-mountain-lion-in-profile/20260929T115249Z-thuan-mac/reference/cougar_22e27c10-01b3-4e0b-9a9f-8c3e35390cda.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'standing-mountain-lion-in-profile'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('standing', 'mountain', 'lion', 'in', 'profile')
    
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

        path('cat',(16,20),[('L',(28,20)),('C',(33,13),(30,18),(31,15)),('C',(36,8),(33,8),(34,8)),('C',(39,13),(38,8),(39,11)),('C',(44,17),(42,13),(44,15)),('C',(39,22),(44,20),(42,22)),('L',(38,40)),('L',(30,40)),('L',(30,30)),('L',(22,30)),('L',(22,40)),('L',(14,40)),('L',(14,28)),('C',(16,20),(14,23),(14,20))],True)
        bez('tail',(16,20),((8,20),(4,24),(4,32)));join('tail','cat')
