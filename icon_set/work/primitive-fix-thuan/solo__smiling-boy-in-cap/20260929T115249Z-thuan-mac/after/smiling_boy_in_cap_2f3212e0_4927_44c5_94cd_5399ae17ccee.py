"""The current cap is flattened sideways and the eyes are missing. No written feedback. Restored a taller rounded lower face, a domed cap, paired eyes and a clear smile; ears are omitted.
Construction: Shared human_ref/user.svg: circular jaw. Source supplies domed cap and broad smile.
Plan: SQUARE SOLO48; shared shape parameters and scoped real joins.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '2f3212e0-4927-44c5-94cd-5399ae17ccee'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__smiling-boy-in-cap/20260929T115249Z-thuan-mac/reference/mario_2f3212e0-4927-44c5-94cd-5399ae17ccee.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'smiling-boy-in-cap'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('smiling', 'boy', 'in', 'cap')
    
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

        arc('cap',(6,15),(42,15),18,9)
        line('brim',(6,15),(42,15));join('cap','brim')
        path('face',(42,15),[('L',(42,24)),('A',(6,24),18),('L',(6,15))]);join('face','brim')
        for x in (16,32):self.add_dot('eye'+str(x),(x,24))
        bez('smile',(20,32),((22,34),(26,34),(28,32)))
